import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import MediaFile

LOGIN_URL = '/painel/login'

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
ALLOWED_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp',  # images
    '.pdf', '.doc', '.docx', '.xls', '.xlsx',                   # docs
    '.mp4', '.webm', '.mov',                                     # video
}


@login_required(login_url=LOGIN_URL)
def media_list(request):
    q = request.GET.get('q', '').strip()
    file_type = request.GET.get('type', '')
    qs = MediaFile.objects.all()
    if q:
        qs = qs.filter(title__icontains=q)
    if file_type:
        qs = qs.filter(file_type=file_type)

    return render(request, 'dashboard/media/media_list.html', {
        'sidebar_active': 'media',
        'files': qs[:100],
        'query': q,
        'file_type': file_type,
    })


@login_required(login_url=LOGIN_URL)
@require_POST
def media_upload(request):
    uploaded = request.FILES.get('file')
    if not uploaded:
        return JsonResponse({'error': 'Nenhum arquivo enviado'}, status=400)

    # Validate file size
    if uploaded.size > MAX_FILE_SIZE:
        return JsonResponse({'error': f'Arquivo muito grande (máx {MAX_FILE_SIZE // 1024 // 1024}MB)'}, status=400)

    # Validate extension
    ext = os.path.splitext(uploaded.name)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return JsonResponse({'error': f'Tipo de arquivo não permitido: {ext}'}, status=400)

    # Sanitize filename (remove path traversal)
    uploaded.name = os.path.basename(uploaded.name).replace('..', '_')

    media = MediaFile(file=uploaded, uploaded_by=request.user)
    media.save()

    return JsonResponse({
        'status': 'ok',
        'id': media.pk,
        'url': media.url,
        'title': media.title,
        'is_image': media.is_image,
    })


@login_required(login_url=LOGIN_URL)
@require_POST
def media_delete(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    media.file.delete(save=False)
    media.delete()
    messages.success(request, 'Arquivo excluído!')
    return redirect('dashboard:media_list')


@login_required(login_url=LOGIN_URL)
def media_browse(request):
    """Modal-friendly view for selecting media from component editor."""
    q = request.GET.get('q', '').strip()
    qs = MediaFile.objects.filter(file_type='image')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'dashboard/media/media_browse_modal.html', {
        'files': qs[:60],
        'query': q,
    })
