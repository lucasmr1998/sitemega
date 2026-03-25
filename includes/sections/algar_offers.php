<?php
// Mock Data for Offers (Matching user screenshot/standard)
$algarOffersStandard = [
    [
        'id' => 1,
        'categoryLabel' => 'Residencial',
        'speedValue' => '320',
        'speedUnit' => 'MEGA',
        'currentPrice' => '89,90',
        'period' => '/mês',
        'features' => [
            'Download até 320 Mbps',
            'Upload simétrico',
            'Suporte 24h'
        ],
        'showBadge' => false,
        'buttonText' => 'Contratar Agora',
        'buttonLink' => 'https://api.whatsapp.com/send?phone=558922210068',
    ],
    [
        'id' => 2,
        'categoryLabel' => 'Melhor Custo-Benefício',
        'speedValue' => '620',
        'speedUnit' => 'MEGA',
        'currentPrice' => '99,90',
        'period' => '/mês',
        'features' => [
            'Download até 620 Mbps',
            'Upload simétrico',
            'Suporte prioritário'
        ],
        'showBadge' => true,
        'badgeText' => 'Mais Popular',
        'badgeBgColor' => '#FF6905',
        'badgeTextColor' => '#FFFFFF',
        'buttonText' => 'Contratar Agora',
        'buttonLink' => 'https://api.whatsapp.com/send?phone=558922210068',
    ],
    [
        'id' => 3,
        'categoryLabel' => 'Alta Performance',
        'speedValue' => '1',
        'speedUnit' => 'GB',
        'currentPrice' => '129,90',
        'period' => '/mês',
        'features' => [
            'Download até 1 Gbps',
            'Upload simétrico',
            'Wi-Fi 6 Pro',
            'Suporte VIP 24h'
        ],
        'showBadge' => true,
        'badgeText' => 'Premium',
        'badgeBgColor' => '#FFD700', // Gold Badge
        'badgeTextColor' => '#000000',
        'buttonText' => 'Contratar Agora',
        'buttonLink' => 'https://api.whatsapp.com/send?phone=558922210068',
    ]
];

// Configuration Defaults (Standard Colors matching Screenshot)
$algarOffersConfig = [
    'titleColor' => '#2323FA',    // Blue Titles
    'underlineColor' => '#FF6905', // Orange Underline
    'buttonBgColor' => '#FF6905', // Orange Button
    'buttonTextColor' => '#FFFFFF',
];
?>

<section id="planos-algar" class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Tab Internet -->
        <div class="flex border-b border-gray-200 mb-12">
            <button class="py-3 px-6 text-lg font-bold border-b-2 text-[#2323FA] border-[#2323FA]">
                Internet
            </button>
        </div>

        <!-- Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <?php foreach ($algarOffersStandard as $offer): ?>
                <div
                    class="relative rounded-2xl shadow-sm border h-full flex flex-col bg-white border-gray-200 hover:shadow-xl transition-shadow duration-300 overflow-visible">

                    <!-- Badge (Pill style on top) -->
                    <?php if ($offer['showBadge']): ?>
                        <div class="absolute -top-3 left-1/2 -translate-x-1/2 text-xs font-bold px-4 py-1 rounded-full z-10 shadow-sm whitespace-nowrap"
                            style="background-color: <?php echo $offer['badgeBgColor']; ?>; color: <?php echo $offer['badgeTextColor']; ?>;">
                            <?php echo $offer['badgeText']; ?>
                        </div>
                    <?php endif; ?>

                    <div class="px-8 pt-8 pb-0 flex flex-col h-full bg-white rounded-t-2xl">
                        <!-- Category with Icon -->
                        <?php if ($offer['categoryLabel']): ?>
                            <div
                                class="flex items-center text-gray-500 text-[10px] uppercase tracking-wider mb-4 font-semibold">
                                <i class="fa-solid fa-wifi w-3 h-3 mr-2"></i> <?php echo $offer['categoryLabel']; ?>
                            </div>
                        <?php endif; ?>

                        <!-- Speed Title -->
                        <h3 class="text-4xl font-extrabold mb-4"
                            style="color: <?php echo $algarOffersConfig['titleColor']; ?>">
                            <div class="flex items-baseline leading-none">
                                <span><?php echo $offer['speedValue']; ?></span>
                                <span class="text-2xl ml-1"><?php echo $offer['speedUnit']; ?></span>
                            </div>
                            <!-- Orange Underline -->
                            <div class="w-12 h-1 mt-3 rounded-full"
                                style="background-color: <?php echo $algarOffersConfig['underlineColor']; ?>">
                            </div>
                        </h3>

                        <!-- Features List -->
                        <div class="space-y-3 text-gray-600 text-sm mb-6 mt-2">
                            <?php foreach ($offer['features'] as $feature): ?>
                                <div class="flex items-center">
                                    <i class="fa-solid fa-check w-4 h-4 mr-3"
                                        style="color: <?php echo $algarOffersConfig['titleColor']; ?>;"></i>
                                    <span><?php echo $feature; ?></span>
                                </div>
                            <?php endforeach; ?>
                        </div>

                        <!-- Price -->
                        <div class="mb-6 mt-auto">
                            <div class="flex items-end gap-1">
                                <span class="text-xl font-bold text-gray-900 mb-1">R$</span>
                                <span
                                    class="text-4xl font-extrabold text-gray-900 leading-none"><?php echo $offer['currentPrice']; ?></span>
                                <span class="text-gray-500 text-sm mb-1 font-medium"><?php echo $offer['period']; ?></span>
                            </div>
                        </div>
                    </div>

                    <!-- Full Width Button -->
                    <div class="mt-auto">
                        <a href="<?php echo $offer['buttonLink']; ?>"
                            class="w-full py-4 font-bold text-lg text-center rounded-b-2xl block hover:opacity-90 transition"
                            style="background-color: <?php echo $algarOffersConfig['buttonBgColor']; ?>; color: <?php echo $algarOffersConfig['buttonTextColor']; ?>;">
                            <?php echo $offer['buttonText']; ?>
                        </a>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>