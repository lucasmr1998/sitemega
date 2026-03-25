<?php
$phones = [
    ['name' => 'Moto G84', 'brand' => 'MOTOROLA', 'installment' => 'Em até 21x sem juros'],
    ['name' => 'Galaxy S23', 'brand' => 'SAMSUNG', 'installment' => 'Em até 21x sem juros'],
    ['name' => 'iPhone 14', 'brand' => 'APPLE', 'installment' => 'Em até 21x sem juros'],
    ['name' => 'Galaxy A54', 'brand' => 'SAMSUNG', 'installment' => 'Em até 21x sem juros'],
];
?>
<section class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-gray-900 mb-8 text-left">As melhores ofertas de smartphones</h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
            <?php foreach ($phones as $phone): ?>
                <div class="border border-gray-200 rounded-xl p-4 hover:shadow-lg transition duration-300 bg-white">
                    <div class="text-[10px] text-gray-400 font-bold uppercase mb-4 tracking-wider">
                        <?php echo $phone['brand']; ?></div>

                    <!-- Placeholder Image -->
                    <div class="bg-gray-100 rounded-lg h-48 mb-4 flex items-center justify-center text-gray-300">
                        <i class="fa-solid fa-mobile-screen-button text-5xl"></i>
                    </div>

                    <h3 class="text-base font-bold text-gray-900 mb-1"><?php echo $phone['name']; ?></h3>
                    <p class="text-xs text-gray-500 mb-6"><?php echo $phone['installment']; ?></p>

                    <button
                        class="w-full py-2 border border-gray-300 rounded-md text-gray-600 font-bold text-sm hover:border-[#2323FA] hover:text-[#2323FA] transition">
                        Ver detalhes
                    </button>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</section>