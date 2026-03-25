import json
import logging

import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Lead

logger = logging.getLogger(__name__)


def _get_client_ip(request):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        return x_forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


@csrf_exempt
@require_POST
def submit_lead(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)

    lead = Lead.objects.create(
        source=data.get('formSource', 'geral'),
        nome=data.get('nome', ''),
        email=data.get('email', ''),
        celular=data.get('celular', ''),
        cep=data.get('cep', ''),
        media_conta=data.get('media_conta', ''),
        tipo_veiculo=data.get('tipo_veiculo', ''),
        cpf=data.get('cpf', ''),
        ip_address=_get_client_ip(request),
    )

    webhook_url = getattr(settings, 'LEAD_WEBHOOK_URL', '')
    if webhook_url:
        try:
            requests.post(webhook_url, json=data, timeout=5)
            lead.webhook_sent = True
            lead.save(update_fields=['webhook_sent'])
        except requests.RequestException:
            logger.warning('Falha ao enviar webhook para lead %s', lead.pk)

    return JsonResponse({'status': 'ok', 'id': lead.pk})
