import json
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from core.models import SiteConfig, MenuItem, FooterColumn
from pages.models import (
    Banner, InternetPlan, Combo, Service, SelfServiceItem, AppPromo,
    MegaEnergiaHome, EnergyHero, EnergySavings, EnergyFeature, EnergyStep,
    TrackingHero, TrackingFeature, TrackingBenefit, TrackingCTA,
)
from leads.models import Lead

from .forms import (
    SiteConfigForm, BannerForm, InternetPlanForm, ComboForm, ServiceForm,
    SelfServiceItemForm, AppPromoForm, MenuItemForm, FooterColumnForm,
    MegaEnergiaHomeForm, EnergyHeroForm, EnergySavingsForm, EnergyFeatureForm,
    EnergyStepForm, TrackingHeroForm, TrackingFeatureForm, TrackingBenefitForm,
    TrackingCTAForm,
)


# ─── Auth ─────────────────────────────────────────────────────────────────────

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('dashboard:index')
    return render(request, 'dashboard/login.html', {'form': True if request.method == 'POST' else False})


def logout_view(request):
    logout(request)
    return redirect('dashboard:login')


# ─── Dashboard Index ──────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def index(request):
    today = timezone.localdate()
    seven_days_ago = today - timedelta(days=6)

    # Chart data
    labels, data = [], []
    for i in range(7):
        day = seven_days_ago + timedelta(days=i)
        labels.append(day.strftime('%d/%m'))
        data.append(Lead.objects.filter(created_at__date=day).count())

    content_counts = [
        {'label': 'Banners', 'count': Banner.objects.count(), 'icon': 'fa-solid fa-images', 'url': '/painel/banners'},
        {'label': 'Planos', 'count': InternetPlan.objects.count(), 'icon': 'fa-solid fa-wifi', 'url': '/painel/planos'},
        {'label': 'Combos', 'count': Combo.objects.count(), 'icon': 'fa-solid fa-cubes', 'url': '/painel/combos'},
        {'label': 'Serviços', 'count': Service.objects.count(), 'icon': 'fa-solid fa-concierge-bell', 'url': '/painel/servicos'},
        {'label': 'Autoatend.', 'count': SelfServiceItem.objects.count(), 'icon': 'fa-solid fa-headset', 'url': '/painel/autoatendimento'},
        {'label': 'Leads', 'count': Lead.objects.count(), 'icon': 'fa-solid fa-users', 'url': '/painel/leads'},
    ]

    return render(request, 'dashboard/index.html', {
        'nav_active': 'dashboard',
        'total_leads': Lead.objects.count(),
        'leads_today': Lead.objects.filter(created_at__date=today).count(),
        'active_plans': InternetPlan.objects.filter(is_active=True).count(),
        'active_banners': Banner.objects.filter(is_active=True).count(),
        'recent_leads': Lead.objects.all()[:5],
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
        'content_counts': content_counts,
    })


# ─── Config ───────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def config_view(request):
    obj = SiteConfig.load()
    if request.method == 'POST':
        form = SiteConfigForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas!')
            return redirect('dashboard:config')
    else:
        form = SiteConfigForm(instance=obj)
    return render(request, 'dashboard/config.html', {
        'form': form, 'nav_active': 'config',
    })


# ─── Leads ────────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def leads_list(request):
    qs = Lead.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(nome__icontains=q)

    objects = []
    for obj in qs[:100]:
        objects.append({
            'display_values': [obj.nome, obj.email or '-', obj.celular or '-',
                               obj.get_source_display(), obj.created_at.strftime('%d/%m/%Y %H:%M')],
            'edit_url': '#',
            'delete_url': '#',
            'display_name': obj.nome,
        })

    return render(request, 'dashboard/generic_list.html', {
        'nav_active': 'leads', 'sidebar_active': '',
        'page_title': 'Leads',
        'page_subtitle': f'{Lead.objects.count()} leads capturados',
        'table_headers': ['Nome', 'Email', 'Celular', 'Origem', 'Data'],
        'objects': objects,
        'add_url': None,
    })


# ─── Generic CRUD Helper ─────────────────────────────────────────────────────

def _crud_list(request, model, form_class, title, sidebar, headers, display_fn,
               list_url_name, add_url_name, edit_url_name, delete_url_name,
               add_label='Adicionar'):
    objects = []
    for obj in model.objects.all():
        objects.append({
            'display_values': display_fn(obj),
            'edit_url': f'/painel/{edit_url_name}/{obj.pk}',
            'delete_url': f'/painel/{delete_url_name}/{obj.pk}/excluir',
            'display_name': str(obj),
        })
    return render(request, 'dashboard/generic_list.html', {
        'sidebar_active': sidebar,
        'page_title': title,
        'table_headers': headers,
        'objects': objects,
        'add_url': f'/painel/{add_url_name}/novo',
        'add_label': add_label,
    })


