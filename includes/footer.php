<footer class="bg-gray-900 text-gray-400 font-sans text-sm">
    <!-- Main Footer Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">

            <!-- Column 1: Sobre nós -->
            <div>
                <h3 class="text-white font-bold mb-6 text-base">Sobre nós</h3>
                <ul class="space-y-4">
                    <li><a href="#" class="hover:text-white transition">Sobre nós</a></li>
                    <li><a href="lojas" class="hover:text-white transition">Nossas lojas</a></li>
                </ul>
            </div>

            <!-- Column 2: Cliente -->
            <div>
                <h3 class="text-white font-bold mb-6 text-base">Cliente</h3>
                <ul class="space-y-4">
                    <li><a href="https://central.megalinktelecom.hubsoft.com.br/" class="hover:text-white transition">2ª
                            via de conta</a></li>
                    <li><a href="https://central.megalinktelecom.hubsoft.com.br/"
                            class="hover:text-white transition">Renovação</a></li>
                </ul>
            </div>

            <!-- Column 3: Saiba mais -->
            <div>
                <h3 class="text-white font-bold mb-6 text-base">Saiba mais</h3>
                <ul class="space-y-4">
                    <li><a href="#" class="hover:text-white transition">Transparência</a></li>
                    <li><a href="https://indique.megalinkpiaui.com.br/mega-cliente" target="_blank"
                            class="hover:text-white transition">Indique e Ganhe</a></li>
                </ul>
            </div>

            <!-- Column 4: Redes sociais -->
            <div>
                <h3 class="text-white font-bold mb-6 text-base">Redes sociais</h3>

                <!-- Social Icons -->
                <div class="flex items-center space-x-3 mb-6">
                    <a href="<?php echo $config['facebookUrl']; ?>" target="_blank"
                        class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-[#FF6905] hover:text-white transition text-gray-400">
                        <i class="fa-brands fa-facebook-f"></i>
                    </a>
                    <a href="<?php echo $config['instagramUrl']; ?>" target="_blank"
                        class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-[#FF6905] hover:text-white transition text-gray-400">
                        <i class="fa-brands fa-instagram"></i>
                    </a>
                    <a href="<?php echo $config['linkedinUrl']; ?>" target="_blank"
                        class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-[#FF6905] hover:text-white transition text-gray-400">
                        <i class="fa-brands fa-linkedin-in"></i>
                    </a>
                    <a href="<?php echo $config['youtubeUrl']; ?>" target="_blank"
                        class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-[#FF6905] hover:text-white transition text-gray-400">
                        <i class="fa-brands fa-youtube"></i>
                    </a>
                </div>

                <!-- WhatsApp Button -->
                <a href="<?php echo isset($config['whatsappNumber']) ? 'https://wa.me/' . $config['whatsappNumber'] : '#'; ?>"
                    target="_blank"
                    class="inline-flex items-center justify-center bg-[#FF6905] text-white font-bold rounded-lg px-6 py-3 hover:bg-orange-600 transition w-full md:w-auto">
                    <i class="fa-brands fa-whatsapp text-xl mr-2"></i>
                    WhatsApp
                </a>
            </div>
        </div>
    </div>

    <!-- Bottom Bar -->
    <div class="border-t border-gray-800 bg-gray-900">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-6 md:gap-0">

                <!-- Left: Terms -->
                <div class="flex items-center space-x-4">
                    <a href="#" class="hover:text-white transition">Termos de uso</a>
                    <span class="text-gray-600">|</span>
                    <a href="#" class="hover:text-white transition">Política de Privacidade</a>
                </div>

                <!-- Center: Logo -->
                <div class="flex-shrink-0">
                    <img src="assets/img/logo-megalink.png" alt="MegaLink"
                        class="h-8 md:h-10 opacity-80 hover:opacity-100 transition">
                </div>

                <!-- Right: Copyright -->
                <div class="text-right">
                    <p class="text-gray-500 text-xs">
                        &copy; 2025 MegaLink. Todos os direitos reservados.
                    </p>
                </div>

            </div>
        </div>
    </div>
</footer>