<?php
// Mock Data for Hero
$banners = [
    /* Banner removed as per request
    [
        'id' => 1,
        'title' => 'Bem-vindo à MegaLink',
        'imageUrl' => 'assets/img/SUPER BANNER SITE 02.png',
        'link' => '#ofertas' 
    ],
    */
    [
        'id' => 2,
        'title' => 'Internet Fibra Óptica',
        'imageUrl' => 'assets/img/SUPER BANNER SITE 04.png',
        'link' => '#assine'
    ]
];
?>

<section id="hero" class="relative group">
    <!-- Grid Container allows stacking without absolute positioning height collapse -->
    <div class="grid grid-cols-1 grid-rows-1">
        <?php foreach ($banners as $index => $banner): ?>
            <!-- Slide Item -->
            <div 
                class="banner-slide col-start-1 row-start-1 transition-opacity duration-1000 ease-in-out <?php echo $index === 0 ? 'opacity-100 z-10' : 'opacity-0 z-0'; ?>" 
                data-index="<?php echo $index; ?>"
            >
                <a href="<?php echo $banner['link']; ?>" class="block w-full">
                    <!-- Image Tag for natural aspect ratio and full visibility -->
                    <!-- w-full h-auto ensures it fits the width and scales height proportionally -->
                    <img 
                        src="<?php echo $banner['imageUrl']; ?>" 
                        alt="<?php echo $banner['title']; ?>"
                        class="w-full h-auto object-contain block"
                    >
                </a>
            </div>
        <?php endforeach; ?>
    </div>

    <!-- Navigation Arrows -->
    <?php if (count($banners) > 1): ?>
        <button id="hero-prev" class="absolute left-4 top-1/2 -translate-y-1/2 z-30 bg-black/30 hover:bg-black/50 rounded-full p-3 transition text-white">
            <i class="fa-solid fa-chevron-left w-6 h-6 flex items-center justify-center"></i>
        </button>
        <button id="hero-next" class="absolute right-4 top-1/2 -translate-y-1/2 z-30 bg-black/30 hover:bg-black/50 rounded-full p-3 transition text-white">
            <i class="fa-solid fa-chevron-right w-6 h-6 flex items-center justify-center"></i>
        </button>

        <!-- Indicators -->
        <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 z-30 flex items-center gap-2">
            <?php foreach ($banners as $index => $banner): ?>
                <button 
                    class="hero-indicator h-2 rounded-full transition-all shadow-sm <?php echo $index === 0 ? 'w-8 bg-white' : 'w-2 bg-white/50 hover:bg-white/80'; ?>"
                    data-index="<?php echo $index; ?>"
                ></button>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>
</section>