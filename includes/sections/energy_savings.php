<section class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

        <div class="text-center mb-16">
            <span class="text-[#2323FA] font-bold tracking-wider uppercase text-sm mb-2 block">Inovação Solar</span>
            <h2 class="text-3xl md:text-4xl font-extrabold text-gray-900">Mais economia para você</h2>
            <p class="text-gray-500 mt-2">Sua fatura mais barata, sem obras e sem investimento.</p>
        </div>

        <div class="flex flex-col md:flex-row items-center gap-16">

            <!-- Left Content -->
            <div class="w-full md:w-1/2">
                <span
                    class="inline-block px-3 py-1 bg-blue-100 text-[#2323FA] rounded-full text-xs font-bold mb-4">Solução
                    Inteligente</span>
                <h3 class="text-2xl md:text-3xl font-bold text-gray-900 mb-4">Energia por Assinatura</h3>
                <p class="text-gray-600 mb-6 leading-relaxed">
                    A oportunidade de economizar na conta de luz agora está ao seu alcance. Assine nossa energia
                    renovável e tenha desconto garantido todo mês direto na sua fatura da distribuidora.
                </p>
                <p class="text-gray-600 mb-8 leading-relaxed">
                    Você não precisa instalar placas solares, nem fazer obras no telhado. É tudo digital, simples e com
                    zero fidelidade.
                </p>

                <div class="grid grid-cols-2 gap-4">
                    <div class="flex items-center gap-3">
                        <div
                            class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 flex-shrink-0">
                            <i class="fa-solid fa-check text-xs"></i>
                        </div>
                        <span class="text-sm font-semibold text-gray-800">Sem taxa de adesão</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div
                            class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 flex-shrink-0">
                            <i class="fa-solid fa-check text-xs"></i>
                        </div>
                        <span class="text-sm font-semibold text-gray-800">Sem fidelidade</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div
                            class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 flex-shrink-0">
                            <i class="fa-solid fa-check text-xs"></i>
                        </div>
                        <span class="text-sm font-semibold text-gray-800">Economia garantida</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div
                            class="w-8 h-8 rounded-full bg-green-100 flex items-center justify-center text-green-600 flex-shrink-0">
                            <i class="fa-solid fa-check text-xs"></i>
                        </div>
                        <span class="text-sm font-semibold text-gray-800">Sem instalação</span>
                    </div>
                </div>
            </div>

            <!-- Right Image Mockup -->
            <div class="w-full md:w-1/2">
                <div class="relative bg-white p-8 rounded-3xl shadow-xl border border-gray-100">
                    <div class="mb-6 border-b border-gray-100 pb-4">
                        <span
                            class="inline-block py-1 px-3 rounded-full bg-green-100 text-green-700 text-xs font-semibold mb-2">
                            Simulação Rápida
                        </span>
                        <h4 class="text-2xl font-bold text-gray-900">Quanto você gasta de luz?</h4>
                        <p class="text-gray-500 text-sm">Descubra sua economia em segundos.</p>
                    </div>

                    <div class="space-y-6">
                        <div>
                            <label for="billValueSavings"
                                class="block text-xs font-semibold uppercase text-gray-600 mb-2">
                                Valor médio da conta
                            </label>
                            <div class="relative">
                                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                    <span class="text-gray-500 font-semibold text-lg">R$</span>
                                </div>
                                <input type="number" id="billValueSavings"
                                    class="block w-full pl-12 pr-4 py-3 bg-gray-50 border border-gray-200 rounded-xl text-xl font-bold text-gray-900 focus:ring-2 focus:ring-[#2323FA] focus:border-transparent transition-all outline-none"
                                    placeholder="0,00" value="500" oninput="calculateSavingsSection()">
                            </div>
                        </div>

                        <!-- Results Box -->
                        <div
                            class="bg-gradient-to-br from-[#2323FA] to-blue-700 rounded-2xl p-6 text-white text-center relative overflow-hidden shadow-lg">
                            <div class="relative z-10">
                                <p class="text-blue-100 text-xs font-bold uppercase tracking-wider mb-1">Sua nova
                                    estimativa</p>
                                <div class="text-4xl font-extrabold mb-4" id="newBillDisplaySavings">R$ 400,00</div>

                                <div class="border-t border-white/20 pt-4 grid grid-cols-2 gap-4">
                                    <div>
                                        <p class="text-[10px] text-blue-100 uppercase font-semibold">Economia Mensal
                                        </p>
                                        <p class="font-bold text-lg" id="monthlySavingsDisplaySavings">R$ 100,00</p>
                                    </div>
                                    <div>
                                        <p class="text-[10px] text-white/80 uppercase font-semibold">Economia Anual</p>
                                        <p class="font-bold text-lg text-white" id="yearlySavingsDisplaySavings">R$
                                            1.200,00</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Decor -->
                            <div class="absolute top-0 right-0 -mr-8 -mt-8 w-24 h-24 rounded-full bg-white/10 blur-xl">
                            </div>
                            <div
                                class="absolute bottom-0 left-0 -ml-8 -mb-8 w-24 h-24 rounded-full bg-white/10 blur-xl">
                            </div>
                        </div>

                        <button onclick="window.location.href='#assine'"
                            class="w-full bg-white text-[#2323FA] border-2 border-[#2323FA] font-bold py-3 px-6 rounded-xl hover:bg-blue-50 transition-all shadow-sm flex items-center justify-center gap-2 group transform duration-200">
                            <span>Garantir meu desconto</span>
                            <i
                                class="fa-solid fa-arrow-right text-sm group-hover:translate-x-1 transition-transform"></i>
                        </button>
                    </div>

                    <script>
                        function formatCurrencySavings(value) {
                            return new Intl.NumberFormat('pt-BR', {
                                style: 'currency',
                                currency: 'BRL'
                            }).format(value);
                        }

                        function calculateSavingsSection() {
                            const input = document.getElementById('billValueSavings');
                            const newBillDisplay = document.getElementById('newBillDisplaySavings');
                            const monthlySavingsDisplay = document.getElementById('monthlySavingsDisplaySavings');
                            const yearlySavingsDisplay = document.getElementById('yearlySavingsDisplaySavings');

                            let value = parseFloat(input.value);

                            if (isNaN(value) || value < 0) {
                                value = 0;
                            }

                            // Calculation Logic: 20% savings
                            const savingsPercent = 0.20;
                            const monthlySavings = value * savingsPercent;
                            const newBill = value - monthlySavings;
                            const yearlySavings = monthlySavings * 12;

                            // Update UI
                            newBillDisplay.textContent = formatCurrencySavings(newBill);
                            monthlySavingsDisplay.textContent = formatCurrencySavings(monthlySavings);
                            yearlySavingsDisplay.textContent = formatCurrencySavings(yearlySavings);
                        }

                        // Init
                        document.addEventListener('DOMContentLoaded', calculateSavingsSection);
                    </script>
                </div>
                <!-- Decorative Circle -->
                <div
                    class="absolute -z-10 top-1/2 right-0 transform translate-x-12 -translate-y-1/2 w-64 h-64 bg-[#2323FA]/10 rounded-full blur-3xl">
                </div>
            </div>

        </div>
    </div>
</section>