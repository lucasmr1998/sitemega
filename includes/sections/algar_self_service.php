<?php
$services = [
    ['icon' => 'fa-file-invoice-dollar', 'label' => '2ª via da fatura'],
    ['icon' => 'fa-barcode', 'label' => 'Código de barras'],
    ['icon' => 'fa-wifi', 'label' => 'Alterar senha Wi-Fi'],
    ['icon' => 'fa-calendar-check', 'label' => 'Agendar visita'],
    ['icon' => 'fa-user-gear', 'label' => 'Meus dados'],
    ['icon' => 'fa-video', 'label' => 'Serviços de Streaming'],
    ['icon' => 'fa-phone-volume', 'label' => 'Fale Conosco'],
    ['icon' => 'fa-store', 'label' => 'Lojas Fisicas'],
];
?>

<section id="autoatendimento" class="py-16 bg-[#2323FA]"> <!-- Blue Background -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-white mb-12">Autoatendimento</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <?php foreach ($services as $service): ?>
                <a href="#"
                    class="bg-white rounded-xl p-8 flex flex-col items-center justify-center hover:bg-gray-50 hover:scale-[1.02] transition-all duration-300 gap-4 group shadow-md cursor-pointer h-40">
                    <i
                        class="fa-solid <?php echo $service['icon']; ?> text-4xl text-[#FF6905] group-hover:text-[#2323FA] transition-colors duration-300"></i>
                    <span
                        class="text-[#2323FA] font-bold text-center text-sm md:text-base group-hover:text-[#040470] transition-colors"><?php echo $service['label']; ?></span>
                </a>
            <?php endforeach; ?>
        </div>
    </div>
</section>