def _crud_form(request, model, form_class, pk, title_new, title_edit, sidebar,
               back_url, redirect_url):
    instance = get_object_or_404(model, pk=pk) if pk else None
    title = title_edit if instance else title_new

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, f'{"Atualizado" if instance else "Criado"} com sucesso!')
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)

    return render(request, 'dashboard/generic_form.html', {
        'form': form, 'sidebar_active': sidebar,
        'page_title': title, 'back_url': back_url,
    })


def _crud_delete(request, model, pk, redirect_url):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Excluído com sucesso!')
    return redirect(redirect_url)


# ─── Banners ─────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def banners_list(request):
    return _crud_list(request, Banner, BannerForm, 'Banners', 'banners',
                      ['Título', 'Página', 'Ativo', 'Ordem'],
                      lambda o: [o.title, o.get_page_display(), '✓' if o.is_active else '✗', o.order],
                      'banners', 'banners', 'banners', 'banners')

@login_required(login_url='/painel/login')
def banners_form(request, pk=None):
    return _crud_form(request, Banner, BannerForm, pk, 'Novo Banner', 'Editar Banner',
                      'banners', '/painel/banners', 'dashboard:banners_list')

@login_required(login_url='/painel/login')
def banners_delete(request, pk):
    return _crud_delete(request, Banner, pk, 'dashboard:banners_list')


# ─── Planos ──────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def plans_list(request):
    return _crud_list(request, InternetPlan, InternetPlanForm, 'Planos de Internet', 'plans',
                      ['Velocidade', 'Preço', 'Badge', 'Ativo'],
                      lambda o: [f'{o.speed_value} {o.speed_unit}', f'R$ {o.current_price}',
                                 o.badge_text or '-', '✓' if o.is_active else '✗'],
                      'planos', 'planos', 'planos', 'planos')

@login_required(login_url='/painel/login')
def plans_form(request, pk=None):
    return _crud_form(request, InternetPlan, InternetPlanForm, pk, 'Novo Plano', 'Editar Plano',
                      'plans', '/painel/planos', 'dashboard:plans_list')

@login_required(login_url='/painel/login')
def plans_delete(request, pk):
    return _crud_delete(request, InternetPlan, pk, 'dashboard:plans_list')


# ─── Combos ──────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def combos_list(request):
    return _crud_list(request, Combo, ComboForm, 'Combos', 'combos',
                      ['Título', 'Ícone', 'Ordem'],
                      lambda o: [o.title, o.icon_class, o.order],
                      'combos', 'combos', 'combos', 'combos')

@login_required(login_url='/painel/login')
def combos_form(request, pk=None):
    return _crud_form(request, Combo, ComboForm, pk, 'Novo Combo', 'Editar Combo',
                      'combos', '/painel/combos', 'dashboard:combos_list')

@login_required(login_url='/painel/login')
def combos_delete(request, pk):
    return _crud_delete(request, Combo, pk, 'dashboard:combos_list')


# ─── Serviços ────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def services_list(request):
    return _crud_list(request, Service, ServiceForm, 'Serviços', 'services',
                      ['Título', 'Ordem'],
                      lambda o: [o.title, o.order],
                      'servicos', 'servicos', 'servicos', 'servicos')

@login_required(login_url='/painel/login')
def services_form(request, pk=None):
    return _crud_form(request, Service, ServiceForm, pk, 'Novo Serviço', 'Editar Serviço',
                      'services', '/painel/servicos', 'dashboard:services_list')

@login_required(login_url='/painel/login')
def services_delete(request, pk):
    return _crud_delete(request, Service, pk, 'dashboard:services_list')


# ─── Autoatendimento ─────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def selfservice_list(request):
    return _crud_list(request, SelfServiceItem, SelfServiceItemForm, 'Autoatendimento', 'selfservice',
                      ['Título', 'Destaque', 'Ordem'],
                      lambda o: [o.title, '✓' if o.highlight else '✗', o.order],
                      'autoatendimento', 'autoatendimento', 'autoatendimento', 'autoatendimento')

@login_required(login_url='/painel/login')
def selfservice_form(request, pk=None):
    return _crud_form(request, SelfServiceItem, SelfServiceItemForm, pk,
                      'Novo Item', 'Editar Item', 'selfservice',
                      '/painel/autoatendimento', 'dashboard:selfservice_list')

