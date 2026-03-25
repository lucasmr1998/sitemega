<?php
if (!isset($_SESSION)) {
    session_start();
}
require_once '../includes/config.php';
?>
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <base href="/">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roleta de Prêmios — MegaLink</title>
    <meta name="description" content="Participe da promoção da MegaLink e gire a roleta para ganhar prêmios incríveis!">

    <!-- Google Fonts: Barlow -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <!-- FontAwesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- jQuery (necessário para animação da roleta e AJAX) -->
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>

    <!-- Tailwind CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { sans: ['Barlow', 'sans-serif'] },
                    colors: {
                        primary: { DEFAULT: '#2323FA', dark: '#040470', mid: '#0000C6', light: '#0000FF' },
                        orange:  { DEFAULT: '#FF6905', dark: '#DC5A05', light: '#F57D05' },
                    }
                }
            }
        }
    </script>

    <style>
        /* Garante que as imagens da roleta não empurrem o layout */
        .roleta-img { display: none; }
        .roleta-img.ativa { display: block; }
    </style>
</head>

<body class="font-sans antialiased text-gray-800 bg-white">

    <?php include '../includes/header.php'; ?>

    <!-- Hero Banner da Roleta -->
    <div class="bg-gradient-to-r from-primary-dark to-primary py-12 text-white text-center">
        <div class="max-w-4xl mx-auto px-4">
            <span class="inline-block bg-orange text-white text-xs font-bold uppercase tracking-widest px-3 py-1 rounded-full mb-4">Promoção Exclusiva</span>
            <h1 class="text-4xl md:text-5xl font-black leading-tight mb-3">
                Gire a Roleta e <span class="text-orange">Ganhe Prêmios!</span>
            </h1>
            <p class="text-blue-100 text-lg">Cadastre-se e gire a roleta para descobrir seu prêmio especial na contratação.</p>
        </div>
    </div>

    <main class="bg-gray-50 min-h-screen py-12">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">

            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="flex flex-col lg:flex-row">

                    <!-- ═══════════════════════════════
                         COLUNA ESQUERDA — Roleta
                    ════════════════════════════════ -->
                    <div class="lg:w-1/2 bg-gradient-to-br from-primary-dark via-primary to-primary-mid flex items-center justify-center p-8">
                        <div class="w-full max-w-sm">
                            <!-- Imagens da Roleta (animação JS) -->
                            <img id="roleta00" src="/roleta/images/roletaPremiosVirtuais00.png" class="w-full h-auto drop-shadow-2xl" alt="Roleta">
                            <img id="roleta01" src="/roleta/images/roletaPremiosVirtuais01.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta02" src="/roleta/images/roletaPremiosVirtuais02.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta03" src="/roleta/images/roletaPremiosVirtuais03.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta04" src="/roleta/images/roletaPremiosVirtuais04.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta05" src="/roleta/images/roletaPremiosVirtuais05.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta06" src="/roleta/images/roletaPremiosVirtuais06.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta07" src="/roleta/images/roletaPremiosVirtuais07.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta08" src="/roleta/images/roletaPremiosVirtuais08.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta09" src="/roleta/images/roletaPremiosVirtuais09.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta10" src="/roleta/images/roletaPremiosVirtuais10.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta11" src="/roleta/images/roletaPremiosVirtuais11.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">
                            <img id="roleta12" src="/roleta/images/roletaPremiosVirtuais12.png" class="w-full h-auto drop-shadow-2xl hidden" alt="Roleta">

                            <div class="mt-6 text-center text-blue-200 text-sm">
                                <i class="fa-solid fa-gift mr-1"></i>
                                Prêmios garantidos para novos clientes
                            </div>
                        </div>
                    </div>

                    <!-- ═══════════════════════════════
                         COLUNA DIREITA — Formulário / Ação
                    ════════════════════════════════ -->
                    <div class="lg:w-1/2 p-8 lg:p-12 flex items-center">
                        <div class="w-full">

                            <?php
                            // ── Estado: sem sessão → exibe formulário de cadastro ──────────
                            if (!isset($_SESSION['premio']) && !isset($_SESSION['erro'])):
                            ?>
                            <h2 class="text-2xl font-black text-primary-dark mb-1">Participe da Promoção!</h2>
                            <p class="text-gray-400 text-xs mb-6">Preencha os dados abaixo e gire a roleta.</p>

                            <!-- Barra de progresso -->
                            <div class="flex items-center mb-7 gap-0">
                                <div class="flex flex-col items-center">
                                    <div id="dot1" class="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-xs font-bold transition-all">1</div>
                                    <span class="text-[10px] text-gray-400 mt-1">Perfil</span>
                                </div>
                                <div id="line1" class="flex-1 h-0.5 bg-gray-200 mb-3 transition-all"></div>
                                <div class="flex flex-col items-center">
                                    <div id="dot2" class="w-8 h-8 rounded-full bg-gray-200 text-gray-400 flex items-center justify-center text-xs font-bold transition-all">2</div>
                                    <span class="text-[10px] text-gray-400 mt-1">Dados</span>
                                </div>
                                <div id="line2" class="flex-1 h-0.5 bg-gray-200 mb-3 transition-all"></div>
                                <div class="flex flex-col items-center">
                                    <div id="dot3" class="w-8 h-8 rounded-full bg-gray-200 text-gray-400 flex items-center justify-center text-xs font-bold transition-all">3</div>
                                    <span class="text-[10px] text-gray-400 mt-1">Endereço</span>
                                </div>
                            </div>

                            <form action="/roleta/cadastrar.php" method="post" id="form-roleta">
                                <input type="hidden" name="canal" value="Online">

                                <!-- ═══ STEP 1: Cliente ou não? ═══ -->
                                <div id="step1" class="step-panel">
                                    <p class="text-sm font-semibold text-gray-700 mb-4">Você já é cliente MegaLink?</p>
                                    <div class="grid grid-cols-2 gap-4">
                                        <button type="button" onclick="escolheCliente(true)"
                                            class="flex flex-col items-center justify-center border-2 border-gray-200 rounded-2xl p-5 hover:border-primary hover:bg-blue-50 transition group cursor-pointer">
                                            <i class="fa-solid fa-user-check text-3xl text-gray-300 group-hover:text-primary mb-2 transition"></i>
                                            <span class="font-bold text-sm text-gray-500 group-hover:text-primary transition">Sim, já sou</span>
                                        </button>
                                        <button type="button" onclick="escolheCliente(false)"
                                            class="flex flex-col items-center justify-center border-2 border-gray-200 rounded-2xl p-5 hover:border-[#FF6905] hover:bg-orange-50 transition group cursor-pointer">
                                            <i class="fa-solid fa-user-plus text-3xl text-gray-300 group-hover:text-[#FF6905] mb-2 transition"></i>
                                            <span class="font-bold text-sm text-gray-500 group-hover:text-[#FF6905] transition">Ainda não</span>
                                        </button>
                                    </div>
                                    <div id="msg-cliente" class="hidden mt-4 rounded-xl border border-blue-200 bg-blue-50 p-4 text-center">
                                        <i class="fa-solid fa-heart text-primary mb-2 text-xl"></i>
                                        <p class="text-sm font-semibold text-primary">Obrigado por ser MegaLink!</p>
                                        <p class="text-xs text-gray-500 mt-1">Esta promoção é exclusiva para novos clientes. Fique de olho nas nossas redes para promoções especiais para quem já é da família! 💙</p>
                                    </div>
                                </div>

                                <!-- ═══ STEP 2: Dados pessoais ═══ -->
                                <div id="step2" class="step-panel hidden space-y-3">
                                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                        <div>
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="nome">Nome completo</label>
                                            <input type="text" id="nome" name="nome" class="sf" placeholder="Seu nome completo">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="telefone">Telefone</label>
                                            <input type="text" id="telefone" name="telefone" class="sf" placeholder="(xx) 9xxxx-xxxx">
                                        </div>
                                    </div>
                                    <div>
                                        <label class="block text-xs font-semibold text-gray-600 mb-1" for="email">E-mail</label>
                                        <input type="email" id="email" name="email" class="sf" placeholder="seu@email.com">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-semibold text-gray-600 mb-1" for="cpf">CPF</label>
                                        <input type="text" id="cpf" name="cpf" class="sf" placeholder="000.000.000-00">
                                    </div>
                                    <div class="flex gap-3 pt-2">
                                        <button type="button" onclick="goStep(1)" class="flex-1 border border-gray-300 text-gray-500 font-semibold py-2.5 rounded-xl hover:bg-gray-50 transition text-sm">← Voltar</button>
                                        <button type="button" onclick="validaStep2()" class="flex-1 bg-primary hover:bg-primary-dark text-white font-bold py-2.5 rounded-xl transition text-sm">Próximo →</button>
                                    </div>
                                </div>

                                <!-- ═══ STEP 3: Endereço ═══ -->
                                <div id="step3" class="step-panel hidden space-y-3">
                                    <div class="grid grid-cols-2 gap-3">
                                        <div>
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="cep">CEP</label>
                                            <input type="text" id="cep" name="cep" onchange="completa_endereco()" class="sf" placeholder="00000-000">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="cidade">Cidade</label>
                                            <select id="cidade" name="cidade" class="sf bg-white">
                                                <option value="Rio Grande">Rio Grande</option>
                                                <option value="Pelotas">Pelotas</option>
                                                <option value="Cassino">Cassino</option>
                                                <option value="São José do Norte">São José do Norte</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-5 gap-3">
                                        <div class="col-span-3">
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="rua">Rua</label>
                                            <input type="text" id="rua" name="rua" class="sf" placeholder="Nome da rua">
                                        </div>
                                        <div class="col-span-1">
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="numero_casa">Nº</label>
                                            <input type="text" id="numero_casa" name="numero_casa" class="sf" placeholder="123">
                                        </div>
                                        <div class="col-span-1">
                                            <label class="block text-xs font-semibold text-gray-600 mb-1" for="estado">UF</label>
                                            <input type="text" id="estado" name="estado" class="sf" placeholder="RS">
                                        </div>
                                    </div>
                                    <div>
                                        <label class="block text-xs font-semibold text-gray-600 mb-1" for="bairro">Bairro</label>
                                        <input type="text" id="bairro" name="bairro" class="sf" placeholder="Seu bairro">
                                    </div>
                                    <div class="flex items-start gap-2">
                                        <input type="checkbox" id="termos" required class="mt-0.5 rounded border-gray-300 text-primary focus:ring-primary">
                                        <label for="termos" class="text-xs text-gray-500">Concordo com os <a href="/roleta/Regulamento.pdf" download class="text-primary font-semibold hover:underline">termos da promoção</a>.</label>
                                    </div>
                                    <div class="flex gap-3 pt-1">
                                        <button type="button" onclick="goStep(2)" class="flex-1 border border-gray-300 text-gray-500 font-semibold py-2.5 rounded-xl hover:bg-gray-50 transition text-sm">← Voltar</button>
                                        <button type="submit" class="flex-1 bg-[#FF6905] hover:bg-[#DC5A05] text-white font-bold py-2.5 rounded-xl transition shadow-md flex items-center justify-center gap-2 text-sm">
                                            <i class="fa-solid fa-ticket"></i> Cadastrar!
                                        </button>
                                    </div>
                                </div>

                            </form>

                            <style>
                                .sf { width:100%; border:1px solid #d1d5db; border-radius:0.75rem; padding:0.55rem 1rem; font-size:0.82rem; outline:none; transition:all .2s; }
                                .sf:focus { border-color:#2323FA; box-shadow:0 0 0 3px rgba(35,35,250,.1); }
                            </style>

                            <script>
                            function goStep(n) {
                                document.querySelectorAll('.step-panel').forEach(el => el.classList.add('hidden'));
                                document.getElementById('step' + n).classList.remove('hidden');
                                for (let i = 1; i <= 3; i++) {
                                    const dot = document.getElementById('dot' + i);
                                    if (i < n) { dot.className='w-8 h-8 rounded-full bg-green-500 text-white flex items-center justify-center text-xs font-bold transition-all'; dot.innerHTML='✓'; }
                                    else if (i===n) { dot.className='w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-xs font-bold transition-all'; dot.innerHTML=i; }
                                    else { dot.className='w-8 h-8 rounded-full bg-gray-200 text-gray-400 flex items-center justify-center text-xs font-bold transition-all'; dot.innerHTML=i; }
                                }
                                for (let i = 1; i <= 2; i++) {
                                    document.getElementById('line'+i).className = (i < n)
                                        ? 'flex-1 h-0.5 bg-green-400 mb-3 transition-all'
                                        : 'flex-1 h-0.5 bg-gray-200 mb-3 transition-all';
                                }
                            }
                            function escolheCliente(sim) {
                                if (sim) { document.getElementById('msg-cliente').classList.remove('hidden'); }
                                else { document.getElementById('msg-cliente').classList.add('hidden'); goStep(2); }
                            }
                            function validaStep2() {
                                const ok = ['nome','telefone','email','cpf'].every(id => document.getElementById(id).value.trim());
                                if (!ok) { alert('Preencha todos os campos antes de continuar.'); return; }
                                goStep(3);
                            }
                            </script>

                            <?php
                            // ── Estado: erro ───────────────────────────────────────────────

                            elseif (isset($_SESSION['erro'])):
                                if ($_SESSION['erro'] === 'jah_cadastrado'):
                                    $nome_salvo = $_SESSION['nome'] ?? 'você';
                                    session_destroy();
                            ?>
                            <div class="rounded-2xl border-2 border-red-200 bg-red-50 p-6 text-center">
                                <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fa-solid fa-circle-exclamation text-red-500 text-3xl"></i>
                                </div>
                                <h3 class="text-lg font-bold text-red-700 mb-2">Você já participou!</h3>
                                <p class="text-red-600 text-sm">Olá, <strong><?= htmlspecialchars($nome_salvo) ?></strong>! Seu CPF já foi cadastrado nesta promoção.</p>
                                <a href="index.php" class="mt-4 inline-block text-primary text-sm font-semibold hover:underline">← Voltar</a>
                            </div>

                            <?php elseif ($_SESSION['erro'] === 'acabau_premio'): ?>
                            <div class="rounded-2xl border-2 border-yellow-200 bg-yellow-50 p-6 text-center">
                                <div class="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fa-solid fa-triangle-exclamation text-yellow-500 text-3xl"></i>
                                </div>
                                <h3 class="text-lg font-bold text-yellow-700 mb-2">Prêmios esgotados</h3>
                                <p class="text-yellow-700 text-sm">Desculpe, os prêmios para a sua região já foram todos resgatados.</p>
                                <a href="index.php" class="mt-4 inline-block text-primary text-sm font-semibold hover:underline">← Voltar</a>
                            </div>

                            <?php
                                endif;
                            // ── Estado: tem prêmio → exibe botão Girar ─────────────────────
                            elseif (isset($_SESSION['premio'])):
                            ?>
                            <div class="text-center">
                                <div class="w-20 h-20 bg-orange/10 rounded-full flex items-center justify-center mx-auto mb-6">
                                    <i class="fa-solid fa-star text-orange text-4xl animate-pulse"></i>
                                </div>
                                <h2 class="text-2xl font-black text-primary-dark mb-2">Cadastro concluído!</h2>
                                <p class="text-gray-500 mb-8">Agora é hora da sorte. Clique no botão e gire a roleta!</p>
                                <button onclick="trocaImagem()" id="btn-girar"
                                    class="w-full bg-orange hover:bg-orange-dark text-white font-black py-5 rounded-2xl text-xl transition shadow-xl hover:shadow-orange/40 flex items-center justify-center gap-3">
                                    <i class="fa-solid fa-arrows-spin"></i>
                                    Girar a Roleta!
                                </button>
                                <p class="text-gray-400 text-xs mt-4">Você tem apenas 1 giro disponível.</p>
                            </div>

                            <?php endif; ?>

                        </div>
                    </div><!-- /coluna direita -->

                </div><!-- /flex row -->
            </div><!-- /card -->

        </div>
    </main>

    <?php include '../includes/footer.php'; ?>

    <!-- ══════════════════════════════════════════
         MODAL DE PRÊMIO (substitui o alert())
    ═══════════════════════════════════════════ -->
    <div id="modal-premio" class="fixed inset-0 z-50 flex items-center justify-center hidden">
        <!-- Overlay -->
        <div class="absolute inset-0 bg-black/60 backdrop-blur-sm"></div>
        <!-- Card -->
        <div class="relative bg-white rounded-3xl shadow-2xl p-10 max-w-md w-full mx-4 text-center z-10 animate-bounce-once">
            <div class="w-20 h-20 bg-orange/10 rounded-full flex items-center justify-center mx-auto mb-6">
                <i class="fa-solid fa-trophy text-orange text-4xl"></i>
            </div>
            <h2 class="text-3xl font-black text-primary-dark mb-2">Parabéns! 🎉</h2>
            <p id="texto-premio" class="text-gray-600 text-base mb-8 leading-relaxed"></p>
            <a href="<?= $config['assineJaLink'] ?? 'tel:08009999999' ?>"
               class="w-full inline-block bg-orange hover:bg-orange-dark text-white font-bold py-4 rounded-xl transition shadow-lg text-lg">
                <i class="fa-solid fa-phone mr-2"></i>Contratar agora
            </a>
            <p class="text-gray-400 text-xs mt-4">Prêmio válido por 24 horas após o giro.</p>
        </div>
    </div>

    <!-- ══════════════════════════════════════════
         PHP → JS: passa o número sorteado
    ═══════════════════════════════════════════ -->
    <?php if (isset($_SESSION['premio'])): ?>
    <script>var sorteado = <?= (int) $_SESSION['premio'] ?>;</script>
    <?php endif; ?>

    <!-- ══════════════════════════════════════════
         JS: Animação da Roleta + autocomplete CEP
    ═══════════════════════════════════════════ -->
    <script>
        // ── Auto-completa endereço via ViaCEP ───────────────────
        function completa_endereco() {
            var cep = $("#cep").val().replace(/\D/g, '');
            if (cep.length !== 8) return;
            $.ajax({
                url: "https://viacep.com.br/ws/" + cep + "/json/",
                cache: false
            }).done(function(end) {
                if (!end.erro) {
                    $("#rua").val(end.logradouro);
                    $("#estado").val(end.uf);
                    $("#bairro").val(end.bairro);
                }
            });
        }

        // ── Animação da Roleta ───────────────────────────────────
        var imagem_atual = 0;
        var velocidade   = 1025;
        var etapa        = 0;
        var contador     = 0;
        var acabou       = false;
        var girando      = false;

        function trocaImagem() {
            if (girando || acabou) return;
            girando = true;

            // Desabilita o botão para evitar múltiplos cliques
            $("#btn-girar").prop("disabled", true)
                           .addClass("opacity-60 cursor-not-allowed");

            _anima();
        }

        function _anima() {
            if (!acabou) {
                var image_velha = "roleta" + ("00" + imagem_atual).slice(-2);
                var proximo     = (imagem_atual === 12) ? 1 : imagem_atual + 1;
                var image_nova  = "roleta" + ("00" + proximo).slice(-2);

                if (imagem_atual === 12) imagem_atual = 0;

                $("#" + image_velha).addClass("hidden");
                $("#" + image_nova).removeClass("hidden");

                imagem_atual++;

                if (etapa === 0) {
                    velocidade -= 125;
                    if (velocidade < 150) { etapa = 1; contador = 0; }
                }
                if (etapa === 1) {
                    contador++;
                    if (contador === 50) etapa = 2;
                }
                if (etapa === 2) {
                    velocidade += 125;
                    if (velocidade > 800) etapa = 3;
                }
                if (etapa === 3 && imagem_atual === sorteado) {
                    acabou = true;
                }

                setTimeout(_anima, velocidade);
            } else {
                // Exibe prêmio no modal
                var premios = {
                    1:  "Você ganhou um desconto de R$10/mês durante 6 meses! Válido por 24 horas.",
                    2:  "Você ganhou 50% de desconto na taxa de instalação! Válido por 24 horas.",
                    3:  "Você ganhou um desconto de R$10/mês durante 12 meses! Válido por 24 horas.",
                    4:  "Você ganhou 1 mês de internet grátis! Válido por 24 horas.",
                    5:  "Você ganhou a taxa de instalação grátis! Válido por 24 horas.",
                    6:  "Você ganhou 2 meses de internet grátis! Válido por 24 horas.",
                    7:  "Você ganhou 1 mês de internet grátis! Válido por 24 horas.",
                    8:  "Você ganhou 50% de desconto na taxa de instalação! Válido por 24 horas.",
                    9:  "Você ganhou um desconto de R$10/mês durante 6 meses! Válido por 24 horas.",
                    10: "Você ganhou um desconto de R$10/mês durante 12 meses! Válido por 24 horas.",
                    11: "Você ganhou 3 meses de internet grátis! Válido por 24 horas.",
                    12: "Você ganhou a taxa de instalação grátis! Válido por 24 horas."
                };

                var msgPremio = premios[imagem_atual] || "Você ganhou 1 mês de internet grátis! Válido por 24 horas.";

                $("#texto-premio").text(msgPremio);
                $("#modal-premio").removeClass("hidden");

                // Destroi sessão no servidor para impedir regiro
                $.ajax({ url: '/roleta/destroy_session.php', method: 'POST' });
            }
        }
    </script>

    <!-- JS principal do site -->
    <script src="../assets/js/main.js"></script>

</body>
</html>
