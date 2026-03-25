<?php
// Configuração Específica para Variação Algar
$config = [
    // Cores MegaLink (Aplicadas ao Layout Algar)
    'primaryColor' => '#2323FA',     // Azul MegaLink
    'primaryDarkColor' => '#040470', // Azul Escuro
    'secondaryColor' => '#FF6905',   // Laranja MegaLink
    'accentColor' => '#FF6905',      // Laranja como destaque

    // Identidade
    'companyName' => 'MegaLink',
    'logoUrl' => 'assets/img/logo-megalink.png',
    'logoAltText' => 'MegaLink',

    // Links Sociais (Copiados da Home)
    'facebookUrl' => 'https://www.facebook.com/megalinkpiaui',
    'instagramUrl' => 'https://www.instagram.com/soumegamais/',
    'twitterUrl' => '#',
    'linkedinUrl' => 'https://www.linkedin.com/company/megalinktelecom/',
    'youtubeUrl' => 'https://www.youtube.com/@megalinktelecom1539',
    'whatsappNumber' => '558922210068',

    // Header/Footer
    'assineJaEnabled' => true,
    'assineJaLink' => '#assine',
    'areaClienteEnabled' => true,
    'areaClienteLink' => '#area-cliente',

    // Rodapé (Copiado da Home)
    'footerText' => 'A melhor conexão para você e sua empresa.',
    'footerCopyright' => 'Copyright 2025 © - MegaLink - Todos os direitos reservados',
    'footerTermsUrl' => '#termos',
    'footerPrivacyUrl' => '#privacidade',
    'companyAddress' => 'Rua Exemplo, 123 - Centro, Cidade - UF',
    'companyPhone' => '(11) 3333-4444',
    'companyEmail' => 'contato@megalink.com.br'
];

// Menu Complexo (Mega Menu Structure)
$menus = [
    [
        'id' => 1,
        'title' => 'Produtos e Serviços',
        'link' => '#',
        'isMegaMenu' => true,
        'isActive' => true,
        'columns' => [
            [
                'title' => 'Para sua casa',
                'items' => [
                    ['title' => 'Internet Fibra', 'link' => '#'],
                    ['title' => 'Fixo', 'link' => '#'],
                    ['title' => 'Conheça nossos serviços', 'link' => '#'],
                    ['title' => 'Super Wi-Fi', 'link' => '#']
                ]
            ],
            [
                'title' => 'Celular',
                'items' => [
                    ['title' => 'Controle e Pós', 'link' => '#'],
                    ['title' => '5G para sua casa', 'link' => '#'],
                    ['title' => 'Pré-Pago', 'link' => '#'],
                    ['title' => 'Recarga', 'link' => '#'],
                    ['title' => 'Aparelhos', 'link' => '#']
                ]
            ],
            [
                'title' => 'Serviços Digitais',
                'items' => [
                    ['title' => 'Disney+', 'link' => '#'],
                    ['title' => 'Nomo Music', 'link' => '#'],
                    ['title' => 'Globoplay', 'link' => '#'],
                    ['title' => 'Sky+', 'link' => '#'],
                    ['title' => 'HBO Max', 'link' => '#'],
                    ['title' => 'Veja todos serviços', 'link' => '#']
                ]
            ]
        ]
    ],
    [
        'id' => 2,
        'title' => 'Atendimento',
        'link' => '#',
        'isMegaMenu' => true, // Changed to Mega Menu
        'isActive' => false,
        'columns' => [
            [
                'title' => 'Autoatendimento',
                'items' => [
                    ['title' => '2ª via', 'link' => '#'],
                    ['title' => 'Detalhamento', 'link' => '#'],
                    ['title' => 'Débito automático', 'link' => '#'],
                    ['title' => 'Suporte técnico', 'link' => '#'],
                    ['title' => 'Negociação de Contas', 'link' => '#'],
                    ['title' => 'Lista telefônica', 'link' => '#']
                ]
            ],
            [
                'title' => 'Canais de atendimento',
                'items' => [
                    ['title' => 'App Algar', 'link' => '#'], // Keeping "App Algar" text from print, maybe should be App MegaLink? Leaving as is for fidelity.
                    ['title' => 'Lojas e credenciadas', 'link' => '#'],
                    ['title' => 'Central de atendimento', 'link' => '#'],
                    ['title' => 'Ponto de venda e recarga', 'link' => '#'],
                    ['title' => 'Ouvidoria', 'link' => '#'],
                    ['title' => 'Jurídico', 'link' => '#']
                ]
            ],
            [
                'title' => 'Informações',
                'items' => [
                    ['title' => 'Telefones úteis', 'link' => '#'],
                    ['title' => 'Portadores de necessidades', 'link' => '#'],
                    ['title' => 'Códigos DDD e DDI', 'link' => '#'],
                    ['title' => 'Pesquisa Anatel', 'link' => '#'],
                    ['title' => 'Incidência de tributos', 'link' => '#'],
                    ['title' => 'Consulta de interrupções', 'link' => '#'],
                    ['title' => 'Regulamentações Anatel', 'link' => '#'],
                    ['title' => 'Portabilidade', 'link' => '#']
                ]
            ],
            [
                'title' => 'Saiba Mais',
                'items' => [
                    ['title' => 'Conta digital', 'link' => '#'],
                    ['title' => 'Regulamentos', 'link' => '#'],
                    ['title' => 'Comunicados/Interrupções', 'link' => '#'],
                    ['title' => '9º dígito', 'link' => '#'],
                    ['title' => 'Conheça seu wi-fi', 'link' => '#'],
                    ['title' => 'Contratos', 'link' => '#'],
                    ['title' => 'Dicas de segurança', 'link' => '#'],
                    ['title' => 'Não Me Perturbe', 'link' => '#']
                ]
            ]
        ]
    ],
    [
        'id' => 3,
        'title' => 'Mais',
        'link' => '#',
        'isMegaMenu' => false,
        'children' => [
            ['title' => 'Sobre a MegaLink', 'link' => '#'],
            ['title' => 'Carreiras', 'link' => '#']
        ]
    ],
];
?>