@login_required(login_url='/painel/login')
def selfservice_delete(request, pk):
    return _crud_delete(request, SelfServiceItem, pk, 'dashboard:selfservice_list')


# ─── App Promo ───────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def app_list(request):
    return _crud_list(request, AppPromo, AppPromoForm, 'Promoção do App', 'app',
                      ['Página', 'Nome do App'],
                      lambda o: [o.get_page_display(), o.app_name],
                      'app', 'app', 'app', 'app')

@login_required(login_url='/painel/login')
def app_form(request, pk=None):
    return _crud_form(request, AppPromo, AppPromoForm, pk, 'Nova Promoção', 'Editar Promoção',
                      'app', '/painel/app', 'dashboard:app_list')

@login_required(login_url='/painel/login')
def app_delete(request, pk):
    return _crud_delete(request, AppPromo, pk, 'dashboard:app_list')


# ─── Menus ───────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def menus_list(request):
    return _crud_list(request, MenuItem, MenuItemForm, 'Menus', 'menus',
                      ['Título', 'Link', 'Localização', 'Ordem'],
                      lambda o: [o.title, o.link, o.get_menu_location_display(), o.order],
                      'menus', 'menus', 'menus', 'menus')

@login_required(login_url='/painel/login')
def menus_form(request, pk=None):
    return _crud_form(request, MenuItem, MenuItemForm, pk, 'Novo Menu', 'Editar Menu',
                      'menus', '/painel/menus', 'dashboard:menus_list')

@login_required(login_url='/painel/login')
def menus_delete(request, pk):
    return _crud_delete(request, MenuItem, pk, 'dashboard:menus_list')


# ─── Footer ──────────────────────────────────────────────────────────────────

@login_required(login_url='/painel/login')
def footer_list(request):
    return _crud_list(request, FooterColumn, FooterColumnForm, 'Colunas do Rodapé', 'footer',
                      ['Título', 'Ordem'],
                      lambda o: [o.title, o.order],
                      'rodape', 'rodape', 'rodape', 'rodape')

@login_required(login_url='/painel/login')
def footer_form(request, pk=None):
    return _crud_form(request, FooterColumn, FooterColumnForm, pk, 'Nova Coluna', 'Editar Coluna',
                      'footer', '/painel/rodape', 'dashboard:footer_list')

@login_required(login_url='/painel/login')
def footer_delete(request, pk):
    return _crud_delete(request, FooterColumn, pk, 'dashboard:footer_list')


# ─── Energia (Singleton pages) ───────────────────────────────────────────────

@login_required(login_url='/painel/login')
def energia_view(request):
    hero = EnergyHero.load()
    savings = EnergySavings.load()
    mega = MegaEnergiaHome.load()

    if request.method == 'POST':
        section = request.POST.get('section')
        if section == 'hero':
            form = EnergyHeroForm(request.POST, request.FILES, instance=hero)
        elif section == 'savings':
            form = EnergySavingsForm(request.POST, instance=savings)
        elif section == 'mega':
            form = MegaEnergiaHomeForm(request.POST, instance=mega)
        else:
            form = None
        if form and form.is_valid():
            form.save()
            messages.success(request, 'Seção atualizada!')
            return redirect('dashboard:energia')

    return render(request, 'dashboard/energia.html', {
        'sidebar_active': 'energia',
        'hero_form': EnergyHeroForm(instance=hero),
        'savings_form': EnergySavingsForm(instance=savings),
        'mega_form': MegaEnergiaHomeForm(instance=mega),
        'features': EnergyFeature.objects.all(),
        'steps': EnergyStep.objects.all(),
    })


# ─── Rastreamento (Singleton pages) ──────────────────────────────────────────

@login_required(login_url='/painel/login')
def rastreamento_view(request):
    hero = TrackingHero.load()
    cta = TrackingCTA.load()

    if request.method == 'POST':
        section = request.POST.get('section')
        if section == 'hero':
            form = TrackingHeroForm(request.POST, request.FILES, instance=hero)
        elif section == 'cta':
            form = TrackingCTAForm(request.POST, instance=cta)
        else:
            form = None
        if form and form.is_valid():
            form.save()
            messages.success(request, 'Seção atualizada!')
            return redirect('dashboard:rastreamento')

    return render(request, 'dashboard/rastreamento.html', {
        'sidebar_active': 'rastreamento',
        'hero_form': TrackingHeroForm(instance=hero),
        'cta_form': TrackingCTAForm(instance=cta),
        'features': TrackingFeature.objects.all(),
        'benefits': TrackingBenefit.objects.all(),
    })
