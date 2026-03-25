document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = mobileMenuBtn ? mobileMenuBtn.querySelector('i') : null;

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');

            // Toggle Icon
            if (mobileMenu.classList.contains('hidden')) {
                menuIcon.classList.remove('fa-xmark');
                menuIcon.classList.add('fa-bars');
            } else {
                menuIcon.classList.remove('fa-bars');
                menuIcon.classList.add('fa-xmark');
            }
        });
    }

    // Mobile Submenu Toggle
    const submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');

    submenuToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const submenu = toggle.nextElementSibling;
            const icon = toggle.querySelector('i');

            if (submenu) {
                submenu.classList.toggle('hidden');

                // Rotate Chevron
                if (submenu.classList.contains('hidden')) {
                    icon.classList.remove('rotate-180');
                } else {
                    icon.classList.add('rotate-180');
                }
            }
        });
    });

    // Hero Carousel Logic
    const slides = document.querySelectorAll('.banner-slide');
    const heroPrev = document.getElementById('hero-prev');
    const heroNext = document.getElementById('hero-next');
    const indicators = document.querySelectorAll('.hero-indicator');

    if (slides.length > 0) {
        let currentSlide = 0;
        const totalSlides = slides.length;
        let slideInterval;

        const showSlide = (index) => {
            // Handle wrap-around
            if (index >= totalSlides) index = 0;
            if (index < 0) index = totalSlides - 1;

            currentSlide = index;

            // Update Slides
            slides.forEach((slide, i) => {
                if (i === currentSlide) {
                    slide.classList.remove('opacity-0', 'z-0');
                    slide.classList.add('opacity-100', 'z-10');
                } else {
                    slide.classList.remove('opacity-100', 'z-10');
                    slide.classList.add('opacity-0', 'z-0');
                }
            });

            // Update Indicators
            indicators.forEach((ind, i) => {
                if (i === currentSlide) {
                    ind.classList.remove('w-2', 'bg-white/40');
                    ind.classList.add('w-8', 'bg-white');
                } else {
                    ind.classList.remove('w-8', 'bg-white');
                    ind.classList.add('w-2', 'bg-white/40');
                }
            });
        };

        const nextSlide = () => {
            showSlide(currentSlide + 1);
        };

        const prevSlide = () => {
            showSlide(currentSlide - 1);
        };

        // Event Listeners
        if (heroPrev) heroPrev.addEventListener('click', () => {
            prevSlide();
            resetInterval();
        });

        if (heroNext) heroNext.addEventListener('click', () => {
            nextSlide();
            resetInterval();
        });

        indicators.forEach((ind) => {
            ind.addEventListener('click', (e) => {
                const index = parseInt(e.target.dataset.index);
                showSlide(index);
                resetInterval();
            });
        });

        // Auto Play
        const startInterval = () => {
            slideInterval = setInterval(nextSlide, 5000); // 5 seconds
        };

        const resetInterval = () => {
            clearInterval(slideInterval);
            startInterval();
        };

        startInterval();
    }
});
