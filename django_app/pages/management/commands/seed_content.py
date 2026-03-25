from django.core.management.base import BaseCommand

from core.models import SiteConfig, MenuItem, FooterColumn, FooterLink
from pages.models import (
    Banner, InternetPlan, PlanFeature, Combo, Service, SelfServiceItem,
    AppPromo, MegaEnergiaHome, EnergyHero, EnergySavings, EnergyFeature,
    EnergyStep, TrackingHero, TrackingFeature, TrackingBenefit, TrackingCTA,
)


class Command(BaseCommand):
    help = 'Popula o banco com o conteúdo inicial do site (dados do PHP)'

    def handle(self, *args, **options):
        self._seed_config()
        self._seed_menus()
        self._seed_footer()
        self._seed_banners()
        self._seed_plans()
        self._seed_combos()
        self._seed_services()
        self._seed_self_service()
        self._seed_app_promo()
        self._seed_mega_energia()
        self._seed_energy()
        self._seed_tracking()
        self.stdout.write(self.style.SUCCESS('Seed completo!'))

    def _seed_config(self):
        config, _ = SiteConfig.objects.get_or_create(pk=1)
        config.company_name = 'MegaLink'
        config.logo_alt_text = 'MegaLink Provedor'
        config.primary_color = '#2323FA'
        config.primary_dark_color = '#040470'
        config.secondary_color = '#FF6905'
        config.accent_color = '#10B981'
        config.whatsapp_number = '558922210068'
        config.facebook_url = 'https://www.facebook.com/megalinkpiaui'
        config.instagram_url = 'https://www.instagram.com/soumegamais/'
        config.linkedin_url = 'https://www.linkedin.com/company/megalinktelecom/'
        config.youtube_url = 'https://www.youtube.com/@megalinktelecom1539'
        config.assine_ja_enabled = True
        config.assine_ja_link = '#assine'
        config.area_cliente_enabled = True
        config.area_cliente_link = '#area-cliente'
        config.footer_text = 'A melhor conexão para você e sua empresa.'
        config.company_address = 'Rua Exemplo, 123 - Centro, Cidade - UF'
        config.company_phone = '(11) 3333-4444'
        config.company_email = 'contato@megalink.com.br'
        config.footer_copyright = 'Copyright 2025 © - MegaLink - Todos os direitos reservados'
        config.footer_terms_url = '#termos'
        config.footer_privacy_url = '#privacidade'
        config.save()
        self.stdout.write('  Config criada')

    def _seed_menus(self):
        if MenuItem.objects.exists():
            return
        MenuItem.objects.create(title='Início', link='/', menu_location='main', order=0)
        MenuItem.objects.create(title='Planos', link='#planos', menu_location='main', order=1)
        MenuItem.objects.create(title='Aplicativo', link='#app', menu_location='main', order=2)
        self.stdout.write('  Menus criados')

    def _seed_footer(self):
        if FooterColumn.objects.exists():
            return
        col1 = FooterColumn.objects.create(title='Sobre nós', order=0)
        FooterLink.objects.create(column=col1, title='Sobre nós', url='#', order=0)
        FooterLink.objects.create(column=col1, title='Nossas lojas', url='/lojas', order=1)

        col2 = FooterColumn.objects.create(title='Cliente', order=1)
        FooterLink.objects.create(column=col2, title='2ª via de conta',
                                  url='https://central.megalinktelecom.hubsoft.com.br/', order=0)
        FooterLink.objects.create(column=col2, title='Renovação',
                                  url='https://central.megalinktelecom.hubsoft.com.br/', order=1)

        col3 = FooterColumn.objects.create(title='Saiba mais', order=2)
        FooterLink.objects.create(column=col3, title='Transparência', url='#', order=0)
        FooterLink.objects.create(column=col3, title='Indique e Ganhe',
                                  url='https://indique.megalinkpiaui.com.br/mega-cliente',
                                  open_new_tab=True, order=1)
        self.stdout.write('  Footer criado')

    def _seed_banners(self):
        if Banner.objects.exists():
            return
        # Note: image field requires actual file. Using placeholder path.
        self.stdout.write('  Banners: precisa upload manual via admin (imagens)')

    def _seed_plans(self):
        if InternetPlan.objects.exists():
            return
        plans_data = [
            {'speed_value': '320', 'speed_unit': 'MEGA', 'current_price': '89,90', 'old_price': '117,90',
             'show_badge': False,
             'button_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+320MB',
             'features': ['Instalação Grátis', '100% fibra óptica', 'WI-FI de alta performance',
                          '1 Dispositivo Cabeado', 'Suporte 24h', 'Download 320Mbps', 'Upload 320Mbps']},
            {'speed_value': '620', 'speed_unit': 'MEGA', 'current_price': '99,90', 'old_price': '137,90',
             'show_badge': True, 'badge_text': 'MELHOR OFERTA',
             'button_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+620MB',
             'features': ['Instalação Grátis', '100% fibra óptica', 'WI-FI de alta performance',
                          '1 Dispositivo Cabeado', 'Suporte 24h', 'Download 620Mbps', 'Upload 620Mbps']},
            {'speed_value': '1', 'speed_unit': 'GIGA', 'current_price': '129,90', 'old_price': '167,90',
             'show_badge': False,
             'button_link': 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+1GB',
             'features': ['Instalação grátis', '100% fibra óptica', 'WI-FI de alta performance',
                          '1 Dispositivo Cabeado', 'Suporte 24h', 'Download 1000Mbps', 'Upload 1000Mbps']},
        ]
        for i, pd in enumerate(plans_data):
            plan = InternetPlan.objects.create(
                page='home', category_label='INTERNET',
                speed_value=pd['speed_value'], speed_unit=pd['speed_unit'],
                current_price=pd['current_price'], old_price=pd['old_price'],
                button_text='Aproveitar Oferta', button_link=pd['button_link'],
                show_badge=pd['show_badge'], badge_text=pd.get('badge_text', ''),
                order=i,
            )
            for j, feat in enumerate(pd['features']):
                PlanFeature.objects.create(plan=plan, text=feat, order=j)
        self.stdout.write('  Planos criados')

    def _seed_combos(self):
        if Combo.objects.exists():
            return
        Combo.objects.create(title='Internet', description='Serviços de internet 100% fibra óptica.',
                             icon_class='fa-wifi', color_class='bg-[#FF6905]', order=0)
        Combo.objects.create(title='Mega Energia', description='Economia e sustentabilidade para sua residência.',
                             icon_class='fa-bolt', color_class='bg-[#10B981]', order=1)
        Combo.objects.create(title='Mega Segurança', description='Proteção e monitoramento 24h para sua família.',
                             icon_class='fa-shield-halved', color_class='bg-[#2323FA]', order=2)
        self.stdout.write('  Combos criados')

    def _seed_services(self):
        if Service.objects.exists():
            return
        Service.objects.create(title='MegaLink 5G',
                               description='O futuro da conexão móvel agora disponível para você com a qualidade MegaLink.',
                               order=0)
        Service.objects.create(title='Mega Music',
                               description='Acesso ilimitado a milhares de músicas e playlists exclusivas para clientes MegaLink.',
                               order=1)
        Service.objects.create(title='Mega Play',
                               description='Assista a filmes e séries com a melhor qualidade de streaming.',
                               order=2)
        Service.objects.create(title='Conecta +',
                               description='A melhor solução para sua casa inteligente, conectando todos os seus dispositivos com segurança.',
                               order=3)
        self.stdout.write('  Serviços criados')

    def _seed_self_service(self):
        if SelfServiceItem.objects.exists():
            return
        items = [
            ('2ª via da fatura', 'Baixe sua fatura através do portal do cliente', 'fa-solid fa-file-invoice', '#', True),
            ('Ligamos para você', 'Informe seus dados que entraremos em contato', 'fa-solid fa-phone', '#', False),
            ('Central de ajuda', 'Tudo o que você precisa saber para tirar suas dúvidas', 'fa-regular fa-circle-question', '#', False),
            ('Suporte remoto', 'Realizamos o seu atendimento por acesso remoto', 'fa-solid fa-desktop', '#', False),
            ('Nossas lojas', 'Verifique as lojas parceiras MegaLink na sua cidade', 'fa-solid fa-location-dot', '#', False),
            ('Ouvidoria', 'Nosso canal de ética pronto para resolver', 'fa-solid fa-headset', '#', False),
        ]
        for i, (title, desc, icon, link, hl) in enumerate(items):
            SelfServiceItem.objects.create(title=title, description=desc, icon_class=icon,
                                           link=link, highlight=hl, order=i)
        self.stdout.write('  Autoatendimento criado')

    def _seed_app_promo(self):
        if AppPromo.objects.exists():
            return
        AppPromo.objects.create(
            page='home', app_name='MegalinkApp', card_title='Megacliente',
            card_description='O aplicativo oficial da MegaLink para autoatendimento.',
            heading='MegalinkApp', heading_subtitle='Completo. Simples.',
            description='Gerencie sua conta, emita segunda via, acompanhe seu consumo e muito mais. Tudo na palma da sua mão com o App MegaLink.',
            google_play_url='https://play.google.com/store/apps/details?id=com.hubsoft_client_app.megalinktelecom&hl=pt_BR',
            app_store_url='https://apps.apple.com/br/app/megalinkapp/id6468992571',
        )
        AppPromo.objects.create(
            page='rastreamento', app_name='Mega Rastreamento',
            card_title='Mega Rastreamento',
            card_description='Monitoramento em tempo real, interface fácil e intuitiva, notificações automáticas.',
            heading='Controle total na ponta dos seus dedos',
            heading_subtitle='',
            description='Baixe nosso aplicativo exclusivo de rastreamento e tenha acesso a todas as funcionalidades do sistema diretamente do seu smartphone ou tablet.',
            google_play_url='https://play.google.com/store/apps/details?id=com.hubsoft_client_app.megalinktelecom&hl=pt_BR',
            app_store_url='https://apps.apple.com/br/app/megalinkapp/id6468992571',
        )
        self.stdout.write('  App promos criados')

    def _seed_mega_energia(self):
        obj, _ = MegaEnergiaHome.objects.get_or_create(pk=1)
        obj.heading = 'Mega Energia sua conta com até'
        obj.heading_highlight = '20% de desconto'
        obj.description = 'Tenha economia e sustentabilidade para sua residência sem obras e sem investimento. Uma solução 100% digital para você economizar na conta de luz todos os meses.'
        obj.cta_text = 'Quero economizar'
        obj.cta_link = '/energia'
        obj.card_title = 'Simples e Digital'
        obj.card_features = ['Sem fidelidade', 'Sem obras', 'Energia limpa e renovável']
        obj.save()
        self.stdout.write('  Mega Energia Home criado')

    def _seed_energy(self):
        hero, _ = EnergyHero.objects.get_or_create(pk=1)
        hero.heading = 'Economize até 20% na sua conta de energia'
        hero.highlight_text = '20%'
        hero.subheading = 'Sem taxas, sem custo de adesão e sem instalação de placas solares.'
        hero.badge_1 = 'Sem fidelidade'
        hero.badge_2 = '100% Digital'
        hero.form_title = 'Informe seus dados para contato'
        hero.form_subtitle = 'Fale com um de nossos especialistas.'
        hero.save()

        sav, _ = EnergySavings.objects.get_or_create(pk=1)
        sav.section_tag = 'Inovação Solar'
        sav.heading = 'Mais economia para você'
        sav.content_title = 'Energia por Assinatura'
        sav.content_body = 'A oportunidade de economizar na conta de luz agora está ao seu alcance. Assine nossa energia renovável e tenha desconto garantido todo mês direto na sua fatura da distribuidora.\n\nVocê não precisa instalar placas solares, nem fazer obras no telhado. É tudo digital, simples e com zero fidelidade.'
        sav.savings_percentage = 20
        sav.checkmarks = ['Sem taxa de adesão', 'Sem fidelidade', 'Economia garantida', 'Sem instalação']
        sav.cta_text = 'Garantir meu desconto'
        sav.save()

        if not EnergyFeature.objects.exists():
            EnergyFeature.objects.create(icon_class='fa-solid fa-hand-holding-dollar',
                                         title='Economia o ano todo',
                                         description='Você economiza na conta de luz todos os meses, sem exceção. O desconto é aplicado diretamente.',
                                         order=0)
            EnergyFeature.objects.create(icon_class='fa-solid fa-mobile-screen',
                                         title='Contratação 100% digital',
                                         description='Faça tudo pelo celular ou computador. Sem papelada, sem filas e sem burocracia desnecessária.',
                                         order=1)
            EnergyFeature.objects.create(icon_class='fa-solid fa-file-contract',
                                         title='Sem fidelidade',
                                         description='Você é livre para ir e vir. Cancele quando quiser sem pagar multas abusivas ou taxas extras.',
                                         order=2)
            EnergyFeature.objects.create(icon_class='fa-solid fa-leaf',
                                         title='Energia limpa e sustentável',
                                         description='Consuma energia de fontes renováveis e contribua para um planeta mais verde e saudável.',
                                         order=3)

        if not EnergyStep.objects.exists():
            EnergyStep.objects.create(number=1, title='Cadastro',
                                      description='Você faz seu cadastro em nosso site em menos de 2 minutos, informando dados básicos.',
                                      order=0)
            EnergyStep.objects.create(number=2, title='Análise',
                                      description='Avaliamos sua conta de energia para indicar a melhor usina solar disponível para você.',
                                      order=1)
            EnergyStep.objects.create(number=3, title='Conexão',
                                      description='Conectamos sua unidade consumidora à nossa fazenda solar de forma 100% digital.',
                                      order=2)
            EnergyStep.objects.create(number=4, title='Economia',
                                      description='Você recebe o desconto na sua conta de energia e acompanha tudo pelo app.',
                                      order=3)
        self.stdout.write('  Energia seeded')

    def _seed_tracking(self):
        hero, _ = TrackingHero.objects.get_or_create(pk=1)
        hero.tag_text = 'Monitoramento 24h'
        hero.heading = 'O controle do seu veículo na palma da sua mão'
        hero.subheading = 'Mais segurança para você e sua família. Localização em tempo real, bloqueio remoto e proteção contra roubo e furto.'
        hero.cta_text = 'Quero proteger meu veículo'
        hero.cta_link = '#contratar'
        hero.form_title = 'Proteja seu veículo agora'
        hero.form_subtitle = 'Preencha o formulário e fale com um consultor.'
        hero.save()

        if not TrackingFeature.objects.exists():
            TrackingFeature.objects.create(icon_class='fa-solid fa-map-location-dot',
                                           title='Localização em Tempo Real',
                                           description='Saiba exatamente onde seu veículo está a qualquer momento através do aplicativo.',
                                           order=0)
            TrackingFeature.objects.create(icon_class='fa-solid fa-lock',
                                           title='Bloqueio Remoto',
                                           description='Em caso de emergência, bloqueie o funcionamento do veículo com apenas um clique.',
                                           order=1)
            TrackingFeature.objects.create(icon_class='fa-solid fa-clock-rotate-left',
                                           title='Histórico de Rotas',
                                           description='Consulte todo o trajeto percorrido, paradas e horários dos últimos meses.',
                                           order=2)
            TrackingFeature.objects.create(icon_class='fa-solid fa-gauge-high',
                                           title='Alerta de Velocidade',
                                           description='Seja notificado caso o veículo ultrapasse o limite de velocidade definido por você.',
                                           order=3)

        if not TrackingBenefit.objects.exists():
            TrackingBenefit.objects.create(icon_class='fa-solid fa-money-bill-wave',
                                           title='Recuperação em caso de Roubo',
                                           description='Maior chance de recuperar seu bem.',
                                           order=0)
            TrackingBenefit.objects.create(icon_class='fa-solid fa-user-shield',
                                           title='Segurança Familiar',
                                           description='Saiba onde sua família está.',
                                           order=1)
            TrackingBenefit.objects.create(icon_class='fa-solid fa-hand-holding-dollar',
                                           title='Valorização na Revenda',
                                           description='Histórico valoriza seu veículo.',
                                           order=2)

        cta, _ = TrackingCTA.objects.get_or_create(pk=1)
        cta.heading = 'Não espere o imprevisto acontecer.\nProteja seu veículo hoje mesmo.'
        cta.subheading = 'Planos acessíveis que cabem no seu bolso. Fale com um de nossos consultores e escolha a melhor opção para você.'
        cta.primary_button_text = 'Falar com Consultor'
        cta.primary_button_link = 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+gostaria+de+saber+mais+sobre+o+Rastreamento+Veicular'
        cta.secondary_button_text = 'Ver Planos'
        cta.secondary_button_link = '#'
        cta.footnote = '* Instalação rápida e suporte técnico especializado em toda a região.'
        cta.save()
        self.stdout.write('  Rastreamento seeded')
