<?php
// Offers Data (Updated to match standard design request)
$offers = [
    [
        'id' => 1,
        'categoryLabel' => 'INTERNET',
        'speedValue' => '320',
        'speedUnit' => 'MEGA',
        'currentPrice' => '89,90',
        'oldPrice' => '117,90',
        'period' => '/mês',
        'features' => [
            'Instalação Grátis',
            '100% fibra óptica',
            'WI-FI de alta performance',
            '1 Dispositivo Cabeado',
            'Suporte 24h',
            'Download 320Mbps',
            'Upload 320Mbps'
        ],
        'showBadge' => false,
        'buttonText' => 'Aproveitar Oferta',
        'buttonLink' => 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+320MB',
    ],
    [
        'id' => 2,
        'categoryLabel' => 'INTERNET',
        'speedValue' => '620',
        'speedUnit' => 'MEGA',
        'currentPrice' => '99,90',
        'oldPrice' => '137,90',
        'period' => '/mês',
        'features' => [
            'Instalação Grátis',
            '100% fibra óptica',
            'WI-FI de alta performance',
            '1 Dispositivo Cabeado',
            'Suporte 24h',
            'Download 620Mbps',
            'Upload 620Mbps'
        ],
        'showBadge' => true,
        'badgeText' => 'MELHOR OFERTA',
        'badgeBgColor' => '#2323FA', // Blue Badge based on screenshot
        'badgeTextColor' => '#FFFFFF',
        'buttonText' => 'Aproveitar Oferta',
        'buttonLink' => 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+620MB',
    ],
    [
        'id' => 3,
        'categoryLabel' => 'INTERNET',
        'speedValue' => '1',
        'speedUnit' => 'GIGA',
        'currentPrice' => '129,90',
        'oldPrice' => '167,90',
        'period' => '/mês',
        'features' => [
            'Instalação grátis',
            '100% fibra óptica',
            'WI-FI de alta performance',
            '1 Dispositivo Cabeado',
            'Suporte 24h',
            'Download 1000Mbps',
            'Upload 1000Mbps'
        ],
        'showBadge' => false,
        'buttonText' => 'Aproveitar Oferta',
        'buttonLink' => 'https://api.whatsapp.com/send/?phone=558922210068&text=Ol%C3%A1%2C+vim+pelo+site%2C+gostaria+de+contratar+o+plano+de+1GB',
    ]
];

// Config for standard offers colors
$offersConfig = [
    'titleColor' => '#2323FA',     // Blue Titles
    'speedColor' => '#2323FA',     // Blue Speed Text
    'underlineColor' => '#FF6905', // Orange Underline
    'buttonBgColor' => '#FF6905',  // Orange Button
    'buttonTextColor' => '#FFFFFF',
];
?>

<section id="planos" class="py-16 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Tab Indicator (Optional, keeping consistent) -->
        <div class="flex border-b border-gray-200 mb-12">
            <button class="py-3 px-6 text-lg font-bold border-b-2 border-blue-800 text-blue-800">
                <!-- Using hardcoded classes to match screenshot dark blue line roughly or config -->
                 Internet
            </button>
        </div>

        <!-- Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <?php foreach ($offers as $offer): ?>
                <div class="relative rounded-2xl shadow-sm border h-full flex flex-col bg-white border-gray-200 hover:shadow-xl transition-shadow duration-300 overflow-visible group">

                    <!-- Badge -->
                    <?php if ($offer['showBadge']): ?>
                        <div class="absolute -top-4 left-1/2 -translate-x-1/2 text-xs font-bold px-6 py-2 rounded-full z-10 shadow-md whitespace-nowrap uppercase tracking-wide"
                            style="background-color: <?php echo $offer['badgeBgColor']; ?>; color: <?php echo $offer['badgeTextColor']; ?>;">
                            <?php echo $offer['badgeText']; ?>
                        </div>
                    <?php endif; ?>

                    <div class="px-8 pt-10 pb-4 flex flex-col h-full bg-white rounded-t-2xl relative">
                         <!-- Decoration Top Border if standard logic needed, but white card implies clean -->
                        
                        <!-- Header Category -->
                        <div class="flex items-center text-gray-500 text-[11px] uppercase tracking-widest mb-2 font-medium">
                            <i class="fa-solid fa-wifi w-3 h-3 mr-2"></i> <?php echo $offer['categoryLabel']; ?>
                        </div>

                        <!-- Speed Info -->
                        <div class="mb-4">
                            <div class="flex items-baseline leading-none font-extrabold" style="color: <?php echo $offersConfig['speedColor']; ?>">
                                <span class="text-5xl"><?php echo $offer['speedValue']; ?></span>
                                <span class="text-2xl ml-1"><?php echo $offer['speedUnit']; ?></span>
                            </div>
                            <!-- Orange Underline -->
                            <div class="w-10 h-1 mt-4 rounded-full" style="background-color: <?php echo $offersConfig['underlineColor']; ?>"></div>
                        </div>

                        <!-- Features List -->
                        <ul class="space-y-3 mb-8 mt-4">
                            <?php foreach ($offer['features'] as $feature): ?>
                                <li class="flex items-center text-sm text-gray-600">
                                    <!-- Icon Logic -->
                                    <?php if(strpos($feature, 'Download') !== false): ?>
                                         <i class="fa-solid fa-download text-[#2323FA] mr-3 text-xs"></i>
                                    <?php elseif(strpos($feature, 'Upload') !== false): ?>
                                         <i class="fa-solid fa-upload text-[#2323FA] mr-3 text-xs"></i>
                                    <?php else: ?>
                                         <span class="w-1.5 h-1.5 rounded-full bg-[#2323FA] mr-3 flex-shrink-0"></span> <!-- Blue Dot -->
                                    <?php endif; ?>
                                    
                                    <div class="flex-1">
                                        <span class="leading-relaxed"><?php echo $feature; ?></span>
                                    </div>
                                </li>
                            <?php endforeach; ?>
                        </ul>

                        <!-- Price Section -->
                        <div class="mt-auto mb-6">
                            <?php if($offer['oldPrice']): ?>
                                <div class="text-xs text-gray-400 line-through mb-1">de R$ <?php echo $offer['oldPrice']; ?></div>
                            <?php endif; ?>
                            
                            <div class="flex items-end gap-1 text-gray-900">
                                <span class="text-xl font-bold mb-1">R$</span>
                                <span class="text-4xl font-extrabold leading-none"><?php echo explode(',', $offer['currentPrice'])[0]; ?>,<small class="text-2xl"><?php echo explode(',', $offer['currentPrice'])[1]; ?></small></span>
                                <span class="text-gray-500 text-sm mb-1 font-medium"><?php echo $offer['period']; ?></span>
                            </div>
                        </div>
                    </div>

                    <!-- Button Area - Full Width Bottom -->
                    <div class="mt-auto">
                        <a href="<?php echo $offer['buttonLink']; ?>"
                            class="w-full py-4 font-bold text-center rounded-b-2xl block hover:opacity-90 transition text-white uppercase text-sm tracking-wide"
                            style="background-color: <?php echo $offersConfig['buttonBgColor']; ?>;">
                            <?php echo $offer['buttonText']; ?>
                        </a>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>