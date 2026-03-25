<?php
// Mock Data for Services
$services = [
    [
        'id' => 1,
        'title' => 'MegaLink 5G',
        'description' => 'O futuro da conexão móvel agora disponível para você com a qualidade MegaLink.'
    ],
    [
        'id' => 2,
        'title' => 'Mega Music',
        'description' => 'Acesso ilimitado a milhares de músicas e playlists exclusivas para clientes MegaLink.'
    ],
    [
        'id' => 3,
        'title' => 'Mega Play',
        'description' => 'Assista a filmes e séries com a melhor qualidade de streaming.'
    ],
    [
        'id' => 4,
        'title' => 'Conecta +',
        'description' => 'A melhor solução para sua casa inteligente, conectando todos os seus dispositivos com segurança.'
    ]
];

function getServiceIcon($title, $primaryColor = '#2323FA', $accentColor = '#10B981')
{
    if (strpos($title, '5G') !== false) {
        return '
        <svg class="w-20 h-20" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="40" fill="#E6F0FF" opacity="0.6"/>
          <rect x="28" y="35" width="44" height="32" rx="3" fill="' . $primaryColor . '"/>
          <rect x="32" y="38" width="12" height="12" rx="1" fill="#FFD700"/>
          <rect x="48" y="38" width="12" height="12" rx="1" fill="#FFD700"/>
          <text x="50" y="78" fontSize="10" fontWeight="bold" fill="' . $primaryColor . '" textAnchor="middle">5G</text>
        </svg>';
    }
    if (strpos($title, 'Music') !== false) {
        return '
        <svg class="w-20 h-20" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="40" fill="#E6F0FF" opacity="0.6"/>
          <rect x="28" y="35" width="44" height="32" rx="3" fill="' . $primaryColor . '"/>
          <circle cx="50" cy="51" r="6" fill="#FFD700"/>
          <rect x="47" y="48" width="6" height="8" rx="1" fill="' . $primaryColor . '"/>
          <circle cx="40" cy="51" r="3" fill="' . $primaryColor . '"/>
          <circle cx="60" cy="51" r="3" fill="' . $primaryColor . '"/>
        </svg>';
    }
    if (strpos($title, 'Play') !== false) {
        return '
        <svg class="w-20 h-20" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="40" fill="#E6F0FF" opacity="0.6"/>
          <rect x="25" y="30" width="50" height="38" rx="3" fill="' . $primaryColor . '"/>
          <rect x="30" y="35" width="40" height="28" rx="2" fill="' . $primaryColor . '"/>
          <circle cx="50" cy="49" r="10" fill="#FFD700"/>
          <path d="M46 44 L46 54 L54 49 Z" fill="' . $primaryColor . '"/>
        </svg>';
    }
    if (strpos($title, 'Conecta') !== false) {
        return '
        <svg class="w-20 h-20" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="40" fill="#E6F0FF" opacity="0.6"/>
          <rect x="28" y="40" width="44" height="28" rx="3" fill="' . $primaryColor . '"/>
          <rect x="32" y="30" width="2.5" height="12" rx="1" fill="' . $primaryColor . '"/>
          <rect x="38" y="30" width="2.5" height="12" rx="1" fill="' . $primaryColor . '"/>
          <rect x="44" y="30" width="2.5" height="12" rx="1" fill="' . $primaryColor . '"/>
          <rect x="50" y="30" width="2.5" height="12" rx="1" fill="' . $primaryColor . '"/>
          <rect x="56" y="30" width="2.5" height="12" rx="1" fill="' . $primaryColor . '"/>
          <circle cx="35" cy="52" r="2.5" fill="' . $accentColor . '"/>
          <circle cx="43" cy="52" r="2.5" fill="' . $accentColor . '"/>
          <circle cx="57" cy="52" r="2.5" fill="' . $accentColor . '"/>
          <circle cx="65" cy="52" r="2.5" fill="' . $accentColor . '"/>
          <circle cx="50" cy="62" r="4" fill="#DC2626"/>
          <line x1="48" y1="62" x2="52" y2="62" stroke="white" strokeWidth="1.5" strokeLinecap="round"/>
        </svg>';
    }
    // Default
    return '
    <svg class="w-20 h-20" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="40" fill="#E6F0FF" opacity="0.6"/>
      <rect x="28" y="35" width="44" height="32" rx="3" fill="' . $primaryColor . '"/>
    </svg>';
}
?>

<section class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Header -->
        <div class="text-center mb-12">
            <h2 class="text-4xl md:text-5xl font-bold mb-4 text-primary">
                Conheça nossos serviços
            </h2>
            <p class="text-gray-600 text-lg">
                A MegaLink tem diversos serviços para você e sua família aproveitar
            </p>
        </div>

        <!-- Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <?php foreach ($services as $service): ?>
                <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition transform hover:-translate-y-1">
                    <!-- Ícone -->
                    <div class="flex justify-center mb-6">
                        <?php echo getServiceIcon($service['title'], '#2323FA', '#10B981'); ?>
                    </div>

                    <!-- Título -->
                    <h3 class="text-xl font-bold text-gray-900 mb-2 text-center">
                        <?php echo $service['title']; ?>
                        <div class="w-12 h-1 mx-auto mt-2 bg-primary"></div>
                    </h3>

                    <!-- Descrição -->
                    <p class="text-gray-600 text-center text-sm">
                        <?php echo $service['description']; ?>
                    </p>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>