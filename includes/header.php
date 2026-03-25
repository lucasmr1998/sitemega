<?php
// Helper para renderizar menu (Estilo Algar Simplificado - Sem Submenus)
function renderMenuItem($menu, $config)
{
    // Detectar página atual para marcar como ativo
    $currentPage = basename($_SERVER['PHP_SELF']);
    $isActive = (isset($menu['link']) && $menu['link'] === $currentPage) || (isset($menu['isActive']) && $menu['isActive']);

    // Estilos
    $baseClass = "px-6 h-full font-bold text-sm uppercase tracking-wide transition flex items-center gap-1 focus:outline-none";
    
    if ($isActive) {
        // Active: Fundo Cinza + Borda Laranja + Texto Azul
        $stateClass = "bg-gray-50 border-b-4 border-[#FF6905] text-[#2323FA]";
    } else {
        // Inactive: Texto Cinza -> Hover: Fundo Cinza + Texto Azul
        $stateClass = "text-gray-700 hover:bg-gray-50 hover:text-[#2323FA] border-b-4 border-transparent";
    }

    ?>
    <a href="<?php echo $menu['link']; ?>"
        class="<?php echo $baseClass . ' ' . $stateClass; ?>">
        <?php echo $menu['title']; ?>
    </a>
    <?php
}
?>

<header class="sticky top-0 z-50 shadow-lg bg-white">
    <!-- Barra superior (Tom mais escuro - Estilo Algar)
    <div class="hidden md:block text-white text-xs py-2 bg-[#040470]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">
            <div class="flex items-center space-x-4">
                <span class="opacity-80">Para Você</span>
                <span class="opacity-80">Para Empresas</span>
            </div>
            <div class="flex items-center space-x-4">
                <?php if (!empty($config['areaClienteLink'])): ?>
                    <a href="<?php echo $config['areaClienteLink']; ?>"
                        class="bg-[#2323FA] text-white px-3 py-1 rounded-full hover:bg-[#040470] transition font-semibold text-xs flex items-center gap-2 shadow-sm">
                        <i class="fa-regular fa-user"></i>
                        Área do cliente
                    </a>
                <?php endif; ?>
            </div>
        </div>
    </div>
 -->
    <!-- Header principal (Branco) -->
    <div class="bg-white border-b border-gray-100 relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <a href="index" class="flex items-center gap-2">
                        <?php if (!empty($config['logoUrl'])): ?>
                            <img src="<?php echo $config['logoUrl']; ?>" alt="<?php echo $config['logoAltText']; ?>"
                                class="h-10 w-auto object-contain">
                        <?php else: ?>
                            <!-- Fallback Logo -->
                            <div class="w-10 h-10 bg-[#FF6905] rounded-full flex items-center justify-center text-white">
                                <i class="fa-solid fa-face-smile text-2xl"></i>
                            </div>
                            <span class="text-2xl font-bold text-[#2323FA] tracking-tight">
                                <?php echo $config['companyName']; ?>
                            </span>
                        <?php endif; ?>
                    </a>
                </div>

                <!-- Desktop Navigation -->
                <nav class="hidden lg:flex items-center space-x-0 h-full">
                    <?php foreach ($menus as $menu): ?>
                        <?php renderMenuItem($menu, $config); ?>
                    <?php endforeach; ?>
                </nav>

                <!-- Action Buttons & Mobile Toggle -->
                <div class="flex items-center space-x-4">
                    <!-- Search hidden on smaller desktop if needed -->
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
        <div id="mobile-menu" class="lg:hidden py-4 border-t border-gray-100 hidden absolute w-full bg-white shadow-xl z-50 left-0 top-full">
            <nav class="flex flex-col">
                <?php foreach ($menus as $menu): ?>
                    <a href="<?php echo $menu['link']; ?>"
                        class="block px-6 py-3 text-gray-700 font-bold uppercase text-sm hover:bg-gray-50 hover:text-[#2323FA] transition border-b border-gray-50 last:border-0">
                        <?php echo $menu['title']; ?>
                    </a>
                <?php endforeach; ?>

                <!-- Mobile Actions -->
                <div class="px-6 py-4 bg-gray-50 mt-2 space-y-3">
                    <?php if ($config['assineJaEnabled']): ?>
                        <a href="<?php echo $config['assineJaLink']; ?>"
                            class="block text-center w-full bg-[#FF6905] text-white font-bold py-2 rounded-lg">Assine já</a>
                    <?php endif; ?>
                    <?php if ($config['areaClienteEnabled']): ?>
                        <a href="<?php echo $config['areaClienteLink']; ?>"
                            class="block text-center w-full border border-[#2323FA] text-[#2323FA] font-bold py-2 rounded-lg">Área
                            do cliente</a>
                    <?php endif; ?>
                </div>
            </nav>
        </div>
    </div>
</header>


