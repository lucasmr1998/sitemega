<section class="py-20 bg-white">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">

        <div class="text-center mb-12">
            <span class="text-[#FF6905] font-bold tracking-wider uppercase text-sm mb-2 block">Dúvidas Frequentes</span>
            <h2 class="text-3xl font-extrabold text-gray-900">Tire suas dúvidas</h2>
        </div>

        <div class="space-y-4">

            <!-- Item 1 -->
            <div class="border border-gray-200 rounded-xl overflow-hidden">
                <button onclick="toggleAccordion('1')"
                    class="w-full flex items-center justify-between p-6 bg-white hover:bg-gray-50 transition text-left focus:outline-none">
                    <span class="font-bold text-gray-900">Como funciona o desconto na conta de luz?</span>
                    <i id="faq-icon-1"
                        class="fa-solid fa-chevron-down text-gray-400 transition-transform duration-300"></i>
                </button>
                <div id="faq-content-1" class="hidden p-6 pt-0 text-gray-600 border-t border-gray-100">
                    O desconto é aplicado através da compensação de energia. A energia gerada em nossas usinas solares é
                    injetada na rede da distribuidora em seu nome, e esse crédito abate o valor do seu consumo, gerando
                    a economia.
                </div>
            </div>

            <!-- Item 2 -->
            <div class="border border-gray-200 rounded-xl overflow-hidden">
                <button onclick="toggleAccordion('2')"
                    class="w-full flex items-center justify-between p-6 bg-white hover:bg-gray-50 transition text-left focus:outline-none">
                    <span class="font-bold text-gray-900">É preciso fazer alguma instalação?</span>
                    <i id="faq-icon-2"
                        class="fa-solid fa-chevron-down text-gray-400 transition-transform duration-300"></i>
                </button>
                <div id="faq-content-2" class="hidden p-6 pt-0 text-gray-600 border-t border-gray-100">
                    Não! Diferente da energia solar residencial tradicional, no modelo por assinatura você não precisa
                    instalar painéis, inversor, nem fazer obras no telhado. Tudo é feito remotamente.
                </div>
            </div>

            <!-- Item 3 -->
            <div class="border border-gray-200 rounded-xl overflow-hidden">
                <button onclick="toggleAccordion('3')"
                    class="w-full flex items-center justify-between p-6 bg-white hover:bg-gray-50 transition text-left focus:outline-none">
                    <span class="font-bold text-gray-900">Tem multa de cancelamento?</span>
                    <i id="faq-icon-3"
                        class="fa-solid fa-chevron-down text-gray-400 transition-transform duration-300"></i>
                </button>
                <div id="faq-content-3" class="hidden p-6 pt-0 text-gray-600 border-t border-gray-100">
                    Nenhuma. Nosso plano não possui fidelidade. Você pode cancelar a qualquer momento sem pagar multas,
                    apenas solicitando o desligamento com o aviso prévio estipulado no contrato.
                </div>
            </div>

            <!-- Item 4 -->
            <div class="border border-gray-200 rounded-xl overflow-hidden">
                <button onclick="toggleAccordion('4')"
                    class="w-full flex items-center justify-between p-6 bg-white hover:bg-gray-50 transition text-left focus:outline-none">
                    <span class="font-bold text-gray-900">Para quem está disponível?</span>
                    <i id="faq-icon-4"
                        class="fa-solid fa-chevron-down text-gray-400 transition-transform duration-300"></i>
                </button>
                <div id="faq-content-4" class="hidden p-6 pt-0 text-gray-600 border-t border-gray-100">
                    Disponível para residências, comércios e empresas atendidas pela distribuidora local (CEMIG, CPFL,
                    etc) com consumo mínimo de R$ 150,00 mensais (conforme região).
                </div>
            </div>

        </div>

    </div>
</section>