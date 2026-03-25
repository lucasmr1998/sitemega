import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from django.db import models

from builder.models import Page, ComponentType, PageComponent


LOGIN_URL = '/painel/login'


# ─── Pages List ───────────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'dashboard/builder/pages_list.html', {
        'sidebar_active': 'pages',
        'pages': pages,
    })


# ─── Page Form (create/edit) ─────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def page_form(request, pk=None):
    instance = get_object_or_404(Page, pk=pk) if pk else None

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        slug = request.POST.get('slug', '').strip()
        meta = request.POST.get('meta_description', '').strip()
        status = request.POST.get('status', 'draft')
        is_homepage = request.POST.get('is_homepage') == 'on'
        show_header = request.POST.get('show_header') == 'on'
        show_footer = request.POST.get('show_footer') == 'on'

        if not title or not slug:
            messages.error(request, 'Título e URL são obrigatórios.')
        else:
            if instance:
                instance.title = title
                instance.slug = slug
                instance.meta_description = meta
                instance.status = status
                instance.is_homepage = is_homepage
                instance.show_header = show_header
                instance.show_footer = show_footer
                instance.save()
                messages.success(request, 'Página atualizada!')
            else:
                instance = Page.objects.create(
                    title=title, slug=slug, meta_description=meta,
                    status=status, is_homepage=is_homepage,
                    show_header=show_header, show_footer=show_footer,
                )
                messages.success(request, 'Página criada!')
            return redirect('dashboard:page_editor', pk=instance.pk)

    return render(request, 'dashboard/builder/page_form.html', {
        'sidebar_active': 'pages',
        'page_obj': instance,
    })


# ─── Page Delete ──────────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    page.delete()
    messages.success(request, 'Página excluída!')
    return redirect('dashboard:pages_list')


# ─── Page Editor (visual builder) ────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def page_editor(request, pk):
    page = get_object_or_404(Page, pk=pk)
    sections = page.sections.select_related('component_type').order_by('order')
    component_types = ComponentType.objects.filter(is_active=True)

    return render(request, 'dashboard/builder/page_editor.html', {
        'sidebar_active': 'pages',
        'page_obj': page,
        'sections': sections,
        'component_types': component_types,
    })


# ─── Add Component to Page ───────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def component_add(request, pk):
    page = get_object_or_404(Page, pk=pk)
    type_id = request.POST.get('component_type')
    comp_type = get_object_or_404(ComponentType, pk=type_id)

    # Build default data from schema
    default_data = {}
    for field in comp_type.schema:
        if field['type'] == 'repeater':
            default_data[field['name']] = []
        elif field['type'] == 'list':
            default_data[field['name']] = []
        elif field['type'] == 'checkbox':
            default_data[field['name']] = False
        else:
            default_data[field['name']] = field.get('default', '')

    max_order = page.sections.count()
    PageComponent.objects.create(
        page=page, component_type=comp_type,
        data=default_data, order=max_order,
    )
    messages.success(request, f'Componente "{comp_type.name}" adicionado!')
    return redirect('dashboard:page_editor', pk=page.pk)


# ─── Edit Component ──────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def component_edit(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    schema = comp.component_type.schema

    if request.method == 'POST':
        data = _parse_component_data(request.POST, request.FILES, schema, comp.data)
        comp.data = data
        comp.is_active = request.POST.get('is_active') == 'on'
        comp.css_classes = request.POST.get('css_classes', '')
        comp.save()
        messages.success(request, 'Componente atualizado!')
        return redirect('dashboard:page_editor', pk=comp.page.pk)

    return render(request, 'dashboard/builder/component_edit.html', {
        'sidebar_active': 'pages',
        'comp': comp,
        'schema': schema,
        'page_obj': comp.page,
    })


# ─── Delete Component ────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def component_delete(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    page_pk = comp.page.pk
    comp.delete()
    messages.success(request, 'Componente removido!')
    return redirect('dashboard:page_editor', pk=page_pk)


# ─── Reorder Components ──────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def component_reorder(request, pk):
    page = get_object_or_404(Page, pk=pk)
    try:
        order_data = json.loads(request.body)
        for item in order_data:
            PageComponent.objects.filter(pk=item['id'], page=page).update(order=item['order'])
        return JsonResponse({'status': 'ok'})
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({'error': 'Invalid data'}, status=400)


# ─── Page Preview (iframe-friendly) ──────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def page_preview(request, pk):
    page = get_object_or_404(Page, pk=pk)
    sections = page.sections.filter(is_active=True).select_related('component_type')
    return render(request, 'builder/page_preview.html', {
        'page': page,
        'sections': sections,
    })


