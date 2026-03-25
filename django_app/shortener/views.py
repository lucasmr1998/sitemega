from django.shortcuts import redirect, get_object_or_404

from .models import ShortLink, ShortLinkClick


def redirect_view(request, code):
    """Redireciona o link curto e registra o clique."""
    link = get_object_or_404(ShortLink, code=code, is_active=True)

    # Track click
    ShortLinkClick.objects.create(
        link=link,
        ip_address=_get_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
        referer=request.META.get('HTTP_REFERER', '')[:2000],
    )

    return redirect(link.destination_url)


def _get_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')
