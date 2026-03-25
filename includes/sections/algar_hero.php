<?php
// Banner Slides (Full Width - Image Only)
$slides = [
    // 'assets/img/SUPER BANNER SITE 02.png',
    'assets/img/SUPER BANNER SITE 04.png'
];
?>

<section class="relative bg-white overflow-hidden">
    <!-- Carousel Container -->
    <div id="heroCarousel" class="relative w-full group">
        <!-- Removed fixed height (h-[500px]) to allow image to dictate height (h-auto) -->

        <!-- Wrapper for slides to maintain aspect ratio logic if needed, but for h-auto we just stack them. 
             However, absolute positioning requires a height on parent. 
             If we want responsive height based on image, we can't easily use absolute for all slides without JS setting height or aspect-ratio hack.
             Simplest approach for responsive banner: 
             Render first slide relatively (to set height) and others absolutely? 
             Or just use a standard aspect-ratio tailored to the image. 
             Given I don't know the exact ratio, I'll rely on the first image setting the container height if I make it relative?
             No, visual stacking requires absolute.
             Let's try: Parent relative. All items absolute EXCEPT active? NO, that jumps layout.
             Better: Parent `aspect-[21/9]` or similar? No.
             
             Let's use a JS approach to set height or just standard CSS Grid stacking?
             Grid area 1/1 for all items is the modern CSS way to stack overlapping items without absolute height issues.
        -->

        <div class="grid grid-cols-1 grid-rows-1">
            <?php foreach ($slides as $index => $slide): ?>
                <div class="carousel-item col-start-1 row-start-1 transition-opacity duration-1000 ease-in-out <?php echo $index === 0 ? 'opacity-100 z-10' : 'opacity-0 z-0'; ?>"
                    data-index="<?php echo $index; ?>">
                    <!-- Full Width Image, Auto Height -->
                    <img src="<?php echo $slide; ?>" alt="Banner MegaLink" class="w-full h-auto object-cover">
                </div>
            <?php endforeach; ?>
        </div>

        <!-- Controls -->
        <div class="absolute bottom-4 left-0 right-0 flex justify-center gap-3 z-20">
            <?php foreach ($slides as $index => $slide): ?>
                <button
                    class="w-3 h-3 rounded-full bg-white/50 hover:bg-white transition shadow-sm carousel-dot <?php echo $index === 0 ? 'bg-white' : ''; ?>"
                    onclick="switchSlide(<?php echo $index; ?>)"></button>
            <?php endforeach; ?>
        </div>
    </div>
</section>

<script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.carousel-item');
    const dots = document.querySelectorAll('.carousel-dot');
    const totalSlides = slides.length;

    function switchSlide(index) {
        // Reset
        slides.forEach(slide => {
            slide.classList.remove('opacity-100', 'z-10');
            slide.classList.add('opacity-0', 'z-0');
        });
        dots.forEach(dot => dot.classList.remove('bg-white'));
        dots.forEach(dot => dot.classList.add('bg-white/50'));

        // Activate
        slides[index].classList.remove('opacity-0', 'z-0');
        slides[index].classList.add('opacity-100', 'z-10');
        dots[index].classList.remove('bg-white/50');
        dots[index].classList.add('bg-white');

        currentSlide = index;
    }

    // Auto Advance
    setInterval(() => {
        let next = (currentSlide + 1) % totalSlides;
        switchSlide(next);
    }, 5000);
</script>