# ─── Autosave Component ─────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def component_autosave(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    schema = comp.component_type.schema
    data = _parse_component_data(request.POST, request.FILES, schema, comp.data)
    comp.data = data
    comp.is_active = request.POST.get('is_active') == 'on'
    comp.css_classes = request.POST.get('css_classes', '')
    comp.save(update_fields=['data', 'is_active', 'css_classes', 'updated_at'])
    return JsonResponse({'status': 'ok'})


# ─── Duplicate Component ────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def component_duplicate(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    new_order = comp.order + 1
    # Shift subsequent components
    PageComponent.objects.filter(page=comp.page, order__gte=new_order).update(
        order=models.F('order') + 1
    )
    PageComponent.objects.create(
        page=comp.page,
        component_type=comp.component_type,
        data=comp.data,
        order=new_order,
        is_active=comp.is_active,
        css_classes=comp.css_classes,
    )
    messages.success(request, 'Componente duplicado!')
    return redirect('dashboard:page_editor', pk=comp.page.pk)


# ─── Duplicate Page ─────────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
@require_POST
def page_duplicate(request, pk):
    page = get_object_or_404(Page, pk=pk)
    new_page = Page.objects.create(
        title=f'{page.title} (cópia)',
        slug=f'{page.slug}-copia-{Page.objects.count()}',
        meta_description=page.meta_description,
        status='draft',
        is_homepage=False,
        show_header=page.show_header,
        show_footer=page.show_footer,
    )
    for section in page.sections.all():
        PageComponent.objects.create(
            page=new_page,
            component_type=section.component_type,
            data=section.data,
            order=section.order,
            is_active=section.is_active,
            css_classes=section.css_classes,
        )
    messages.success(request, f'Página duplicada como "{new_page.title}"!')
    return redirect('dashboard:page_editor', pk=new_page.pk)


# ─── Components Library ──────────────────────────────────────────────────────

@login_required(login_url=LOGIN_URL)
def components_list(request):
    types = ComponentType.objects.all()
    return render(request, 'dashboard/builder/components_list.html', {
        'sidebar_active': 'components',
        'types': types,
    })


# ─── Helper: Parse form data from schema ─────────────────────────────────────

def _save_upload(uploaded_file):
    """Save an uploaded file and return its URL."""
    path = default_storage.save(f'components/{uploaded_file.name}', uploaded_file)
    return default_storage.url(path)


def _parse_component_data(post_data, files, schema, existing_data=None):
    """Parse POST data into JSON structure based on component schema."""
    existing_data = existing_data or {}
    data = {}
    for field in schema:
        name = field['name']
        ftype = field['type']

        if ftype == 'checkbox':
            data[name] = post_data.get(name) == 'on'
        elif ftype == 'image':
            uploaded = files.get(name)
            if uploaded:
                data[name] = _save_upload(uploaded)
            else:
                data[name] = post_data.get(f'{name}_current', '') or existing_data.get(name, '')
        elif ftype == 'list':
            raw = post_data.get(name, '')
            data[name] = [line.strip() for line in raw.split('\n') if line.strip()]
        elif ftype == 'number':
            try:
                data[name] = int(post_data.get(name, 0))
            except (ValueError, TypeError):
                data[name] = 0
        elif ftype == 'repeater':
            sub_fields = field.get('fields', [])
            existing_items = existing_data.get(name, [])
            items = []
            idx = 0
            while True:
                prefix = f'{name}__{idx}__'
                has_any = any(k.startswith(prefix) for k in post_data) or any(k.startswith(prefix) for k in files)
                if not has_any:
                    break
                existing_item = existing_items[idx] if idx < len(existing_items) else {}
                item = {}
                for sf in sub_fields:
                    sf_name = sf['name']
                    key = f'{prefix}{sf_name}'
                    if sf['type'] == 'checkbox':
                        item[sf_name] = post_data.get(key) == 'on'
                    elif sf['type'] == 'list':
                        raw = post_data.get(key, '')
                        item[sf_name] = [ln.strip() for ln in raw.split('\n') if ln.strip()]
                    elif sf['type'] == 'image':
                        uploaded = files.get(key)
                        if uploaded:
                            item[sf_name] = _save_upload(uploaded)
                        else:
                            item[sf_name] = post_data.get(f'{key}_current', '') or existing_item.get(sf_name, '')
                    else:
                        item[sf_name] = post_data.get(key, '')
                items.append(item)
                idx += 1
            data[name] = items
        else:
            data[name] = post_data.get(name, '')

    return data
