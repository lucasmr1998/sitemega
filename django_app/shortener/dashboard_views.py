import json
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import ShortLink, ShortLinkClick

LOGIN_URL = '/painel/login'


@login_required(login_url=LOGIN_URL)
def links_list(request):
    q = request.GET.get('q', '').strip()
    qs = ShortLink.objects.annotate(click_count=Count('clicks'))
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'dashboard/shortener/links_list.html', {
        'sidebar_active': 'shortener',
        'links': qs[:100],
        'query': q,
        'total_links': ShortLink.objects.count(),
        'total_clicks': ShortLinkClick.objects.count(),
    })


@login_required(login_url=LOGIN_URL)
def link_form(request, pk=None):
    instance = get_object_or_404(ShortLink, pk=pk) if pk else None

    if request.method == 'POST':
        destination = request.POST.get('destination_url', '').strip()
        title = request.POST.get('title', '').strip()
        code = request.POST.get('code', '').strip()
        is_active = request.POST.get('is_active') == 'on'

        if not destination:
            messages.error(request, 'URL de destino é obrigatória.')
        else:
            if instance:
                instance.destination_url = destination
                instance.title = title
                if code and code != instance.code:
                    if ShortLink.objects.filter(code=code).exclude(pk=instance.pk).exists():
                        messages.error(request, f'O código "{code}" já está em uso.')
                        return render(request, 'dashboard/shortener/link_form.html', {
                            'sidebar_active': 'shortener', 'link': instance,
                        })
                    instance.code = code
                instance.is_active = is_active
                instance.save()
                messages.success(request, 'Link atualizado!')
            else:
                kwargs = {'destination_url': destination, 'title': title,
                          'is_active': is_active, 'created_by': request.user}
                if code:
                    if ShortLink.objects.filter(code=code).exists():
                        messages.error(request, f'O código "{code}" já está em uso.')
                        return render(request, 'dashboard/shortener/link_form.html', {
                            'sidebar_active': 'shortener', 'link': None,
                        })
                    kwargs['code'] = code
                ShortLink.objects.create(**kwargs)
                messages.success(request, 'Link criado!')
            return redirect('dashboard:links_list')

    return render(request, 'dashboard/shortener/link_form.html', {
        'sidebar_active': 'shortener',
        'link': instance,
    })


@login_required(login_url=LOGIN_URL)
@require_POST
def link_delete(request, pk):
    link = get_object_or_404(ShortLink, pk=pk)
    link.delete()
    messages.success(request, 'Link excluído!')
    return redirect('dashboard:links_list')


@login_required(login_url=LOGIN_URL)
def link_stats(request, pk):
    link = get_object_or_404(ShortLink, pk=pk)
    today = timezone.localdate()
    thirty_days_ago = today - timedelta(days=29)

    # Daily clicks chart
    daily = (
        link.clicks.filter(clicked_at__date__gte=thirty_days_ago)
        .annotate(day=TruncDate('clicked_at'))
        .values('day')
        .annotate(total=Count('id'))
        .order_by('day')
    )
    daily_map = {item['day']: item['total'] for item in daily}

    labels, data = [], []
    for i in range(30):
        day = thirty_days_ago + timedelta(days=i)
        labels.append(day.strftime('%d/%m'))
        data.append(daily_map.get(day, 0))

    # Recent clicks
    recent = link.clicks.all()[:20]

    # Top referers
    top_referers = (
        link.clicks.exclude(referer='')
        .values('referer')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    return render(request, 'dashboard/shortener/link_stats.html', {
        'sidebar_active': 'shortener',
        'link': link,
        'total_clicks': link.clicks.count(),
        'clicks_today': link.clicks.filter(clicked_at__date=today).count(),
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
        'recent_clicks': recent,
        'top_referers': top_referers,
    })
