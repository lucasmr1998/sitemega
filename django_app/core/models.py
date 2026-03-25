from django.core.cache import cache
from django.db import models
from colorfield.fields import ColorField


class SiteConfig(models.Model):
    """Singleton — configurações globais do site."""
    company_name = models.CharField('Nome da empresa', max_length=100, default='MegaLink')
    logo = models.ImageField('Logo', upload_to='config/', blank=True)
    logo_alt_text = models.CharField('Alt do logo', max_length=100, default='MegaLink Provedor')
    favicon = models.ImageField('Favicon', upload_to='config/', blank=True)

    # Cores
    primary_color = ColorField('Cor primária', default='#2323FA')
    primary_dark_color = ColorField('Cor primária escura', default='#040470')
    secondary_color = ColorField('Cor secundária', default='#FF6905')
    accent_color = ColorField('Cor de destaque', default='#10B981')

    # Contato
    whatsapp_number = models.CharField('WhatsApp', max_length=20, default='558922210068')
    phone = models.CharField('Telefone', max_length=30, blank=True)
    email = models.EmailField('E-mail', blank=True)
    address = models.TextField('Endereço', blank=True)

    # Redes sociais
    facebook_url = models.URLField('Facebook', blank=True)
    instagram_url = models.URLField('Instagram', blank=True)
    linkedin_url = models.URLField('LinkedIn', blank=True)
    youtube_url = models.URLField('YouTube', blank=True)

    # Header
    assine_ja_enabled = models.BooleanField('Botão "Assine já" ativo', default=True)
    assine_ja_link = models.CharField('Link "Assine já"', max_length=200, default='#assine')
    area_cliente_enabled = models.BooleanField('Botão "Área do Cliente" ativo', default=True)
    area_cliente_link = models.CharField('Link "Área do Cliente"', max_length=200, default='#area-cliente')

    # Footer
    footer_text = models.CharField('Texto do rodapé', max_length=300, blank=True,
                                   default='A melhor conexão para você e sua empresa.')
    company_address = models.CharField('Endereço empresa', max_length=300, blank=True)
    company_phone = models.CharField('Telefone empresa', max_length=30, blank=True)
    company_email = models.EmailField('E-mail empresa', blank=True)
    footer_copyright = models.CharField('Copyright', max_length=300, blank=True,
                                        default='Copyright 2025 © - MegaLink - Todos os direitos reservados')
    footer_terms_url = models.CharField('URL Termos', max_length=200, blank=True, default='#termos')
    footer_privacy_url = models.CharField('URL Privacidade', max_length=200, blank=True, default='#privacidade')

    class Meta:
        verbose_name = 'Configuração do Site'
        verbose_name_plural = 'Configuração do Site'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        cache.delete('site_config')

    @classmethod
    def load(cls):
        obj = cache.get('site_config')
        if obj is None:
            obj, _ = cls.objects.get_or_create(pk=1)
            cache.set('site_config', obj, 300)
        return obj


class MenuItem(models.Model):
    MENU_LOCATIONS = [
        ('main', 'Menu Principal'),
        ('algar', 'Menu Algar'),
    ]

    title = models.CharField('Título', max_length=100)
    link = models.CharField('Link', max_length=200, default='#')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children',
                               on_delete=models.CASCADE, verbose_name='Item pai')
    menu_location = models.CharField('Localização', max_length=20, choices=MENU_LOCATIONS, default='main')
    is_mega_menu = models.BooleanField('Mega menu', default=False)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Item do Menu'
        verbose_name_plural = 'Itens do Menu'

    def __str__(self):
        return self.title


class MegaMenuColumn(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='columns', on_delete=models.CASCADE,
                                  verbose_name='Item do menu')
    title = models.CharField('Título', max_length=100)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Coluna do Mega Menu'
        verbose_name_plural = 'Colunas do Mega Menu'

    def __str__(self):
        return f'{self.menu_item.title} > {self.title}'


class MegaMenuLink(models.Model):
    column = models.ForeignKey(MegaMenuColumn, related_name='links', on_delete=models.CASCADE,
                               verbose_name='Coluna')
    title = models.CharField('Título', max_length=100)
    link = models.CharField('Link', max_length=200, default='#')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Link do Mega Menu'
        verbose_name_plural = 'Links do Mega Menu'

    def __str__(self):
        return self.title


class FooterColumn(models.Model):
    title = models.CharField('Título', max_length=100)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Coluna do Rodapé'
        verbose_name_plural = 'Colunas do Rodapé'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    column = models.ForeignKey(FooterColumn, related_name='links', on_delete=models.CASCADE,
                               verbose_name='Coluna')
    title = models.CharField('Título', max_length=100)
    url = models.CharField('URL', max_length=300)
    open_new_tab = models.BooleanField('Abrir em nova aba', default=False)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Link do Rodapé'
        verbose_name_plural = 'Links do Rodapé'

    def __str__(self):
        return self.title


# ─── Cache Invalidation Signals ──────────────────────────────────────────────

from django.db.models.signals import post_save, post_delete


def _invalidate_nav_cache(**kwargs):
    cache.delete_many(['main_menus', 'algar_menus', 'footer_columns'])


for _model in (MenuItem, MegaMenuColumn, MegaMenuLink):
    post_save.connect(_invalidate_nav_cache, sender=_model)
    post_delete.connect(_invalidate_nav_cache, sender=_model)

for _model in (FooterColumn, FooterLink):
    post_save.connect(_invalidate_nav_cache, sender=_model)
    post_delete.connect(_invalidate_nav_cache, sender=_model)
