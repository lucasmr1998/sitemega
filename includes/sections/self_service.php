<?php
// Mock Data for Self Service Items matching the screenshot
$selfServiceItems = [
    [
        'id' => 1,
        'title' => '2ª via da fatura',
        'description' => 'Baixe sua fatura através do portal do cliente',
        'icon' => 'fa-solid fa-file-invoice', // Or similar document icon
        'link' => $config['areaClienteLink'] ?? '#',
        'highlight' => true, // Blue card
    ],
    [
        'id' => 2,
        'title' => 'Ligamos para você',
        'description' => 'Informe seus dados que entraremos em contato',
        'icon' => 'fa-solid fa-phone',
        'link' => '#',
        'highlight' => false,
    ],
    [
        'id' => 3,
        'title' => 'Central de ajuda',
        'description' => 'Tudo o que você precisa saber para tirar suas dúvidas',
        'icon' => 'fa-regular fa-circle-question',
        'link' => '#',
        'highlight' => false,
    ],
    [
        'id' => 4,
        'title' => 'Suporte remoto',
        'description' => 'Realizamos o seu atendimento por acesso remoto',
        'icon' => 'fa-solid fa-desktop',
        'link' => '#',
        'highlight' => false,
    ],
    [
        'id' => 5,
        'title' => 'Nossas lojas',
        'description' => 'Verifique as lojas parceiras MegaLink na sua cidade',
        'icon' => 'fa-solid fa-location-dot',
        'link' => '#',
        'highlight' => false,
    ],
    [
        'id' => 6,
        'title' => 'Ouvidoria',
        'description' => 'Nosso canal de ética pronto para resolver',
        'icon' => 'fa-solid fa-headset',
        'link' => '#',
        'highlight' => false,
    ],
];
?>

<section id="autoatendimento" class="py-24 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-4">
                Autoatendimento para clientes
            </h2>
            <p class="text-gray-500 text-lg">
                Resolva suas necessidades de forma rápida e prática
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <?php foreach ($selfServiceItems as $item): ?>
                <?php if ($item['highlight']): ?>
                    <!-- Highlighted Card (Blue) -->
                    <a href="<?php echo $item['link']; ?>"
                        class="bg-[#2323FA] rounded-2xl p-8 transition hover:bg-blue-800 group flex items-start gap-4 shadow-lg hover:shadow-xl">
                        <div class="flex-shrink-0">
                            <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center text-white text-2xl">
                                <i class="<?php echo $item['icon']; ?>"></i>
                            </div>
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <h3 class="text-xl font-bold text-white"><?php echo $item['title']; ?></h3>
                                <i class="fa-solid fa-chevron-right text-white text-sm"></i>
                            </div>
                            <p class="text-blue-100 text-sm leading-relaxed">
                                <?php echo $item['description']; ?>
                            </p>
                        </div>
                    </a>
                <?php else: ?>
                    <!-- Standard Card (Light Gray) -->
                    <a href="<?php echo $item['link']; ?>"
                        class="bg-[#F8F9FA] rounded-2xl p-8 transition hover:bg-[#EEF2FF] group flex items-start gap-4 border border-transparent hover:border-blue-100">
                        <div class="flex-shrink-0">
                            <div
                                class="w-12 h-12 bg-[#E0E7FF] rounded-xl flex items-center justify-center text-[#2323FA] text-2xl group-hover:bg-[#2323FA] group-hover:text-white transition-colors">
                                <i class="<?php echo $item['icon']; ?>"></i>
                            </div>
                        </div>
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <h3 class="text-xl font-bold text-gray-900"><?php echo $item['title']; ?></h3>
                                <i
                                    class="fa-solid fa-chevron-right text-gray-400 group-hover:text-[#2323FA] text-sm transition"></i>
                            </div>
                            <p class="text-gray-500 text-sm leading-relaxed">
                                <?php echo $item['description']; ?>
                            </p>
                        </div>
                    </a>
                <?php endif; ?>
            <?php endforeach; ?>
        </div>
    </div>
</section>