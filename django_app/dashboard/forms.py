from django import forms
from core.models import SiteConfig, MenuItem, FooterColumn


class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfig
        exclude = ['id']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'link', 'menu_location', 'is_mega_menu', 'order']


class FooterColumnForm(forms.ModelForm):
    class Meta:
        model = FooterColumn
        fields = '__all__'
