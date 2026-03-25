"""
Schemas definem os campos editáveis de cada tipo de componente.
Cada campo tem: name, type, label, required (opcional), help (opcional), options (para select).

Tipos de campo suportados:
- text: input de texto simples
- textarea: textarea multilinha
- richtext: textarea grande (futuro: editor WYSIWYG)
- number: input numérico
- url: input de URL
- image: upload de imagem
- color: seletor de cor
- select: dropdown com opções
- checkbox: boolean
- list: lista de strings (JSON array)
- repeater: lista de objetos (sub-campos repetíveis)
"""

COMPONENT_SCHEMAS = {
    'hero_banner': {
        'name': 'Hero Banner',
        'icon': 'fa-solid fa-panorama',
        'description': 'Banner principal com imagem, título e botão CTA',
        'template': 'components/hero_banner.html',
        'schema': [
            {'name': 'title', 'type': 'text', 'label': 'Título', 'required': True},
            {'name': 'subtitle', 'type': 'textarea', 'label': 'Subtítulo'},
            {'name': 'image', 'type': 'image', 'label': 'Imagem de fundo'},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão'},
            {'name': 'cta_link', 'type': 'url', 'label': 'Link do botão'},
            {'name': 'bg_color', 'type': 'color', 'label': 'Cor de fundo', 'default': '#2323FA'},
        ],
    },

    'banner_carousel': {
        'name': 'Carrossel de Banners',
        'icon': 'fa-solid fa-images',
        'description': 'Slideshow de banners com navegação',
        'template': 'components/banner_carousel.html',
        'schema': [
            {'name': 'banners', 'type': 'repeater', 'label': 'Banners', 'fields': [
                {'name': 'title', 'type': 'text', 'label': 'Título'},
                {'name': 'image', 'type': 'image', 'label': 'Imagem'},
                {'name': 'link', 'type': 'url', 'label': 'Link'},
            ]},
        ],
    },

    'pricing_cards': {
        'name': 'Cards de Preço',
        'icon': 'fa-solid fa-tags',
        'description': 'Cards de planos com preço, features e botão',
        'template': 'components/pricing_cards.html',
        'schema': [
            {'name': 'section_title', 'type': 'text', 'label': 'Título da seção', 'default': 'Internet'},
            {'name': 'speed_color', 'type': 'color', 'label': 'Cor da velocidade', 'default': '#2323FA'},
            {'name': 'underline_color', 'type': 'color', 'label': 'Cor do sublinhado', 'default': '#FF6905'},
            {'name': 'button_color', 'type': 'color', 'label': 'Cor do botão', 'default': '#FF6905'},
            {'name': 'plans', 'type': 'repeater', 'label': 'Planos', 'fields': [
                {'name': 'speed_value', 'type': 'text', 'label': 'Velocidade'},
                {'name': 'speed_unit', 'type': 'select', 'label': 'Unidade', 'options': ['MEGA', 'GIGA']},
                {'name': 'current_price', 'type': 'text', 'label': 'Preço atual'},
                {'name': 'old_price', 'type': 'text', 'label': 'Preço antigo'},
                {'name': 'category_label', 'type': 'text', 'label': 'Categoria', 'default': 'INTERNET'},
                {'name': 'badge_text', 'type': 'text', 'label': 'Badge'},
                {'name': 'badge_bg_color', 'type': 'color', 'label': 'Cor do badge', 'default': '#2323FA'},
                {'name': 'badge_text_color', 'type': 'color', 'label': 'Cor texto badge', 'default': '#FFFFFF'},
                {'name': 'period', 'type': 'text', 'label': 'Período', 'default': '/mês'},
                {'name': 'button_text', 'type': 'text', 'label': 'Texto do botão', 'default': 'Aproveitar Oferta'},
                {'name': 'button_link', 'type': 'url', 'label': 'Link do botão'},
                {'name': 'features', 'type': 'list', 'label': 'Features (1 por linha)'},
            ]},
        ],
    },

    'feature_grid': {
        'name': 'Grid de Features',
        'icon': 'fa-solid fa-grip',
        'description': 'Grid de cards com ícone, título e descrição',
        'template': 'components/feature_grid.html',
        'schema': [
            {'name': 'tag', 'type': 'text', 'label': 'Tag/Label'},
            {'name': 'heading', 'type': 'text', 'label': 'Título', 'required': True},
            {'name': 'items', 'type': 'repeater', 'label': 'Items', 'fields': [
                {'name': 'icon', 'type': 'text', 'label': 'Ícone FontAwesome'},
                {'name': 'title', 'type': 'text', 'label': 'Título'},
                {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
            ]},
        ],
    },

    'text_with_card': {
        'name': 'Texto + Card Lateral',
        'icon': 'fa-solid fa-table-columns',
        'description': 'Seção com texto à esquerda e card à direita (ex: Mega Energia)',
        'template': 'components/text_with_card.html',
        'schema': [
            {'name': 'heading', 'type': 'textarea', 'label': 'Título', 'required': True},
            {'name': 'heading_highlight', 'type': 'text', 'label': 'Texto destacado (cor diferente)'},
            {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão'},
            {'name': 'cta_link', 'type': 'url', 'label': 'Link do botão'},
            {'name': 'card_title', 'type': 'text', 'label': 'Título do card'},
            {'name': 'card_icon', 'type': 'text', 'label': 'Ícone do card (FontAwesome)'},
            {'name': 'card_items', 'type': 'list', 'label': 'Items do card (checkmarks)'},
        ],
    },

    'hero_with_form': {
        'name': 'Hero com Formulário',
        'icon': 'fa-solid fa-rectangle-list',
        'description': 'Hero com texto à esquerda e formulário de lead à direita',
        'template': 'components/hero_with_form.html',
        'schema': [
            {'name': 'heading', 'type': 'textarea', 'label': 'Título', 'required': True},
            {'name': 'subheading', 'type': 'textarea', 'label': 'Subtítulo'},
            {'name': 'bg_color', 'type': 'color', 'label': 'Cor de fundo', 'default': '#2323FA'},
            {'name': 'bg_image', 'type': 'image', 'label': 'Imagem de fundo'},
            {'name': 'badges', 'type': 'list', 'label': 'Badges (1 por linha)'},
            {'name': 'form_title', 'type': 'text', 'label': 'Título do formulário'},
            {'name': 'form_subtitle', 'type': 'text', 'label': 'Subtítulo do formulário'},
            {'name': 'form_source', 'type': 'text', 'label': 'Origem do lead (ex: energia)'},
            {'name': 'form_fields', 'type': 'repeater', 'label': 'Campos do formulário', 'fields': [
                {'name': 'name', 'type': 'text', 'label': 'Nome do campo (HTML)'},
                {'name': 'label', 'type': 'text', 'label': 'Label'},
                {'name': 'type', 'type': 'select', 'label': 'Tipo', 'options': ['text', 'email', 'tel', 'select']},
                {'name': 'placeholder', 'type': 'text', 'label': 'Placeholder'},
                {'name': 'options', 'type': 'list', 'label': 'Opções (para select)'},
                {'name': 'half_width', 'type': 'checkbox', 'label': 'Meia largura'},
            ]},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão de CTA'},
            {'name': 'cta_link', 'type': 'url', 'label': 'Link do CTA'},
        ],
    },

    'steps': {
        'name': 'Passo a Passo',
        'icon': 'fa-solid fa-list-ol',
        'description': 'Seção com passos numerados (ex: Como funciona)',
        'template': 'components/steps.html',
        'schema': [
            {'name': 'tag', 'type': 'text', 'label': 'Tag'},
            {'name': 'heading', 'type': 'text', 'label': 'Título', 'required': True},
            {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão'},
            {'name': 'cta_link', 'type': 'url', 'label': 'Link do botão'},
            {'name': 'steps', 'type': 'repeater', 'label': 'Passos', 'fields': [
                {'name': 'title', 'type': 'text', 'label': 'Título'},
                {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
            ]},
        ],
    },

    'app_promo': {
        'name': 'Promoção de App',
        'icon': 'fa-solid fa-mobile-screen',
        'description': 'Seção com card do app e botões de download',
        'template': 'components/app_promo.html',
        'schema': [
            {'name': 'app_name', 'type': 'text', 'label': 'Nome do app'},
            {'name': 'card_title', 'type': 'text', 'label': 'Título do card'},
            {'name': 'card_description', 'type': 'textarea', 'label': 'Descrição do card'},
            {'name': 'heading', 'type': 'text', 'label': 'Título principal'},
            {'name': 'heading_subtitle', 'type': 'text', 'label': 'Subtítulo'},
            {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
            {'name': 'google_play_url', 'type': 'url', 'label': 'Google Play URL'},
            {'name': 'app_store_url', 'type': 'url', 'label': 'App Store URL'},
        ],
    },

    'cta_section': {
        'name': 'Call to Action',
        'icon': 'fa-solid fa-bullhorn',
        'description': 'Seção de destaque com botões de ação',
        'template': 'components/cta_section.html',
        'schema': [
            {'name': 'heading', 'type': 'textarea', 'label': 'Título', 'required': True},
            {'name': 'subheading', 'type': 'textarea', 'label': 'Subtítulo'},
            {'name': 'bg_color', 'type': 'color', 'label': 'Cor de fundo', 'default': '#2323FA'},
            {'name': 'primary_btn_text', 'type': 'text', 'label': 'Botão primário - texto'},
            {'name': 'primary_btn_link', 'type': 'url', 'label': 'Botão primário - link'},
            {'name': 'primary_btn_icon', 'type': 'text', 'label': 'Botão primário - ícone'},
            {'name': 'secondary_btn_text', 'type': 'text', 'label': 'Botão secundário - texto'},
            {'name': 'secondary_btn_link', 'type': 'url', 'label': 'Botão secundário - link'},
            {'name': 'footnote', 'type': 'text', 'label': 'Nota de rodapé'},
        ],
    },

    'savings_calculator': {
        'name': 'Calculadora de Economia',
        'icon': 'fa-solid fa-calculator',
        'description': 'Calculadora interativa com percentual de economia',
        'template': 'components/savings_calculator.html',
        'schema': [
            {'name': 'tag', 'type': 'text', 'label': 'Tag da seção'},
            {'name': 'heading', 'type': 'text', 'label': 'Título'},
            {'name': 'content_title', 'type': 'text', 'label': 'Título do conteúdo'},
            {'name': 'content_body', 'type': 'textarea', 'label': 'Corpo do texto'},
            {'name': 'savings_percentage', 'type': 'number', 'label': 'Percentual de economia', 'default': 20},
            {'name': 'checkmarks', 'type': 'list', 'label': 'Checkmarks (1 por linha)'},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão'},
        ],
    },

    'self_service_grid': {
        'name': 'Grid de Autoatendimento',
        'icon': 'fa-solid fa-headset',
        'description': 'Grid de links de autoatendimento com ícones',
        'template': 'components/self_service_grid.html',
        'schema': [
            {'name': 'heading', 'type': 'text', 'label': 'Título'},
            {'name': 'subheading', 'type': 'text', 'label': 'Subtítulo'},
            {'name': 'items', 'type': 'repeater', 'label': 'Items', 'fields': [
                {'name': 'title', 'type': 'text', 'label': 'Título'},
                {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
                {'name': 'icon', 'type': 'text', 'label': 'Ícone FontAwesome'},
                {'name': 'link', 'type': 'url', 'label': 'Link'},
                {'name': 'highlight', 'type': 'checkbox', 'label': 'Destacar (azul)'},
            ]},
        ],
    },

    'combo_cards': {
        'name': 'Cards de Combo',
        'icon': 'fa-solid fa-cubes',
        'description': 'Cards lado a lado com ícone colorido (ex: Internet + Energia + Segurança)',
        'template': 'components/combo_cards.html',
        'schema': [
            {'name': 'heading', 'type': 'textarea', 'label': 'Título'},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão'},
            {'name': 'cta_link', 'type': 'url', 'label': 'Link do botão'},
            {'name': 'combos', 'type': 'repeater', 'label': 'Combos', 'fields': [
                {'name': 'title', 'type': 'text', 'label': 'Título'},
                {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
                {'name': 'icon', 'type': 'text', 'label': 'Ícone FontAwesome'},
                {'name': 'color', 'type': 'color', 'label': 'Cor de fundo'},
            ]},
        ],
    },

    'benefits_showcase': {
        'name': 'Showcase de Benefícios',
        'icon': 'fa-solid fa-shield-halved',
        'description': 'Seção visual com card escuro e lista de benefícios + texto lateral',
        'template': 'components/benefits_showcase.html',
        'schema': [
            {'name': 'tag', 'type': 'text', 'label': 'Tag'},
            {'name': 'heading', 'type': 'textarea', 'label': 'Título'},
            {'name': 'description', 'type': 'textarea', 'label': 'Descrição'},
            {'name': 'cta_text', 'type': 'text', 'label': 'Texto do botão'},
            {'name': 'cta_link', 'type': 'url', 'label': 'Link do botão'},
            {'name': 'card_title', 'type': 'text', 'label': 'Título do card'},
            {'name': 'card_subtitle', 'type': 'text', 'label': 'Subtítulo do card'},
            {'name': 'benefits', 'type': 'repeater', 'label': 'Benefícios', 'fields': [
                {'name': 'icon', 'type': 'text', 'label': 'Ícone FontAwesome'},
                {'name': 'title', 'type': 'text', 'label': 'Título'},
                {'name': 'description', 'type': 'text', 'label': 'Descrição curta'},
            ]},
        ],
    },
}
