import string
import random

from django.conf import settings
from django.db import models


def generate_code(length=6):
    """Generate unique code with atomic check via DB constraint."""
    chars = string.ascii_letters + string.digits
    for _ in range(100):  # max retries
        code = ''.join(random.choices(chars, k=length))
        if not ShortLink.objects.filter(code=code).exists():
            return code
    raise RuntimeError('Could not generate unique code after 100 attempts')


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
        # Retry with new code on duplicate (race condition safety)
        from django.db import IntegrityError
        for attempt in range(5):
            try:
                super().save(*args, **kwargs)
                return
            except IntegrityError:
                if attempt < 4 and not kwargs.get('force_update'):
                    self.code = generate_code()
                else:
                    raise

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
