<?php
// Mock Data for Combos
$combos = [
    [
        'title' => 'Internet',
        'description' => 'Serviços de internet 100% fibra óptica.',
        'color' => 'bg-[#FF6905]', // Orange
        'icon' => 'fa-wifi'
    ],
    [
        'title' => 'Mega Energia',
        'description' => 'Economia e sustentabilidade para sua residência.',
        'color' => 'bg-[#10B981]', // Green
        'icon' => 'fa-bolt'
    ],
    [
        'title' => 'Mega Segurança',
        'description' => 'Proteção e monitoramento 24h para sua família.',
        'color' => 'bg-[#2323FA]', // Blue
        'icon' => 'fa-shield-halved'
    ]
];
?>

<section class="py-24 bg-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row items-center gap-16 lg:gap-24">

            <!-- Left Content -->
            <div class="w-full lg:w-1/3 text-left">
                <h2 class="text-4xl md:text-5xl font-extrabold text-[#2323FA] leading-tight mb-8">
                    Aproveite nossas ofertas em

                    <br>
                    forma de combo
                </h2>

                <!-- White block placeholder from print or CTA -->
                <a href="#planos"
                    class="inline-block bg-[#FF6905] text-white font-bold text-lg px-10 py-4 rounded-lg hover:shadow-lg transition mt-4">
                    Conhecer as ofertas
                </a>
            </div>

            <!-- Right Content - Cards -->
            <div class="w-full lg:w-2/3">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative">
                    <?php foreach ($combos as $index => $combo): ?>
                        <div class="relative group h-full z-0 hover:z-10 bg-transparent">
                            <!-- Card Container (Removed overflow-hidden from parent) -->
                            <div
                                class="bg-gray-50 rounded-[2rem] shadow-sm h-full flex flex-col transition-transform hover:-translate-y-2 duration-300">

                                <!-- Top Color Block (Rounded Top + Overflow Hidden for watermark) -->
                                <div
                                    class="h-48 <?php echo $combo['color']; ?> relative flex items-center justify-center p-6 rounded-t-[2rem] overflow-hidden">
                                    <!-- Background Icon (Watermark) -->
                                    <i
                                        class="fa-solid <?php echo $combo['icon']; ?> text-white text-8xl absolute opacity-20 transform -rotate-12"></i>
                                    <!-- Main Icon -->
                                    <i
                                        class="fa-solid <?php echo $combo['icon']; ?> text-white text-5xl relative z-10 drop-shadow-sm"></i>
                                </div>

                                <!-- Content Area (Rounded Bottom + Relative for Plus positioning) -->
                                <div class="p-8 flex-1 bg-[#F9FAFB] rounded-b-[2rem] relative">
                                    <h3 class="text-xl font-bold text-gray-900 mb-4"><?php echo $combo['title']; ?></h3>
                                    <p class="text-sm text-gray-500 leading-relaxed font-medium">
                                        <?php echo $combo['description']; ?>
                                    </p>

                                    <!-- Plus Sign (Attached to Content Area) -->
                                    <?php if ($index < count($combos) - 1): ?>
                                        <div
                                            class="hidden md:flex absolute top-1/2 -translate-y-1/2 -right-6 z-20 w-8 h-8 items-center justify-center text-gray-800 text-3xl font-bold">
                                            <i class="fa-solid fa-plus"></i>
                                        </div>
                                    <?php endif; ?>
                                    </div>
                                    </div>
   
                                 <!-- Mobile Plus Sign (Below Card) -->
                                <?php if ($index < count($combos) - 1): ?>
                                        <div class="md:hidden flex justify-center py-4 text-gray-400 text-xl">
                                                <i class="fa-solid fa-plus"></i>
                                            </div>
                                        <?php endif; ?>
                                    </div>
                            <?php endforeach; ?>
                </div>
                    </div>
        
        </div>
    </div>
</section>