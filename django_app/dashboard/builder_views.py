import json

from django.contrib import messages
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.clickjacking import xframe_options_exempt

from django.db import models
from django.utils.text import slugify

from builder.models import Page, ComponentType, PageComponent, PageRevision, PageTemplate, PageView
from .permissions import role_required


# ─── Pages List ───────────────────────────────────────────────────────────────

@role_required('page.view')
def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'dashboard/builder/pages_list.html', {
        'sidebar_active': 'pages',
        'pages': pages,
    })


# ─── Page Form (create/edit) ─────────────────────────────────────────────────

@role_required('page.edit')
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
        # SEO
        meta_title = request.POST.get('meta_title', '').strip()
        canonical_url = request.POST.get('canonical_url', '').strip()
        noindex = request.POST.get('noindex') == 'on'
        # Agendamento
        publish_at = request.POST.get('publish_at', '').strip() or None
        unpublish_at = request.POST.get('unpublish_at', '').strip() or None

        import re
        error = None
        if not title or not slug:
            error = 'Título e URL são obrigatórios.'
        elif not re.match(r'^[a-z0-9][a-z0-9-]*$', slug):
            error = 'URL deve conter apenas letras minúsculas, números e hífens.'
        elif len(meta) > 300:
            error = 'Meta descrição deve ter no máximo 300 caracteres.'
        elif publish_at and unpublish_at and publish_at >= unpublish_at:
            error = 'Data de despublicação deve ser posterior à de publicação.'
        elif status not in ('draft', 'published', 'scheduled'):
            error = 'Status inválido.'

        if error:
            messages.error(request, error)
        else:
            fields = dict(
                title=title, slug=slug, meta_description=meta,
                status=status, is_homepage=is_homepage,
                show_header=show_header, show_footer=show_footer,
                meta_title=meta_title, canonical_url=canonical_url,
                noindex=noindex, publish_at=publish_at, unpublish_at=unpublish_at,
            )
            if instance:
                for k, v in fields.items():
                    setattr(instance, k, v)
                instance.save()
                messages.success(request, 'Página atualizada!')
            else:
                instance = Page.objects.create(**fields)
                messages.success(request, 'Página criada!')
            return redirect('dashboard:page_editor', pk=instance.pk)

    return render(request, 'dashboard/builder/page_form.html', {
        'sidebar_active': 'pages',
        'page_obj': instance,
    })


# ─── Visual Editor (split-panel, fullscreen, sem sidebar) ────────────────────

@role_required('page.view')
def visual_editor(request, pk):
    page = get_object_or_404(Page, pk=pk)
    sections = page.sections.select_related('component_type').order_by('order')
    component_types = ComponentType.objects.filter(is_active=True)

    sections_data = []
    for s in sections:
        sections_data.append({
            'id': s.pk,
            'type_name': s.component_type.name,
            'type_icon': s.component_type.icon,
            'type_slug': s.component_type.slug,
            'schema': s.component_type.schema,
            'data': s.data,
            'is_active': s.is_active,
            'css_classes': s.css_classes,
            'order': s.order,
        })

    types_data = [{'id': t.pk, 'name': t.name, 'icon': t.icon, 'description': t.description}
                  for t in component_types]

    return render(request, 'dashboard/builder/visual_editor.html', {
        'page_obj': page,
        'sections_json': sections_data,
        'types_json': types_data,
    })


# ─── Page Delete ──────────────────────────────────────────────────────────────

@role_required('page.delete')
@require_POST
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    page.delete()
    messages.success(request, 'Página excluída!')
    return redirect('dashboard:pages_list')


# ─── Page Editor (visual builder) ────────────────────────────────────────────

@role_required('page.view')
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

@role_required('page.create')
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
    comp = PageComponent.objects.create(
        page=page, component_type=comp_type,
        data=default_data, order=max_order,
    )

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'ok', 'id': comp.pk,
            'type_name': comp_type.name, 'type_icon': comp_type.icon,
            'type_slug': comp_type.slug, 'schema': comp_type.schema,
            'data': default_data, 'order': max_order,
            'is_active': True, 'css_classes': '',
        })

    messages.success(request, f'Componente "{comp_type.name}" adicionado!')
    return redirect('dashboard:page_editor', pk=page.pk)


# ─── Edit Component ──────────────────────────────────────────────────────────

