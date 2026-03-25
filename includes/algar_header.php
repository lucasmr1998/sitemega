<?php
// Helper para renderizar menu (Algar Style - Mega Menu Support)
function renderAlgarMenuItem($menu)
{
    // Mega Menu Layout
    if (isset($menu['isMegaMenu']) && $menu['isMegaMenu']) {
        $activeClass = isset($menu['isActive']) && $menu['isActive']
            ? 'border-b-4 border-[#FF6905] text-[#2323FA] bg-gray-50'
            : 'text-gray-700 hover:text-[#2323FA]';
        ?>
        <div class="group h-full flex items-center">
            <button
                class="<?php echo $activeClass; ?> px-4 h-full font-bold text-sm uppercase tracking-wide transition flex items-center gap-1 focus:outline-none">
                <?php echo $menu['title']; ?>
                <i
                    class="fa-solid fa-chevron-up text-[10px] ml-1 hidden group-hover:block transition-transform duration-300"></i>
                <i class="fa-solid fa-chevron-down text-[10px] ml-1 group-hover:hidden transition-transform duration-300"></i>
            </button>

            <!-- Full Width Mega Dropdown -->
            <div
                class="absolute top-full left-0 w-full bg-[#040470] shadow-2xl border-t border-[#FF6905] hidden group-hover:block z-50 text-white py-8 transition-opacity duration-300">
                <!-- Using a distinct dark green-ish bg (#004740) or dark blue to match requested 'structure'.
                  User screenshot had Green (#00A98F or darker). I will use a Dark Teal/Green to resemble the screenshot
                  but keeping it compatible. Or better: use Config Primary Dark Color?
                  User said "mesma estrutura, textos da algar". The print has a green background.
                  I'll use a deep teal/green to match the print for the dropdown background as requested by "mesma estrutura".
                  Or stick safely to primaryDark (#040470). Let's stick to Primary Dark Blue (#040470) to allow branding consistency.
              -->
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <?php
                    $colCount = count($menu['columns']);
                    $gridClass = $colCount > 3 ? 'md:grid-cols-4' : 'md:grid-cols-3';
                    ?>
                    <div class="grid grid-cols-1 <?php echo $gridClass; ?> gap-8">
                        <?php foreach ($menu['columns'] as $column): ?>
                            <div>
                                <h4 class="font-bold text-lg mb-4 text-white border-b border-white/20 pb-2">
                                    <?php echo $column['title']; ?>
                                </h4>
                                <ul class="space-y-3">
                                    <?php foreach ($column['items'] as $item): ?>
                                        <li>
                                            <a href="<?php echo $item['link']; ?>"
                                                class="block text-sm text-gray-200 hover:text-white hover:translate-x-1 transition duration-200">
                                                <?php echo $item['title']; ?>
                                            </a>
                                        </li>
                                    <?php endforeach; ?>
                                </ul>
                            </div>
                        <?php endforeach; ?>
                    </div>
                </div>
            </div>
        </div>
        <?php
    } elseif (!empty($menu['children'])) {
        // Standard Dropdown (Atendimento, Mais)
        ?>
        <div class="relative group h-full flex items-center">
            <button class="text-gray-700 font-semibold px-4 h-full transition flex items-center hover:text-[#2323FA]">
                <?php echo $menu['title']; ?>
                <i class="fa-solid fa-chevron-down ml-1 text-xs"></i>
            </button>
            <div
                class="absolute top-full left-0 mt-0 w-48 bg-white rounded-b-lg shadow-lg border-t border-[#FF6905] py-2 hidden group-hover:block z-50">
                <?php foreach ($menu['children'] as $child): ?>
                    <a href="<?php echo $child['link']; ?>"
                        class="block px-4 py-2 text-gray-700 hover:bg-gray-50 hover:text-[#2323FA] transition">
                        <?php echo $child['title']; ?>
                    </a>
                <?php endforeach; ?>
            </div>
        </div>
        <?php
    } else {
        // Simple Link
        ?>
        <a href="<?php echo $menu['link']; ?>"
            class="text-gray-700 font-semibold px-4 transition hover:text-[#2323FA] h-full flex items-center">
            <?php echo $menu['title']; ?>
        </a>
        <?php
    }
}
?>

<header class="sticky top-0 z-50 shadow-lg bg-white">
    <!-- Barra superior (Tom mais escuro) -->
    <div class="hidden md:block text-white text-xs py-2 bg-[#040470]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
            <div class="flex items-center space-x-4">
                <span class="opacity-80">Para Você</span>
                <span class="opacity-80">Para Empresas</span>
            </div>
            <div class="flex items-center space-x-4">
                <a href="<?php echo $config['areaClienteLink']; ?>"
                    class="bg-[#2323FA] text-white px-3 py-1 rounded-full hover:bg-[#040470] transition font-semibold text-xs flex items-center gap-2 shadow-sm">
                    <i class="fa-regular fa-user"></i>
                    Área do cliente
                </a>
            </div>
        </div>
    </div>

    <!-- Header principal (Branco) -->
    <div class="bg-white border-b border-gray-100 relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="algar" class="flex items-center gap-2">
                        <?php if ($config['logoUrl']): ?>
                            <img src="<?php echo $config['logoUrl']; ?>" alt="<?php echo $config['logoAltText']; ?>"
                                class="h-10 w-auto object-contain">
                        <?php else: ?>
                            <!-- Fallback Logo -->
                            <div
                                class="w-10 h-10 bg-[#FF6905] rounded-full flex items-center justify-center text-white">
                                <i class="fa-solid fa-face-smile text-2xl"></i>
                            </div>
                            <span class="text-2xl font-bold text-[#2323FA] tracking-tight">
                                Mega<span class="font-light">Link</span>
                            </span>
                        <?php endif; ?>
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-0 h-full">
                    <!-- space-x-0 because padding is on items -->
                    <?php foreach ($menus as $menu): ?>
                        <?php renderAlgarMenuItem($menu); ?>
                    <?php endforeach; ?>
                </nav>

                <!-- Action Buttons & Mobile Toggle -->
                <div class="flex items-center space-x-4">
                    <!-- Search hidden on smaller desktop if needed, but keeping generally -->
                    <a href="#" class="hidden lg:flex text-gray-700 hover:text-[#2323FA] font-medium items-center">
                        <i class="fa-solid fa-magnifying-glass mr-1"></i>
                    </a>

                    <button id="mobile-menu-btn" class="lg:hidden text-2xl text-[#2323FA] cursor-pointer relative z-50">
                        <i class="fa-solid fa-bars cursor-pointer"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu (Hidden by default) -->
        <div id="mobile-menu" class="lg:hidden py-4 border-t border-gray-100 hidden absolute w-full bg-white shadow-xl left-0 top-full z-50">
            <nav class="flex flex-col h-[calc(100vh-80px)] overflow-y-auto pb-20">
                <?php foreach ($menus as $menu): ?>
                    <?php if ((isset($menu['isMegaMenu']) && $menu['isMegaMenu']) || !empty($menu['children'])): ?>
                        <!-- Submenu Item -->
                        <div>
                            <button
                                class="mobile-submenu-toggle w-full flex justify-between items-center px-6 py-3 text-gray-700 font-bold uppercase text-sm hover:bg-gray-50 hover:text-[#2323FA] transition border-b border-gray-50">
                                <?php echo $menu['title']; ?>
                                <i class="fa-solid fa-chevron-down text-xs transition-transform duration-200"></i>
                            </button>

                            <!-- Submenu Content -->
                            <div class="hidden bg-gray-50">
                                <?php
                                $items = [];
                                if (isset($menu['columns'])) {
                                    // Flatten Mega Menu
                                    foreach ($menu['columns'] as $col) {
                                        // Optional: Add Column Title?
                                        // $items[] = ['type' => 'header', 'title' => $col['title']];
                                        foreach ($col['items'] as $item) $items[] = $item;
                                    }
                                } elseif (isset($menu['children'])) {
                                    $items = $menu['children'];
                                }
                                ?>

                                <?php foreach ($items as $item): ?>
                                    <a href="<?php echo $item['link']; ?>" class="block px-8 py-3 text-gray-600 text-sm hover:text-[#2323FA] border-b border-gray-100 last:border-0 pl-10">
                                        <?php echo $item['title']; ?>
                                    </a>
                                <?php endforeach; ?>
                            </div>
                        </div>
                    <?php else: ?>
                        <!-- Simple Link -->
                        <a href="<?php echo $menu['link']; ?>"
                            class="block px-6 py-3 text-gray-700 font-bold uppercase text-sm hover:bg-gray-50 hover:text-[#2323FA] transition border-b border-gray-50 last:border-0">
                            <?php echo $menu['title']; ?>
                        </a>
                    <?php endif; ?>
                <?php endforeach; ?>

                <!-- Mobile Actions -->
                <div class="px-6 py-4 mt-2 space-y-3">
                    <?php if ($config['areaClienteEnabled']): ?>
                        <a href="<?php echo $config['areaClienteLink']; ?>"
                            class="block text-center w-full border border-[#2323FA] text-[#2323FA] font-bold py-3 rounded-lg hover:bg-[#2323FA] hover:text-white transition">
                            <i class="fa-regular fa-user mr-2"></i>
                            Área do cliente
                        </a>
                    <?php endif; ?>
                </div>
            </nav>
        </div>
    </div>
</header>

</script>

