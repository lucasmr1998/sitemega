from django.db import models
from colorfield.fields import ColorField


# ─── HOME: Banners ───────────────────────────────────────────────────────────

class Banner(models.Model):
    PAGE_CHOICES = [('home', 'Home'), ('algar', 'Algar')]

    title = models.CharField('Título', max_length=200)
    image = models.ImageField('Imagem', upload_to='banners/')
    link = models.CharField('Link', max_length=300, default='#')
    page = models.CharField('Página', max_length=20, choices=PAGE_CHOICES, default='home')
    is_active = models.BooleanField('Ativo', default=True)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return f'{self.title} ({self.page})'


# ─── HOME: Planos de Internet ────────────────────────────────────────────────

class InternetPlan(models.Model):
    PAGE_CHOICES = [('home', 'Home'), ('algar', 'Algar')]
    SPEED_UNITS = [('MEGA', 'MEGA'), ('GIGA', 'GIGA')]

    page = models.CharField('Página', max_length=20, choices=PAGE_CHOICES, default='home')
    category_label = models.CharField('Categoria', max_length=50, default='INTERNET')
    speed_value = models.CharField('Velocidade', max_length=10)
    speed_unit = models.CharField('Unidade', max_length=10, choices=SPEED_UNITS, default='MEGA')
    current_price = models.CharField('Preço atual', max_length=20, help_text='Ex: 89,90')
    old_price = models.CharField('Preço antigo', max_length=20, blank=True, help_text='Ex: 117,90')
    period = models.CharField('Período', max_length=10, default='/mês')

    # Botão
    button_text = models.CharField('Texto do botão', max_length=50, default='Aproveitar Oferta')
    button_link = models.URLField('Link do botão', max_length=500)

    # Badge
    show_badge = models.BooleanField('Mostrar badge', default=False)
    badge_text = models.CharField('Texto do badge', max_length=50, blank=True)
    badge_bg_color = ColorField('Cor de fundo do badge', default='#2323FA', blank=True)
    badge_text_color = ColorField('Cor do texto do badge', default='#FFFFFF', blank=True)

    # Cores da seção
    title_color = ColorField('Cor do título', default='#2323FA')
    speed_color = ColorField('Cor da velocidade', default='#2323FA')
    underline_color = ColorField('Cor do sublinhado', default='#FF6905')
    button_bg_color = ColorField('Cor do botão', default='#FF6905')
    button_text_color = ColorField('Cor do texto do botão', default='#FFFFFF')

    is_active = models.BooleanField('Ativo', default=True)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Plano de Internet'
        verbose_name_plural = 'Planos de Internet'

    def __str__(self):
        return f'{self.speed_value} {self.speed_unit} ({self.page})'


class PlanFeature(models.Model):
    plan = models.ForeignKey(InternetPlan, related_name='features', on_delete=models.CASCADE,
                             verbose_name='Plano')
    text = models.CharField('Texto', max_length=200)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Feature do Plano'
        verbose_name_plural = 'Features do Plano'

    def __str__(self):
        return self.text


# ─── HOME: Combos ────────────────────────────────────────────────────────────

class Combo(models.Model):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição')
    icon_class = models.CharField('Classe do ícone', max_length=100,
                                  help_text='Ex: fa-wifi, fa-bolt')
    color_class = models.CharField('Classe de cor', max_length=100,
                                   help_text='Ex: bg-[#FF6905]')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Combo'
        verbose_name_plural = 'Combos'

    def __str__(self):
        return self.title


# ─── HOME: Serviços ──────────────────────────────────────────────────────────

class Service(models.Model):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição')
    icon_class = models.CharField('Classe do ícone', max_length=100, blank=True,
                                  help_text='FontAwesome class (opcional, usa SVG por padrão)')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title


# ─── HOME: Autoatendimento ───────────────────────────────────────────────────