@role_required('page.edit')
def component_edit(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    schema = comp.component_type.schema

    if request.method == 'POST':
        # Create revision before saving
        PageRevision.create_from_page(comp.page, user=request.user, comment=f'Editou {comp.component_type.name}')
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

@role_required('component.delete')
@require_POST
def component_delete(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    page_pk = comp.page.pk
    comp.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok'})

    messages.success(request, 'Componente removido!')
    return redirect('dashboard:page_editor', pk=page_pk)


# ─── Reorder Components ──────────────────────────────────────────────────────

@role_required('page.edit')
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

@xframe_options_exempt
@role_required('page.view')
def page_preview(request, pk):
    page = get_object_or_404(Page, pk=pk)
    sections = page.sections.filter(is_active=True).select_related('component_type')
    return render(request, 'builder/page_preview.html', {
        'page': page,
        'sections': sections,
    })


# ─── Autosave Component ─────────────────────────────────────────────────────

@role_required('page.edit')
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

@role_required('page.create')
@require_POST
def component_duplicate(request, pk):
    comp = get_object_or_404(PageComponent, pk=pk)
    new_order = comp.order + 1
    # Shift subsequent components
    PageComponent.objects.filter(page=comp.page, order__gte=new_order).update(
        order=models.F('order') + 1
    )
    new_comp = PageComponent.objects.create(
        page=comp.page,
        component_type=comp.component_type,
        data=comp.data,
        order=new_order,
        is_active=comp.is_active,
        css_classes=comp.css_classes,
    )
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'ok',
            'id': new_comp.pk,
            'type_name': new_comp.component_type.name,
            'type_icon': new_comp.component_type.icon,
            'type_slug': new_comp.component_type.slug,
            'schema': new_comp.component_type.schema,
            'data': new_comp.data,
            'is_active': new_comp.is_active,
            'css_classes': new_comp.css_classes,
            'order': new_comp.order,
        })
    messages.success(request, 'Componente duplicado!')
    return redirect('dashboard:page_editor', pk=comp.page.pk)


# ─── Duplicate Page ─────────────────────────────────────────────────────────

@role_required('page.create')
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


# ─── Revisions ──────────────────────────────────────────────────────────────

@role_required('revision.view')
def revision_list(request, pk):
    page = get_object_or_404(Page, pk=pk)
    revisions = page.revisions.select_related('created_by')[:50]
    return render(request, 'dashboard/builder/revisions_list.html', {
        'sidebar_active': 'pages',
        'page_obj': page,
        'revisions': revisions,
    })


@role_required('page.edit')
@require_POST
def revision_create(request, pk):
    """Cria uma revisão manual (chamado pelo visual editor via AJAX)."""
    page = get_object_or_404(Page, pk=pk)
    comment = request.POST.get('comment', 'Salvo pelo editor visual')
    rev = PageRevision.create_from_page(page, user=request.user, comment=comment)
    return JsonResponse({'status': 'ok', 'revision_number': rev.revision_number})


@role_required('revision.restore')
@require_POST
def revision_restore(request, pk, rev_pk):
    page = get_object_or_404(Page, pk=pk)
    revision = get_object_or_404(PageRevision, pk=rev_pk, page=page)
    # Save current state as new revision before restoring
    PageRevision.create_from_page(page, user=request.user, comment=f'Antes de restaurar rev #{revision.revision_number}')
    revision.restore()
    messages.success(request, f'Página restaurada para revisão #{revision.revision_number}!')
    return redirect('dashboard:page_editor', pk=page.pk)


# ─── Page Templates ─────────────────────────────────────────────────────────

@role_required('page.view')
def templates_list(request):
    templates = PageTemplate.objects.filter(is_active=True)
    return render(request, 'dashboard/builder/templates_list.html', {
        'sidebar_active': 'templates',
        'templates': templates,
    })


@role_required('page.create')
@require_POST
def template_save(request, pk):
    """Salva a página atual como template reutilizável."""
    page = get_object_or_404(Page, pk=pk)
    name = request.POST.get('template_name', '').strip() or f'Template de {page.title}'
    tpl = PageTemplate.create_from_page(page, name=name)
    messages.success(request, f'Template "{tpl.name}" salvo!')
    return redirect('dashboard:page_editor', pk=page.pk)


