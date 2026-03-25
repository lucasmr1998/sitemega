<?php
// Configuração Mockada (Simulando o Banco de Dados)
$config = [
    'primaryColor' => '#2323FA',
    'primaryDarkColor' => '#040470',
    'secondaryColor' => '#FF6905',
    'companyName' => 'MegaLink',
    'logoUrl' => 'assets/img/logo-megalink.png', // Logo configurada
    'logoAltText' => 'MegaLink Provedor',

    // Links Sociais
    'facebookUrl' => 'https://www.facebook.com/megalinkpiaui',
    'instagramUrl' => 'https://www.instagram.com/soumegamais/',
    'twitterUrl' => '#',
    'linkedinUrl' => 'https://www.linkedin.com/company/megalinktelecom/',
    'youtubeUrl' => 'https://www.youtube.com/@megalinktelecom1539',
    'whatsappNumber' => '558922210068',

    // Links Header
    'assineJaEnabled' => true,
    'assineJaLink' => '#assine',
    'areaClienteEnabled' => true,
    'areaClienteLink' => '#area-cliente',

    // Rodapé
    'footerText' => 'A melhor conexão para você e sua empresa.',
    'companyAddress' => 'Rua Exemplo, 123 - Centro, Cidade - UF',
    'companyPhone' => '(11) 3333-4444',
    'companyEmail' => 'contato@megalink.com.br',
    'footerCopyright' => 'Copyright 2025 © - MegaLink - Todos os direitos reservados',
    'footerTermsUrl' => '#termos',
    'footerPrivacyUrl' => '#privacidade'
];

// Mock de Menus
$menus = [
    ['id' => 1, 'title' => 'Início', 'link' => 'index', 'children' => []],
    ['id' => 2, 'title' => 'Planos', 'link' => '#planos', 'children' => []],
    ['id' => 3, 'title' => 'Aplicativo', 'link' => '#app', 'children' => []],
];
?>