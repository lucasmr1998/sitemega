import json
import logging

import requests
from django.conf import settings
from django.core.cache import cache
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Lead

logger = logging.getLogger(__name__)

VALID_SOURCES = {'energia', 'rastreamento', 'internet', 'geral'}
MAX_LEADS_PER_IP_PER_HOUR = 10


def _get_client_ip(request):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        return x_forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


@csrf_exempt
@require_POST
def submit_lead(request):
    # Rate limiting by IP
    ip = _get_client_ip(request)
    rate_key = f'lead_rate:{ip}'
    attempts = cache.get(rate_key, 0)
    if attempts >= MAX_LEADS_PER_IP_PER_HOUR:
        return JsonResponse({'error': 'Muitas tentativas. Tente novamente em breve.'}, status=429)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)

    # Validate required fields
    nome = data.get('nome', '').strip()
    if not nome:
        return JsonResponse({'error': 'Nome é obrigatório'}, status=400)

    # Validate email if provided
    email = data.get('email', '').strip()
    if email:
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'error': 'Email inválido'}, status=400)

    # Validate source
    source = data.get('formSource', 'geral')
    if source not in VALID_SOURCES:
        source = 'geral'

    # Sanitize string fields (max lengths)
    lead = Lead.objects.create(
        source=source,
        nome=nome[:200],
        email=email[:254],
        celular=data.get('celular', '').strip()[:20],
        cep=data.get('cep', '').strip()[:10],
        media_conta=data.get('media_conta', '').strip()[:100],
        tipo_veiculo=data.get('tipo_veiculo', '').strip()[:100],
        cpf=data.get('cpf', '').strip()[:14],
        ip_address=ip,
    )

    # Increment rate limit
    cache.set(rate_key, attempts + 1, 3600)

    # Webhook
    webhook_url = getattr(settings, 'LEAD_WEBHOOK_URL', '')
    if webhook_url:
        try:
            requests.post(webhook_url, json=data, timeout=5)
            lead.webhook_sent = True
            lead.save(update_fields=['webhook_sent'])
        except requests.RequestException:
            logger.warning('Falha ao enviar webhook para lead %s', lead.pk)

    return JsonResponse({'status': 'ok', 'id': lead.pk})