@role_required('page.create')
@require_POST
def template_apply(request, pk):
    """Aplica um template a uma nova página."""
    tpl = get_object_or_404(PageTemplate, pk=pk)
    slug_base = slugify(tpl.name) or 'pagina'
    new_page = Page.objects.create(
        title=f'{tpl.name}',
        slug=f'{slug_base}-{Page.objects.count() + 1}',
        status='draft',
        **tpl.page_defaults,
    )
    tpl.apply_to_page(new_page)
    messages.success(request, f'Página criada a partir do template "{tpl.name}"!')
    return redirect('dashboard:page_editor', pk=new_page.pk)


@role_required('page.delete')
@require_POST
def template_delete(request, pk):
    tpl = get_object_or_404(PageTemplate, pk=pk)
    tpl.delete()
    messages.success(request, 'Template excluído!')
    return redirect('dashboard:templates_list')


# ─── Import / Export ────────────────────────────────────────────────────────

@role_required('page.view')
def page_export(request, pk):
    """Exporta página como JSON para download."""
    page = get_object_or_404(Page, pk=pk)
    components = []
    for comp in page.sections.all():
        components.append({
            'component_type_slug': comp.component_type.slug,
            'data': comp.data,
            'order': comp.order,
            'is_active': comp.is_active,
            'css_classes': comp.css_classes,
        })
    export = {
        'title': page.title,
        'slug': page.slug,
        'meta_title': page.meta_title,
        'meta_description': page.meta_description,
        'show_header': page.show_header,
        'show_footer': page.show_footer,
        'components': components,
    }
    response = JsonResponse(export, json_dumps_params={'indent': 2, 'ensure_ascii': False})
    response['Content-Disposition'] = f'attachment; filename="{page.slug}.json"'
    return response


@role_required('page.create')
@require_POST
def page_import(request):
    """Importa página de um arquivo JSON."""
    uploaded = request.FILES.get('file')
    if not uploaded:
        messages.error(request, 'Nenhum arquivo enviado.')
        return redirect('dashboard:pages_list')

    try:
        data = json.loads(uploaded.read().decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        messages.error(request, 'Arquivo JSON inválido.')
        return redirect('dashboard:pages_list')

    # Avoid slug collision
    base_slug = data.get('slug', 'importada')
    slug = base_slug
    counter = 1
    while Page.objects.filter(slug=slug).exists():
        slug = f'{base_slug}-{counter}'
        counter += 1

    page = Page.objects.create(
        title=data.get('title', 'Página Importada'),
        slug=slug,
        meta_title=data.get('meta_title', ''),
        meta_description=data.get('meta_description', ''),
        show_header=data.get('show_header', True),
        show_footer=data.get('show_footer', True),
        status='draft',
    )

    for item in data.get('components', []):
        ct_slug = item.get('component_type_slug', '')
        ct = ComponentType.objects.filter(slug=ct_slug).first()
        if ct:
            PageComponent.objects.create(
                page=page,
                component_type=ct,
                data=item.get('data', {}),
                order=item.get('order', 0),
                is_active=item.get('is_active', True),
                css_classes=item.get('css_classes', ''),
            )

    messages.success(request, f'Página "{page.title}" importada como rascunho!')
    return redirect('dashboard:page_editor', pk=page.pk)


# ─── Analytics ──────────────────────────────────────────────────────────────

@role_required('page.view')
def analytics_view(request):
    from datetime import timedelta
    from django.utils import timezone
    from django.db.models import Sum

    today = timezone.localdate()
    thirty_days_ago = today - timedelta(days=29)

    # Total views last 30 days
    total_views = PageView.objects.filter(date__gte=thirty_days_ago).aggregate(
        total=Sum('count'))['total'] or 0

    # Daily chart (30 days)
    labels, data = [], []
    for i in range(30):
        day = thirty_days_ago + timedelta(days=i)
        labels.append(day.strftime('%d/%m'))
        count = PageView.objects.filter(date=day).aggregate(total=Sum('count'))['total'] or 0
        data.append(count)

    # Top pages
    top_pages = (
        PageView.objects.filter(date__gte=thirty_days_ago)
        .values('page__title', 'page__slug')
        .annotate(total=Sum('count'))
        .order_by('-total')[:10]
    )

    return render(request, 'dashboard/builder/analytics.html', {
        'sidebar_active': 'analytics',
        'total_views': total_views,
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
        'top_pages': top_pages,
    })


# ─── Components Library ──────────────────────────────────────────────────────

@role_required('page.view')
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
