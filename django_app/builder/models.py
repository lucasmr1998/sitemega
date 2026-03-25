from django.db import models
from django.utils.text import slugify


class ComponentType(models.Model):
    """Tipo de componente reutilizável (hero, pricing, features, etc)."""
    name = models.CharField('Nome', max_length=100, unique=True)
    slug = models.SlugField('Slug', max_length=100, unique=True)
    icon = models.CharField('Ícone', max_length=100, default='fa-solid fa-cube',
                            help_text='Classe FontAwesome')
    description = models.CharField('Descrição', max_length=300, blank=True)
    template_name = models.CharField('Template', max_length=200,
                                     help_text='Ex: components/hero.html')
    # Schema define quais campos o JSON deve ter
    schema = models.JSONField('Schema dos campos', default=list,
                              help_text='Lista de campos: [{"name": "title", "type": "text", "label": "Título", "required": true}, ...]')
    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Componente'
        verbose_name_plural = 'Tipos de Componente'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Page(models.Model):
    """Página dinâmica do site."""
    STATUS_CHOICES = [
        ('draft', 'Rascunho'),
        ('published', 'Publicada'),
    ]

    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True,
                            help_text='Ex: black-friday, planos-empresariais')
    meta_description = models.CharField('Meta descrição', max_length=300, blank=True)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='draft')
    is_homepage = models.BooleanField('É a página inicial?', default=False,
                                      help_text='Apenas uma página pode ser a inicial')
    show_header = models.BooleanField('Mostrar header', default=True)
    show_footer = models.BooleanField('Mostrar footer', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['is_homepage', 'status']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.is_homepage:
            return '/'
        return f'/p/{self.slug}'

    def get_sections(self):
        return self.sections.filter(is_active=True).select_related('component_type')

    def save(self, *args, **kwargs):
        if self.is_homepage:
            Page.objects.filter(is_homepage=True).exclude(pk=self.pk).update(is_homepage=False)
        super().save(*args, **kwargs)


class PageComponent(models.Model):
    """Instância de um componente em uma página (com conteúdo)."""
    page = models.ForeignKey(Page, related_name='sections', on_delete=models.CASCADE,
                             verbose_name='Página')
    component_type = models.ForeignKey(ComponentType, on_delete=models.PROTECT,
                                       verbose_name='Tipo de componente')
    data = models.JSONField('Conteúdo', default=dict,
                            help_text='Dados do componente (segue o schema do tipo)')
    order = models.PositiveIntegerField('Ordem', default=0)
    is_active = models.BooleanField('Ativo', default=True)
    css_classes = models.CharField('Classes CSS extras', max_length=500, blank=True,
                                   help_text='Tailwind classes adicionais para este bloco')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Componente da Página'
        verbose_name_plural = 'Componentes da Página'
        indexes = [
            models.Index(fields=['page', 'order']),
        ]

    def __str__(self):
        return f'{self.page.title} > {self.component_type.name} (#{self.order})'

    @property
    def template(self):
        return self.component_type.template_name
