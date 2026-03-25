<section id="calculadora" class="py-16 md:py-24 bg-gray-50">
    <div class="container mx-auto px-4 md:px-6">
        <div class="max-w-4xl mx-auto">
            <!-- Header -->
            <div class="text-center mb-12">
                <span
                    class="inline-block py-1 px-3 rounded-full bg-green-100 text-green-700 text-sm font-semibold mb-3">
                    Simule sua Economia
                </span>
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                    Quanto você gasta hoje com energia?
                </h2>
                <p class="text-lg text-gray-600">
                    Veja o quanto você pode economizar garantindo seus 20% de desconto.
                </p>
            </div>

            <!-- Calculator Card -->
            <div class="bg-white rounded-2xl shadow-xl overflow-hidden border border-gray-100">
                <div class="grid md:grid-cols-2">

                    <!-- Input Section -->
                    <div class="p-8 md:p-10 bg-white">
                        <label for="billValue" class="block text-sm font-medium text-gray-700 mb-2">
                            Valor médio da sua conta de luz
                        </label>
                        <div class="relative mb-8">
                            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <span class="text-gray-500 font-semibold text-lg">R$</span>
                            </div>
                            <input type="number" id="billValue"
                                class="block w-full pl-12 pr-4 py-4 bg-gray-50 border border-gray-200 rounded-xl text-2xl font-bold text-gray-900 focus:ring-2 focus:ring-green-500 focus:border-transparent transition-all outline-none"
                                placeholder="0,00" value="500" oninput="calculateSavings()">
                        </div>

                        <div class="space-y-4">
                            <div class="flex items-center justify-between text-sm text-gray-600">
                                <span>Desconto Garantido</span>
                                <span class="font-bold text-green-600 bg-green-50 px-2 py-1 rounded">20% OFF</span>
                            </div>
                            <div class="w-full bg-gray-100 rounded-full h-2">
                                <div class="bg-green-500 h-2 rounded-full" style="width: 20%"></div>
                            </div>
                            <p class="text-xs text-gray-400">
                                *O desconto é aplicado sobre a tarifa de energia, excluindo impostos e taxas de
                                iluminação pública.
                            </p>
                        </div>
                    </div>

                    <!-- Result Section -->
                    <div
                        class="p-8 md:p-10 bg-gradient-to-br from-green-600 to-green-700 text-white flex flex-col justify-center relative overflow-hidden">
                        <!-- Decorative Circles -->
                        <div class="absolute top-0 right-0 -mr-16 -mt-16 w-32 h-32 rounded-full bg-white/10 blur-2xl">
                        </div>
                        <div class="absolute bottom-0 left-0 -ml-16 -mb-16 w-32 h-32 rounded-full bg-white/10 blur-2xl">
                        </div>

                        <div class="relative z-10">
                            <div class="mb-8">
                                <p class="text-green-100 text-sm font-medium mb-1">Nova estimativa mensal</p>
                                <h3 class="text-4xl font-bold" id="newBillDisplay">R$ 400,00</h3>
                            </div>

                            <div class="grid grid-cols-2 gap-4 mb-8">
                                <div class="bg-white/10 rounded-lg p-3 backdrop-blur-sm">
                                    <p class="text-green-100 text-xs mb-1">Economia Mensal</p>
                                    <p class="text-xl font-bold text-white" id="monthlySavingsDisplay">R$ 100,00</p>
                                </div>
                                <div class="bg-white/20 rounded-lg p-3 backdrop-blur-sm border border-white/20">
                                    <p class="text-white text-xs mb-1">Economia Anual</p>
                                    <p class="text-xl font-bold text-yellow-300" id="yearlySavingsDisplay">R$ 1.200,00
                                    </p>
                                </div>
                            </div>

                            <a href="#assine"
                                class="block w-full py-3 px-6 bg-white text-green-700 rounded-xl font-bold text-center hover:bg-green-50 transition-colors shadow-lg">
                                Quero economizar agora
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function formatCurrency(value) {
            return new Intl.NumberFormat('pt-BR', {
                style: 'currency',
                currency: 'BRL'
            }).format(value);
        }

        function calculateSavings() {
            const input = document.getElementById('billValue');
            const newBillDisplay = document.getElementById('newBillDisplay');
            const monthlySavingsDisplay = document.getElementById('monthlySavingsDisplay');
            const yearlySavingsDisplay = document.getElementById('yearlySavingsDisplay');

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
            newBillDisplay.textContent = formatCurrency(newBill);
            monthlySavingsDisplay.textContent = formatCurrency(monthlySavings);
            yearlySavingsDisplay.textContent = formatCurrency(yearlySavings);
        }

        // Initialize on load
        document.addEventListener('DOMContentLoaded', calculateSavings);
    </script>
</section>