import string
import random

from django.conf import settings
from django.db import models


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if not ShortLink.objects.filter(code=code).exists():
            return code


class ShortLink(models.Model):
    code = models.CharField('Código', max_length=20, unique=True, db_index=True)
    destination_url = models.URLField('URL de destino', max_length=2000)
    title = models.CharField('Título', max_length=200, blank=True,
                              help_text='Nome interno para identificar o link')
    is_active = models.BooleanField('Ativo', default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                    null=True, blank=True, verbose_name='Criado por')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Link Curto'
        verbose_name_plural = 'Links Curtos'

    def __str__(self):
        return f'/{self.code} → {self.title or self.destination_url[:50]}'

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_code()
        if not self.title:
            self.title = self.destination_url[:100]
        super().save(*args, **kwargs)

    @property
    def short_url(self):
        return f'/{self.code}'

    @property
    def total_clicks(self):
        return self.clicks.count()


class ShortLinkClick(models.Model):
    link = models.ForeignKey(ShortLink, related_name='clicks', on_delete=models.CASCADE)
    clicked_at = models.DateTimeField('Clicado em', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IP', blank=True, null=True)
    user_agent = models.CharField('User Agent', max_length=500, blank=True)
    referer = models.URLField('Referer', max_length=2000, blank=True)

    class Meta:
        ordering = ['-clicked_at']
        verbose_name = 'Clique'
        verbose_name_plural = 'Cliques'
        indexes = [
            models.Index(fields=['link', 'clicked_at']),
        ]

    def __str__(self):
        return f'{self.link.code} — {self.clicked_at}'
