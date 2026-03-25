from django import forms
from core.models import SiteConfig, MenuItem, FooterColumn, FooterLink
from pages.models import (
    Banner, InternetPlan, PlanFeature, Combo, Service, SelfServiceItem,
    AppPromo, MegaEnergiaHome, EnergyHero, EnergySavings, EnergyFeature,
    EnergyStep, TrackingHero, TrackingFeature, TrackingBenefit, TrackingCTA,
)


class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfig
        exclude = ['id']


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'


class InternetPlanForm(forms.ModelForm):
    class Meta:
        model = InternetPlan
        fields = '__all__'


class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class SelfServiceItemForm(forms.ModelForm):
    class Meta:
        model = SelfServiceItem
        fields = '__all__'


class AppPromoForm(forms.ModelForm):
    class Meta:
        model = AppPromo
        fields = '__all__'


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'link', 'menu_location', 'is_mega_menu', 'order']


class FooterColumnForm(forms.ModelForm):
    class Meta:
        model = FooterColumn
        fields = '__all__'


class MegaEnergiaHomeForm(forms.ModelForm):
    class Meta:
        model = MegaEnergiaHome
        exclude = ['id']


class EnergyHeroForm(forms.ModelForm):
    class Meta:
        model = EnergyHero
        exclude = ['id']


class EnergySavingsForm(forms.ModelForm):
    class Meta:
        model = EnergySavings
        exclude = ['id']


class EnergyFeatureForm(forms.ModelForm):
    class Meta:
        model = EnergyFeature
        fields = '__all__'


class EnergyStepForm(forms.ModelForm):
    class Meta:
        model = EnergyStep
        fields = '__all__'


class TrackingHeroForm(forms.ModelForm):
    class Meta:
        model = TrackingHero
        exclude = ['id']


class TrackingFeatureForm(forms.ModelForm):
    class Meta:
        model = TrackingFeature
        fields = '__all__'


class TrackingBenefitForm(forms.ModelForm):
    class Meta:
        model = TrackingBenefit
        fields = '__all__'


class TrackingCTAForm(forms.ModelForm):
    class Meta:
        model = TrackingCTA
        exclude = ['id']
