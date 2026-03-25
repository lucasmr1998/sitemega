from .models import SiteConfig, MenuItem, FooterColumn


def site_context(request):
    config = SiteConfig.load()
    menus = (
        MenuItem.objects
        .filter(parent__isnull=True, menu_location='main')
        .prefetch_related('children')
    )
    algar_menus = (
        MenuItem.objects
        .filter(parent__isnull=True, menu_location='algar')
        .prefetch_related('children', 'columns__links')
    )
    footer_columns = FooterColumn.objects.prefetch_related('links')

    return {
        'config': config,
        'menus': menus,
        'algar_menus': algar_menus,
        'footer_columns': footer_columns,
    }
