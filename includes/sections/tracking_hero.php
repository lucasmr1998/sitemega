<section class="relative bg-[#2323FA] text-white py-20 lg:py-32 overflow-hidden">
    <!-- Background Image Mockup (Overlay) -->
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=2070&auto=format&fit=crop"
            class="w-full h-full object-cover opacity-20 object-center" alt="Background Tracking">
    </div>

    <div
        class="absolute right-0 top-0 w-1/2 h-full bg-gradient-to-l from-[#0000C6] to-transparent opacity-50 blur-3xl rounded-full transform translate-x-1/2 -translate-y-1/2">
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-12">
            <!-- Text Content -->
            <div class="w-full lg:w-1/2">
                <div
                    class="inline-flex items-center gap-2 bg-[#3B3BFF]/30 border border-white/10 rounded-full px-4 py-1.5 mb-8 backdrop-blur-md shadow-lg">
                    <span class="w-2 h-2 rounded-full bg-white animate-pulse shadow-[0_0_10px_#ffffff]"></span>
                    <span class="text-xs font-bold tracking-widest uppercase text-white">Monitoramento 24h</span>
                </div>

                <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 leading-tight text-white">
                    O controle do seu veículo na palma da sua mão
                </h1>

                <p class="text-lg md:text-xl text-gray-300 mb-8 leading-relaxed max-w-lg">
                    Mais segurança para você e sua família. Localização em tempo real, bloqueio remoto e proteção contra
                    roubo e furto.
                </p>

                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="#contratar"
                        class="inline-flex items-center justify-center bg-white text-[#2323FA] font-bold text-lg py-4 px-8 rounded-full hover:bg-blue-50 transition shadow-lg hover:shadow-white/30 transform hover:-translate-y-1">
                        Quero proteger meu veículo
                        <i class="fa-solid fa-shield-halved ml-2"></i>
                    </a>
                </div>
            </div>

            <!-- Right Form Card -->
            <div class="w-full lg:w-1/3">
                <div class="bg-white rounded-2xl shadow-2xl p-6 md:p-8">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">Proteja seu veículo agora</h3>
                    <p class="text-sm text-gray-500 mb-6">Preencha o formulário e fale com um consultor.</p>

                    <form action="#" class="space-y-4" id="leadFormTracking">
                        <div>
                            <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">Nome
                                Completo</label>
                            <input type="text" name="nome"
                                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#FF6905] focus:border-[#FF6905] outline-none transition text-gray-800"
                                placeholder="Seu nome">
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">E-mail</label>
                            <input type="email" name="email"
                                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition text-gray-800"
                                placeholder="seu@email.com">
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">Celular</label>
                                <input type="tel" name="celular"
                                    class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition text-gray-800"
                                    placeholder="(86) 99999-9999">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">CEP</label>
                                <input type="text" name="cep"
                                    class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition text-gray-800"
                                    placeholder="00000-000">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">Tipo de Veículo</label>
                            <select name="tipo_veiculo"
                                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition appearance-none bg-white text-gray-800">
                                <option>Selecione uma opção</option>
                                <option>Carro de Passeio</option>
                                <option>Motocicleta</option>
                                <option>Caminhão / Frota</option>
                                <option>Outros</option>
                            </select>
                        </div>

                        <button type="submit"
                            class="w-full bg-[#2323FA] text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition shadow-lg mt-4">
                            Solicitar Cotação
                        </button>

                        <p class="text-[10px] text-gray-400 text-center mt-4 leading-tight">
                            Seus dados estão seguros. Ao enviar você aceita nossa <a href="#"
                                class="underline hover:text-[#2323FA]">Política de Privacidade</a>.
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>