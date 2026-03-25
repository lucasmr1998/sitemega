from django.contrib import admin
import nested_admin

from .models import (
    SiteConfig, MenuItem, MegaMenuColumn, MegaMenuLink,
    FooterColumn, FooterLink,
)


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identidade', {
            'fields': ('company_name', 'logo', 'logo_alt_text', 'favicon'),
        }),
        ('Cores', {
            'fields': ('primary_color', 'primary_dark_color', 'secondary_color', 'accent_color'),
            'description': 'Cores em formato hex (#RRGGBB)',
        }),
        ('Contato', {
            'fields': ('whatsapp_number', 'phone', 'email', 'address'),
        }),
        ('Redes Sociais', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'youtube_url'),
        }),
        ('Header', {
            'fields': ('assine_ja_enabled', 'assine_ja_link', 'area_cliente_enabled', 'area_cliente_link'),
        }),
        ('Rodapé', {
            'fields': ('footer_text', 'company_address', 'company_phone', 'company_email',
                       'footer_copyright', 'footer_terms_url', 'footer_privacy_url'),
        }),
    )

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ─── Menus ────────────────────────────────────────────────────────────────────

class MegaMenuLinkInline(nested_admin.NestedTabularInline):
    model = MegaMenuLink
    extra = 1


class MegaMenuColumnInline(nested_admin.NestedStackedInline):
    model = MegaMenuColumn
    extra = 0
    inlines = [MegaMenuLinkInline]


class MenuItemChildInline(nested_admin.NestedTabularInline):
    model = MenuItem
    fk_name = 'parent'
    extra = 0
    fields = ('title', 'link', 'order')


@admin.register(MenuItem)
class MenuItemAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'link', 'menu_location', 'parent', 'order')
    list_filter = ('menu_location',)
    list_editable = ('order',)
    inlines = [MenuItemChildInline, MegaMenuColumnInline]

    def get_queryset(self, request):
        return super().get_queryset(request).filter(parent__isnull=True)


# ─── Footer ──────────────────────────────────────────────────────────────────

class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


@admin.register(FooterColumn)
class FooterColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [FooterLinkInline]
