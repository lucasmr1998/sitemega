from django.core.cache import cache

from .models import SiteConfig, MenuItem, FooterColumn

CACHE_TTL = 300  # 5 min


def site_context(request):
    config = SiteConfig.load()  # already cached

    menus = cache.get('main_menus')
    if menus is None:
        menus = list(
            MenuItem.objects
            .filter(parent__isnull=True, menu_location='main')
            .prefetch_related('children')
        )
        cache.set('main_menus', menus, CACHE_TTL)

    algar_menus = cache.get('algar_menus')
    if algar_menus is None:
        algar_menus = list(
            MenuItem.objects
            .filter(parent__isnull=True, menu_location='algar')
            .prefetch_related('children', 'columns__links')
        )
        cache.set('algar_menus', algar_menus, CACHE_TTL)

    footer_columns = cache.get('footer_columns')
    if footer_columns is None:
        footer_columns = list(FooterColumn.objects.prefetch_related('links'))
        cache.set('footer_columns', footer_columns, CACHE_TTL)

    return {
        'config': config,
        'menus': menus,
        'algar_menus': algar_menus,
        'footer_columns': footer_columns,
    }
