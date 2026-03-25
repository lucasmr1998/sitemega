import os

from django.conf import settings
from django.db import models

try:
    from PIL import Image
except ImportError:
    Image = None


class MediaFile(models.Model):
    FILE_TYPES = [
        ('image', 'Imagem'),
        ('document', 'Documento'),
        ('video', 'Vídeo'),
    ]

    title = models.CharField('Título', max_length=200, blank=True)
    file = models.FileField('Arquivo', upload_to='library/%Y/%m/')
    file_type = models.CharField('Tipo', max_length=20, choices=FILE_TYPES, default='image')
    mime_type = models.CharField('MIME', max_length=100, blank=True)
    file_size = models.PositiveIntegerField('Tamanho (bytes)', default=0)
    width = models.PositiveIntegerField('Largura', null=True, blank=True)
    height = models.PositiveIntegerField('Altura', null=True, blank=True)
    alt_text = models.CharField('Texto alternativo', max_length=300, blank=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Enviado por',
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return self.title or os.path.basename(self.file.name)

    @property
    def url(self):
        return self.file.url if self.file else ''

    @property
    def is_image(self):
        return self.file_type == 'image'

    def save(self, *args, **kwargs):
        if self.file:
            name = os.path.basename(self.file.name)
            if not self.title:
                self.title = os.path.splitext(name)[0]

            ext = os.path.splitext(name)[1].lower()
            if ext in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp'):
                self.file_type = 'image'
            elif ext in ('.mp4', '.webm', '.mov', '.avi'):
                self.file_type = 'video'
            else:
                self.file_type = 'document'

            self.file_size = self.file.size

            if self.file_type == 'image' and Image and ext != '.svg':
                try:
                    img = Image.open(self.file)
                    self.width, self.height = img.size
                    self.file.seek(0)
                except Exception:
                    pass

        super().save(*args, **kwargs)