class SelfServiceItem(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    icon_class = models.CharField('Classe do ícone', max_length=100,
                                  help_text='Ex: fa-solid fa-file-invoice')
    link = models.CharField('Link', max_length=300, default='#')
    highlight = models.BooleanField('Destacar (azul)', default=False)
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Item de Autoatendimento'
        verbose_name_plural = 'Itens de Autoatendimento'

    def __str__(self):
        return self.title


# ─── HOME: App ────────────────────────────────────────────────────────────────

class AppPromo(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('rastreamento', 'Rastreamento'),
        ('algar', 'Algar'),
    ]

    page = models.CharField('Página', max_length=20, choices=PAGE_CHOICES)
    app_name = models.CharField('Nome do app', max_length=100, default='MegalinkApp')
    card_title = models.CharField('Título do card', max_length=100, default='Megacliente')
    card_description = models.TextField('Descrição do card',
                                        default='O aplicativo oficial da MegaLink para autoatendimento.')
    heading = models.CharField('Título principal', max_length=200, default='MegalinkApp')
    heading_subtitle = models.CharField('Subtítulo', max_length=200, default='Completo. Simples.')
    description = models.TextField('Descrição')
    image = models.ImageField('Imagem', upload_to='app/', blank=True)
    google_play_url = models.URLField('Google Play URL', blank=True)
    app_store_url = models.URLField('App Store URL', blank=True)

    class Meta:
        verbose_name = 'Promoção do App'
        verbose_name_plural = 'Promoções do App'

    def __str__(self):
        return f'App Promo - {self.page}'


# ─── HOME: Mega Energia ──────────────────────────────────────────────────────

class MegaEnergiaHome(models.Model):
    heading = models.TextField('Título', default='Mega Energia sua conta com até')
    heading_highlight = models.CharField('Texto destacado', max_length=200, default='20% de desconto')
    description = models.TextField('Descrição')
    cta_text = models.CharField('Texto do botão', max_length=100, default='Quero economizar')
    cta_link = models.CharField('Link do botão', max_length=200, default='energia')
    card_title = models.CharField('Título do card', max_length=200, default='Simples e Digital')
    card_features = models.JSONField('Itens do card', default=list,
                                     help_text='Lista: ["Sem fidelidade", "Sem obras", ...]')

    class Meta:
        verbose_name = 'Mega Energia (Home)'
        verbose_name_plural = 'Mega Energia (Home)'

    def __str__(self):
        return 'Mega Energia - Home'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ─── ENERGIA: Hero ────────────────────────────────────────────────────────────

class EnergyHero(models.Model):
    heading = models.TextField('Título', default='Economize até 20% na sua conta de energia')
    highlight_text = models.CharField('Texto destacado', max_length=100, default='20%')
    subheading = models.TextField('Subtítulo',
                                  default='Sem taxas, sem custo de adesão e sem instalação de placas solares.')
    badge_1 = models.CharField('Badge 1', max_length=100, blank=True, default='Sem fidelidade')
    badge_2 = models.CharField('Badge 2', max_length=100, blank=True, default='100% Digital')
    form_title = models.CharField('Título do formulário', max_length=200,
                                  default='Informe seus dados para contato')
    form_subtitle = models.CharField('Subtítulo do formulário', max_length=200, blank=True,
                                     default='Fale com um de nossos especialistas.')
    background_image = models.ImageField('Imagem de fundo', upload_to='energy/', blank=True)

    class Meta:
        verbose_name = 'Energia - Hero'
        verbose_name_plural = 'Energia - Hero'

    def __str__(self):
        return 'Energia Hero'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ─── ENERGIA: Economia ───────────────────────────────────────────────────────

class EnergySavings(models.Model):
    section_tag = models.CharField('Tag da seção', max_length=100, default='Inovação Solar')
    heading = models.CharField('Título', max_length=200, default='Mais economia para você')
    content_title = models.CharField('Título do conteúdo', max_length=200, default='Energia por Assinatura')
    content_body = models.TextField('Corpo do conteúdo')
    savings_percentage = models.IntegerField('Percentual de economia', default=20)
    checkmarks = models.JSONField('Checkmarks', default=list,
                                  help_text='Lista: ["Sem taxa de adesão", ...]')
    cta_text = models.CharField('Texto do botão', max_length=100, default='Garantir meu desconto')
    cta_link = models.CharField('Link do botão', max_length=200, default='#')

    class Meta:
        verbose_name = 'Energia - Economia'
        verbose_name_plural = 'Energia - Economia'

    def __str__(self):
        return 'Energia Economia'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ─── ENERGIA: Vantagens ──────────────────────────────────────────────────────

class EnergyFeature(models.Model):
    icon_class = models.CharField('Classe do ícone', max_length=100)
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Energia - Vantagem'
        verbose_name_plural = 'Energia - Vantagens'

    def __str__(self):
        return self.title


# ─── ENERGIA: Passos ─────────────────────────────────────────────────────────

class EnergyStep(models.Model):
    number = models.PositiveIntegerField('Número')
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Energia - Passo'
        verbose_name_plural = 'Energia - Passos'

    def __str__(self):
        return f'{self.number}. {self.title}'


# ─── RASTREAMENTO: Hero ──────────────────────────────────────────────────────

class TrackingHero(models.Model):
    tag_text = models.CharField('Tag', max_length=100, default='Monitoramento 24h')
    heading = models.TextField('Título')
    subheading = models.TextField('Subtítulo')
    cta_text = models.CharField('Texto do botão', max_length=200, blank=True)
    cta_link = models.CharField('Link do botão', max_length=200, default='#contratar')
    form_title = models.CharField('Título do formulário', max_length=200, blank=True)
    form_subtitle = models.CharField('Subtítulo do formulário', max_length=200, blank=True)
    background_image = models.ImageField('Imagem de fundo', upload_to='tracking/', blank=True)

    class Meta:
        verbose_name = 'Rastreamento - Hero'
        verbose_name_plural = 'Rastreamento - Hero'

    def __str__(self):
        return 'Rastreamento Hero'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ─── RASTREAMENTO: Features ──────────────────────────────────────────────────

class TrackingFeature(models.Model):
    icon_class = models.CharField('Classe do ícone', max_length=100)
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Rastreamento - Funcionalidade'
        verbose_name_plural = 'Rastreamento - Funcionalidades'

    def __str__(self):
        return self.title


# ─── RASTREAMENTO: Benefícios ────────────────────────────────────────────────

class TrackingBenefit(models.Model):
    icon_class = models.CharField('Classe do ícone', max_length=100)
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Rastreamento - Benefício'
        verbose_name_plural = 'Rastreamento - Benefícios'

    def __str__(self):
        return self.title


# ─── RASTREAMENTO: CTA ───────────────────────────────────────────────────────

class TrackingCTA(models.Model):
    heading = models.TextField('Título')
    subheading = models.TextField('Subtítulo')
    primary_button_text = models.CharField('Botão primário', max_length=200)
    primary_button_link = models.URLField('Link botão primário')
    secondary_button_text = models.CharField('Botão secundário', max_length=200, blank=True)
    secondary_button_link = models.CharField('Link botão secundário', max_length=200, blank=True)
    footnote = models.CharField('Rodapé', max_length=300, blank=True)

    class Meta:
        verbose_name = 'Rastreamento - CTA'
        verbose_name_plural = 'Rastreamento - CTA'

    def __str__(self):
        return 'Rastreamento CTA'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ─── ALGAR: Blog ─────────────────────────────────────────────────────────────

class BlogPost(models.Model):
    title = models.CharField('Título', max_length=200)
    excerpt = models.TextField('Resumo')
    category_tag = models.CharField('Categoria', max_length=50)
    tag_bg_color = ColorField('Cor do tag', default='#FFD100')
    cover_bg_color = ColorField('Cor de fundo da capa', default='#2323FA')
    cover_icon_class = models.CharField('Ícone da capa', max_length=100, blank=True)
    image = models.ImageField('Imagem', upload_to='blog/', blank=True)
    link = models.CharField('Link', max_length=300, default='#')
    order = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
