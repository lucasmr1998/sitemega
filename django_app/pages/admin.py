from django.contrib import admin

from .models import (
    Banner, InternetPlan, PlanFeature, Combo, Service, SelfServiceItem,
    AppPromo, MegaEnergiaHome, EnergyHero, EnergySavings, EnergyFeature,
    EnergyStep, TrackingHero, TrackingFeature, TrackingBenefit, TrackingCTA,
    BlogPost,
)


# ─── Banners ─────────────────────────────────────────────────────────────────

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'is_active', 'order')
    list_filter = ('page', 'is_active')
    list_editable = ('is_active', 'order')


# ─── Planos de Internet ──────────────────────────────────────────────────────

class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 3


@admin.register(InternetPlan)
class InternetPlanAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'page', 'current_price', 'show_badge', 'is_active', 'order')
    list_filter = ('page', 'is_active')
    list_editable = ('order', 'is_active')
    inlines = [PlanFeatureInline]
    fieldsets = (
        (None, {'fields': ('page', 'category_label', 'speed_value', 'speed_unit')}),
        ('Preço', {'fields': ('current_price', 'old_price', 'period')}),
        ('Botão', {'fields': ('button_text', 'button_link')}),
        ('Badge', {
            'fields': ('show_badge', 'badge_text', 'badge_bg_color', 'badge_text_color'),
            'classes': ('collapse',),
        }),
        ('Cores', {
            'fields': ('title_color', 'speed_color', 'underline_color',
                       'button_bg_color', 'button_text_color'),
            'classes': ('collapse',),
        }),
        ('Status', {'fields': ('is_active', 'order')}),
    )


# ─── Combos ──────────────────────────────────────────────────────────────────

@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


# ─── Serviços ────────────────────────────────────────────────────────────────

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


# ─── Autoatendimento ─────────────────────────────────────────────────────────

@admin.register(SelfServiceItem)
class SelfServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'highlight', 'order')
    list_editable = ('order', 'highlight')


# ─── App Promo ───────────────────────────────────────────────────────────────

@admin.register(AppPromo)
class AppPromoAdmin(admin.ModelAdmin):
    list_display = ('page', 'app_name')
    list_filter = ('page',)


# ─── Singleton admins ────────────────────────────────────────────────────────

class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(MegaEnergiaHome)
class MegaEnergiaHomeAdmin(SingletonAdmin):
    pass


@admin.register(EnergyHero)
class EnergyHeroAdmin(SingletonAdmin):
    pass


@admin.register(EnergySavings)
class EnergySavingsAdmin(SingletonAdmin):
    pass


@admin.register(TrackingHero)
class TrackingHeroAdmin(SingletonAdmin):
    pass


@admin.register(TrackingCTA)
class TrackingCTAAdmin(SingletonAdmin):
    pass


# ─── Orderable list admins ───────────────────────────────────────────────────

@admin.register(EnergyFeature)
class EnergyFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(EnergyStep)
class EnergyStepAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)


@admin.register(TrackingFeature)
class TrackingFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(TrackingBenefit)
class TrackingBenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


# ─── Blog ────────────────────────────────────────────────────────────────────

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_tag', 'order')
    list_editable = ('order',)
