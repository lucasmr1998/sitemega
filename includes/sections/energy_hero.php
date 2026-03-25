<section class="relative bg-[#2323FA] text-white py-16 md:py-24 overflow-hidden">
    <!-- Background Image Mockup (Overlay) -->
    <div class="absolute inset-0 z-0">
        <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=2070&auto=format&fit=crop"
            class="w-full h-full object-cover opacity-30 object-center" alt="Background Energy">
    </div>

    <div
        class="absolute right-0 top-0 w-1/2 h-full bg-gradient-to-l from-[#0000C6] to-transparent opacity-50 blur-3xl rounded-full transform translate-x-1/2 -translate-y-1/2">
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-12">

            <!-- Left Text -->
            <div class="w-full lg:w-1/2 text-white">
                <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold leading-tight mb-6">
                    Economize até <span class="text-white">20%</span> na sua conta de energia
                </h1>
                <p class="text-lg md:text-xl text-gray-300 mb-8 max-w-lg">
                    Sem taxas, sem custo de adesão e sem instalação de placas solares.
                </p>

                <!-- Trust Badges (Optional based on print style) -->
                <div class="flex items-center gap-4 text-sm text-blue-200">
                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-white"></i> Sem fidelidade
                    </div>
                    <div class="flex items-center gap-2">
                        <i class="fa-solid fa-check text-white"></i> 100% Digital
                    </div>
                </div>
            </div>

            <!-- Right Form Card -->
            <div class="w-full lg:w-1/3">
                <div class="bg-white rounded-2xl shadow-2xl p-6 md:p-8">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">Informe seus dados para contato</h3>
                    <p class="text-sm text-gray-500 mb-6">Fale com um de nossos especialistas.</p>

                    <form action="#" class="space-y-4" id="leadFormEnergy">
                        <div>
                            <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">Nome
                                Completo</label>
                            <input type="text" name="nome"
                                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition"
                                placeholder="João da Silva">
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">E-mail</label>
                            <input type="email" name="email"
                                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition"
                                placeholder="nome@exemplo.com">
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">Celular</label>
                                <input type="tel" name="celular"
                                    class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition"
                                    placeholder="(00) 00000-0000">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">CEP</label>
                                <input type="text" name="cep"
                                    class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition"
                                    placeholder="00000-000">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-gray-700 uppercase mb-1">Qual sua média de
                                conta de energia?</label>
                            <select name="media_conta"
                                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-[#2323FA] focus:border-[#2323FA] outline-none transition appearance-none bg-white">
                                <option>Selecione uma faixa</option>
                                <option>Abaixo de R$ 200</option>
                                <option>Entre R$ 200 e R$ 500</option>
                                <option>Acima de R$ 500</option>
                            </select>
                        </div>

                        <button type="submit"
                            class="w-full bg-[#2323FA] text-white font-bold py-3 rounded-lg hover:bg-blue-700 transition shadow-lg mt-4">
                            Enviar
                        </button>

                        <p class="text-[10px] text-gray-400 text-center mt-4 leading-tight">
                            Ao clicar em enviar você concorda com nossa <a href="#"
                                class="underline hover:text-[#2323FA]">Política de Privacidade</a>.
                        </p>
                    </form>
                </div>


            </div>

        </div>
    </div>
</section>