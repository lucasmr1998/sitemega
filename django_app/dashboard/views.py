import json
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from builder.models import Page, PageComponent
from core.models import SiteConfig, MenuItem, FooterColumn
from leads.models import Lead

from .forms import SiteConfigForm, MenuItemForm, FooterColumnForm


LOGIN_URL = '/painel/login'


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

@login_required(login_url=LOGIN_URL)
def index(request):
    today = timezone.localdate()
    seven_days_ago = today - timedelta(days=6)

    labels, data = [], []
    for i in range(7):
        day = seven_days_ago + timedelta(days=i)
        labels.append(day.strftime('%d/%m'))
        data.append(Lead.objects.filter(created_at__date=day).count())

    content_counts = [
        {'label': 'Páginas', 'count': Page.objects.count(), 'icon': 'fa-solid fa-file-lines', 'url': '/painel/paginas'},
        {'label': 'Componentes', 'count': PageComponent.objects.count(), 'icon': 'fa-solid fa-puzzle-piece', 'url': '/painel/componentes'},
        {'label': 'Leads', 'count': Lead.objects.count(), 'icon': 'fa-solid fa-users', 'url': '/painel/leads'},
    ]

    return render(request, 'dashboard/index.html', {
        'nav_active': 'dashboard',
        'total_leads': Lead.objects.count(),
        'leads_today': Lead.objects.filter(created_at__date=today).count(),
        'active_pages': Page.objects.filter(status='published').count(),
        'total_components': PageComponent.objects.filter(is_active=True).count(),
        'recent_leads': Lead.objects.all()[:5],
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
        'content_counts': content_counts,
    })


# ─── Config ───────────────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
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

@login_required(login_url=LOGIN_URL)
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


# ─── Menus ───────────────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def menus_list(request):
    return _crud_list(request, MenuItem, MenuItemForm, 'Menus', 'menus',
                      ['Título', 'Link', 'Localização', 'Ordem'],
                      lambda o: [o.title, o.link, o.get_menu_location_display(), o.order],
                      'menus', 'menus', 'menus', 'menus')

@login_required(login_url=LOGIN_URL)
def menus_form(request, pk=None):
    return _crud_form(request, MenuItem, MenuItemForm, pk, 'Novo Menu', 'Editar Menu',
                      'menus', '/painel/menus', 'dashboard:menus_list')

@login_required(login_url=LOGIN_URL)
def menus_delete(request, pk):
    return _crud_delete(request, MenuItem, pk, 'dashboard:menus_list')


# ─── Footer ──────────────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def footer_list(request):
    return _crud_list(request, FooterColumn, FooterColumnForm, 'Colunas do Rodapé', 'footer',
                      ['Título', 'Ordem'],
                      lambda o: [o.title, o.order],
                      'rodape', 'rodape', 'rodape', 'rodape')

@login_required(login_url=LOGIN_URL)
def footer_form(request, pk=None):
    return _crud_form(request, FooterColumn, FooterColumnForm, pk, 'Nova Coluna', 'Editar Coluna',
                      'footer', '/painel/rodape', 'dashboard:footer_list')

@login_required(login_url=LOGIN_URL)
def footer_delete(request, pk):
    return _crud_delete(request, FooterColumn, pk, 'dashboard:footer_list')
