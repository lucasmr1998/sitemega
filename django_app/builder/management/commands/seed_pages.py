from django.core.management.base import BaseCommand
from builder.models import Page, ComponentType, PageComponent


class Command(BaseCommand):
    help = 'Cria as páginas legadas (Home, Energia, Rastreamento) com componentes'

    def handle(self, *args, **options):
        self._create_home()
        self._create_energia()
        self._create_rastreamento()
        self.stdout.write(self.style.SUCCESS('Páginas legadas criadas!'))

    def _get_type(self, slug):
        return ComponentType.objects.get(slug=slug)

    def _create_home(self):
        page, created = Page.objects.get_or_create(
            slug='home',
            defaults={'title': 'Home', 'status': 'published', 'is_homepage': True},
        )
        if not created:
            page.sections.all().delete()
            self.stdout.write('  Home: limpando componentes existentes...')

        # 1. Banner Carousel
        PageComponent.objects.create(
            page=page, component_type=self._get_type('banner_carousel'), order=0,
            data={
                'banners': [
                    {
                        'title': 'Internet Fibra Óptica',
                        'image': '/static/img/SUPER BANNER SITE 04.png',
                        'link': '#assine',
                    },
                ],
            },
        )

        # 2. Pricing Cards
        PageComponent.objects.create(
            page=page, component_type=self._get_type('pricing_cards'), order=1,
            data={
                'section_title': 'Internet',
                'speed_color': '#2323FA',
                'underline_color': '#FF6905',
                'button_color': '#FF6905',
                'plans': [
                    {
                        'speed_value': '320',
                        'speed_unit': 'MEGA',
                        'current_price': '89,90',
                        'old_price': '117,90',
                        'category_label': 'INTERNET',
                        'badge_text': '',
                        'badge_bg_color': '#2323FA',
                        'badge_text_color': '#FFFFFF',
                        'period': '/mês',
                        'button_text': 'Aproveitar Oferta',
                        'button_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+320MB',
                        'features': [
                            'Instalação Grátis',
                            '100% fibra óptica',
                            'WI-FI de alta performance',
                            '1 Dispositivo Cabeado',
                            'Suporte 24h',
                            'Download 320Mbps',
                            'Upload 320Mbps',
                        ],
                    },
                    {
                        'speed_value': '620',
                        'speed_unit': 'MEGA',
                        'current_price': '99,90',
                        'old_price': '137,90',
                        'category_label': 'INTERNET',
                        'badge_text': 'MELHOR OFERTA',
                        'badge_bg_color': '#2323FA',
                        'badge_text_color': '#FFFFFF',
                        'period': '/mês',
                        'button_text': 'Aproveitar Oferta',
                        'button_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+620MB',
                        'features': [
                            'Instalação Grátis',
                            '100% fibra óptica',
                            'WI-FI de alta performance',
                            '1 Dispositivo Cabeado',
                            'Suporte 24h',
                            'Download 620Mbps',
                            'Upload 620Mbps',
                        ],
                    },
                    {
                        'speed_value': '1',
                        'speed_unit': 'GIGA',
                        'current_price': '129,90',
                        'old_price': '167,90',
                        'category_label': 'INTERNET',
                        'badge_text': '',
                        'badge_bg_color': '#2323FA',
                        'badge_text_color': '#FFFFFF',
                        'period': '/mês',
                        'button_text': 'Aproveitar Oferta',
                        'button_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+1GB',
                        'features': [
                            'Instalação grátis',
                            '100% fibra óptica',
                            'WI-FI de alta performance',
                            '1 Dispositivo Cabeado',
                            'Suporte 24h',
                            'Download 1000Mbps',
                            'Upload 1000Mbps',
                        ],
                    },
                ],
            },
        )

        # 3. Mega Energia (Text with Card)
        PageComponent.objects.create(
            page=page, component_type=self._get_type('text_with_card'), order=2,
            data={
                'heading': 'Mega Energia sua conta com até',
                'heading_highlight': '20% de desconto',
                'description': 'Tenha economia e sustentabilidade para sua residência sem obras e sem investimento. Uma solução 100% digital para você economizar na conta de luz todos os meses.',
                'cta_text': 'Quero economizar',
                'cta_link': '/p/energia',
                'card_title': 'Simples e Digital',
                'card_icon': 'fa-solid fa-bolt',
                'card_items': ['Sem fidelidade', 'Sem obras', 'Energia limpa e renovável'],
            },
        )

        # 4. App Promo
        PageComponent.objects.create(
            page=page, component_type=self._get_type('app_promo'), order=3,
            data={
                'app_name': 'Megalink',
                'card_title': 'Megacliente',
                'card_description': 'O aplicativo oficial da MegaLink para autoatendimento.',
                'heading': 'MegalinkApp',
                'heading_subtitle': 'Completo. Simples.',
                'description': 'Gerencie sua conta, emita segunda via, acompanhe seu consumo e muito mais. Tudo na palma da sua mão com o App MegaLink.',
                'google_play_url': 'https://play.google.com/store/apps/details?id=com.hubsoft_client_app.megalinktelecom&hl=pt_BR',
                'app_store_url': 'https://apps.apple.com/br/app/megalinkapp/id6468992571',
            },
        )

        self.stdout.write('  Home criada (4 componentes)')

    def _create_energia(self):
        page, created = Page.objects.get_or_create(
            slug='energia',
            defaults={'title': 'Mega Energia', 'status': 'published'},
        )
        if not created:
            page.sections.all().delete()
            self.stdout.write('  Energia: limpando componentes existentes...')

        # 1. Hero with Form
        PageComponent.objects.create(
            page=page, component_type=self._get_type('hero_with_form'), order=0,
            data={
                'heading': 'Economize até 20% na sua conta de energia',
                'subheading': 'Sem taxas, sem custo de adesão e sem instalação de placas solares.',
                'bg_color': '#2323FA',
                'bg_image': '',
                'badges': ['Sem fidelidade', '100% Digital'],
                'form_title': 'Informe seus dados para contato',
                'form_subtitle': 'Fale com um de nossos especialistas.',
                'form_source': 'energia',
                'form_fields': [
                    {'name': 'nome', 'label': 'Nome Completo', 'type': 'text', 'placeholder': 'João da Silva', 'options': [], 'half_width': False},
                    {'name': 'email', 'label': 'E-mail', 'type': 'email', 'placeholder': 'nome@exemplo.com', 'options': [], 'half_width': False},
                    {'name': 'celular', 'label': 'Celular', 'type': 'tel', 'placeholder': '(00) 00000-0000', 'options': [], 'half_width': True},
                    {'name': 'cep', 'label': 'CEP', 'type': 'text', 'placeholder': '00000-000', 'options': [], 'half_width': True},
                    {'name': 'media_conta', 'label': 'Qual sua média de conta de energia?', 'type': 'select', 'placeholder': 'Selecione uma faixa', 'options': ['Abaixo de R$ 200', 'Entre R$ 200 e R$ 500', 'Acima de R$ 500'], 'half_width': False},
                ],
                'cta_text': '',
                'cta_link': '',
            },
        )

        # 2. Savings Calculator
        PageComponent.objects.create(
            page=page, component_type=self._get_type('savings_calculator'), order=1,
            data={
                'tag': 'Inovação Solar',
                'heading': 'Mais economia para você',
                'content_title': 'Energia por Assinatura',
                'content_body': 'A oportunidade de economizar na conta de luz agora está ao seu alcance. Assine nossa energia renovável e tenha desconto garantido todo mês direto na sua fatura da distribuidora.\n\nVocê não precisa instalar placas solares, nem fazer obras no telhado. É tudo digital, simples e com zero fidelidade.',
                'savings_percentage': 20,
                'checkmarks': ['Sem taxa de adesão', 'Sem fidelidade', 'Economia garantida', 'Sem instalação'],
                'cta_text': 'Garantir meu desconto',
            },
        )

        # 3. Feature Grid (Vantagens)
        PageComponent.objects.create(
            page=page, component_type=self._get_type('feature_grid'), order=2,
            data={
                'tag': 'Vantagens',
                'heading': 'Vantagens da Assinatura de Energia',
                'items': [
                    {'icon': 'fa-solid fa-hand-holding-dollar', 'title': 'Economia o ano todo', 'description': 'Você economiza na conta de luz todos os meses, sem exceção. O desconto é aplicado diretamente.'},
                    {'icon': 'fa-solid fa-mobile-screen', 'title': 'Contratação 100% digital', 'description': 'Faça tudo pelo celular ou computador. Sem papelada, sem filas e sem burocracia desnecessária.'},
                    {'icon': 'fa-solid fa-file-contract', 'title': 'Sem fidelidade', 'description': 'Você é livre para ir e vir. Cancele quando quiser sem pagar multas abusivas ou taxas extras.'},
                    {'icon': 'fa-solid fa-leaf', 'title': 'Energia limpa e sustentável', 'description': 'Consuma energia de fontes renováveis e contribua para um planeta mais verde e saudável.'},
                ],
            },
        )

        # 4. Steps
        PageComponent.objects.create(
            page=page, component_type=self._get_type('steps'), order=3,
            data={
                'tag': 'Passo a passo',
                'heading': 'Veja como é fácil',
                'description': 'Todo o processo é feito online, de forma rápida e segura. Comece a economizar em poucos cliques.',
                'cta_text': 'Simule agora mesmo',
                'cta_link': '#',
                'steps': [
                    {'title': 'Cadastro', 'description': 'Você faz seu cadastro em nosso site em menos de 2 minutos, informando dados básicos.'},
                    {'title': 'Análise', 'description': 'Avaliamos sua conta de energia para indicar a melhor usina solar disponível para você.'},
                    {'title': 'Conexão', 'description': 'Conectamos sua unidade consumidora à nossa fazenda solar de forma 100% digital.'},
                    {'title': 'Economia', 'description': 'Você recebe o desconto na sua conta de energia e acompanha tudo pelo app.'},
                ],
            },
        )

        self.stdout.write('  Energia criada (4 componentes)')

    def _create_rastreamento(self):
        page, created = Page.objects.get_or_create(
            slug='rastreamento',
            defaults={'title': 'Mega Rastreamento', 'status': 'published'},
        )
        if not created:
            page.sections.all().delete()
            self.stdout.write('  Rastreamento: limpando componentes existentes...')

        # 1. Hero with Form
        PageComponent.objects.create(
            page=page, component_type=self._get_type('hero_with_form'), order=0,
            data={
                'heading': 'O controle do seu veículo na palma da sua mão',
                'subheading': 'Mais segurança para você e sua família. Localização em tempo real, bloqueio remoto e proteção contra roubo e furto.',
                'bg_color': '#2323FA',
                'bg_image': '',
                'badges': ['Monitoramento 24h'],
                'form_title': 'Proteja seu veículo agora',
                'form_subtitle': 'Preencha o formulário e fale com um consultor.',
                'form_source': 'rastreamento',
                'form_fields': [
                    {'name': 'nome', 'label': 'Nome Completo', 'type': 'text', 'placeholder': 'Seu nome', 'options': [], 'half_width': False},
                    {'name': 'email', 'label': 'E-mail', 'type': 'email', 'placeholder': 'seu@email.com', 'options': [], 'half_width': False},
                    {'name': 'celular', 'label': 'Celular', 'type': 'tel', 'placeholder': '(86) 99999-9999', 'options': [], 'half_width': True},
                    {'name': 'cep', 'label': 'CEP', 'type': 'text', 'placeholder': '00000-000', 'options': [], 'half_width': True},
                    {'name': 'tipo_veiculo', 'label': 'Tipo de Veículo', 'type': 'select', 'placeholder': 'Selecione uma opção', 'options': ['Carro de Passeio', 'Motocicleta', 'Caminhão / Frota', 'Outros'], 'half_width': False},
                ],
                'cta_text': 'Quero proteger meu veículo',
                'cta_link': '#contratar',
            },
        )

        # 2. Feature Grid (Funcionalidades)
        PageComponent.objects.create(
            page=page, component_type=self._get_type('feature_grid'), order=1,
            data={
                'tag': '',
                'heading': 'Tudo o que você precisa para assumir o controle',
                'items': [
                    {'icon': 'fa-solid fa-map-location-dot', 'title': 'Localização em Tempo Real', 'description': 'Saiba exatamente onde seu veículo está a qualquer momento através do aplicativo.'},
                    {'icon': 'fa-solid fa-lock', 'title': 'Bloqueio Remoto', 'description': 'Em caso de emergência, bloqueie o funcionamento do veículo com apenas um clique.'},
                    {'icon': 'fa-solid fa-clock-rotate-left', 'title': 'Histórico de Rotas', 'description': 'Consulte todo o trajeto percorrido, paradas e horários dos últimos meses.'},
                    {'icon': 'fa-solid fa-gauge-high', 'title': 'Alerta de Velocidade', 'description': 'Seja notificado caso o veículo ultrapasse o limite de velocidade definido por você.'},
                ],
            },
        )

        # 3. Benefits Showcase
        PageComponent.objects.create(
            page=page, component_type=self._get_type('benefits_showcase'), order=2,
            data={
                'tag': 'Por que escolher?',
                'heading': 'Mais que rastreamento, uma solução completa de segurança.',
                'description': 'A MegaLink oferece a tecnologia mais avançada do mercado para garantir que seu carro ou moto esteja sempre protegido. Durma tranquilo sabendo onde seu veículo está.',
                'cta_text': 'Proteger agora',
                'cta_link': '#contratar',
                'card_title': 'Tranquilidade Garantida',
                'card_subtitle': 'Monitoramento 24h por dia.',
                'benefits': [
                    {'icon': 'fa-solid fa-money-bill-wave', 'title': 'Recuperação em caso de Roubo', 'description': 'Maior chance de recuperar seu bem.'},
                    {'icon': 'fa-solid fa-user-shield', 'title': 'Segurança Familiar', 'description': 'Saiba onde sua família está.'},
                    {'icon': 'fa-solid fa-hand-holding-dollar', 'title': 'Valorização na Revenda', 'description': 'Histórico valoriza seu veículo.'},
                ],
            },
        )

        # 4. App Promo
        PageComponent.objects.create(
            page=page, component_type=self._get_type('app_promo'), order=3,
            data={
                'app_name': 'Mega Rastreamento',
                'card_title': 'Mega Rastreamento',
                'card_description': 'Monitoramento em tempo real, interface fácil e intuitiva, notificações automáticas.',
                'heading': 'Controle total na ponta dos seus dedos',
                'heading_subtitle': '',
                'description': 'Baixe nosso aplicativo exclusivo de rastreamento e tenha acesso a todas as funcionalidades do sistema diretamente do seu smartphone ou tablet.',
                'google_play_url': 'https://play.google.com/store/apps/details?id=com.hubsoft_client_app.megalinktelecom&hl=pt_BR',
                'app_store_url': 'https://apps.apple.com/br/app/megalinkapp/id6468992571',
            },
        )

        # 5. CTA
        PageComponent.objects.create(
            page=page, component_type=self._get_type('cta_section'), order=4,
            data={
                'heading': 'Não espere o imprevisto acontecer.\nProteja seu veículo hoje mesmo.',
                'subheading': 'Planos acessíveis que cabem no seu bolso. Fale com um de nossos consultores e escolha a melhor opção para você.',
                'bg_color': '#2323FA',
                'primary_btn_text': 'Falar com Consultor',
                'primary_btn_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+gostaria+de+saber+mais+sobre+o+Rastreamento+Veicular',
                'primary_btn_icon': 'fa-brands fa-whatsapp',
                'secondary_btn_text': 'Ver Planos',
                'secondary_btn_link': '#',
                'footnote': '* Instalação rápida e suporte técnico especializado em toda a região.',
            },
        )

        self.stdout.write('  Rastreamento criada (5 componentes)')
