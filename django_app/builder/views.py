from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Page, PageView


def page_view(request, slug=None):
    """Renderiza qualquer página dinâmica pelo slug."""
    if slug is None:
        page = Page.objects.filter(is_homepage=True, status='published').first()
        if not page:
            raise Http404('Nenhuma página inicial configurada')
    else:
        page = get_object_or_404(Page, slug=slug, status='published')

    # Track pageview
    PageView.record(page)

    sections = page.get_sections()

    return render(request, 'builder/page.html', {
        'page': page,
        'sections': sections,
    })


def lojas_redirect(request):
    return redirect('https://megalinktelecom.com.br/lojas')
