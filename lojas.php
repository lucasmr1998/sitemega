<?php require_once 'includes/config.php'; ?>
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nossas Lojas - <?php echo $config['companyName']; ?></title>

    <!-- Google Fonts: Barlow -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
        rel="stylesheet">

    <!-- CSS Global -->
    <link rel="stylesheet" href="assets/css/style.css">

    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <!-- Tailwind CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Barlow', 'sans-serif'],
                    },
                    colors: {
                        primary: {
                            DEFAULT: '#2323FA',
                            dark: '#040470',
                            darker: '#000073',
                            mid: '#0000C6',
                            light: '#0000FF',
                        },
                        orange: {
                            DEFAULT: '#FF6905',
                            dark: '#DC5A05',
                            light: '#F57D05',
                            lighter: '#ED8905',
                            golden: '#FFA72D',
                        },
                        secondary: {
                            DEFAULT: '#2323FA',
                            dark: '#040470',
                            light: '#0000FF',
                        },
                        accent: {
                            DEFAULT: '#10B981',
                            dark: '#059669',
                        },
                        pink: {
                            500: '#E4405F',
                        }
                    }
                }
            }
        }
    </script>
</head>

<body class="font-sans antialiased text-black bg-white flex flex-col min-h-screen">

    <?php include 'includes/header.php'; ?>

    <main class="flex-grow bg-[#E6E7EB]"> <!-- Gray background consistent with screenshot -->

        <!-- Title Section -->
        <section class="py-12 text-center">
            <h1 class="text-4xl font-bold text-[#2323FA] mb-2">Nossas Lojas</h1>
            <p class="text-gray-500">Encontre a MegaLink mais próxima de você</p>
        </section>

        <!-- Stores Grid -->
        <section class="pb-20 px-4 md:px-8 max-w-7xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

                <?php
                $stores = [
                    [
                        'city' => 'FLORIANO/PI',
                        'address1' => 'Av. Bucar Neto, 1088',
                        'address2' => 'Catumbi'
                    ],
                    [
                        'city' => 'OEIRAS/PI',
                        'address1' => 'Av. Duque de Caxias, 246',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'ÁGUA BRANCA/PI',
                        'address1' => 'Av. Miguel Rosa, 1310',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'NAZARÉ DO PIAUÍ/PI',
                        'address1' => 'Avenida Joaquim Ramos, 1507',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'AROAZES/PI',
                        'address1' => 'Praça Detinho Soares, 521',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'GUADALUPE/PI',
                        'address1' => 'Rua Jonas Lopes, 13',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'REGENERAÇÃO/PI',
                        'address1' => 'Av. Alberto Leal Nunes, 1342',
                        'address2' => 'Alto do Balanço'
                    ],
                    [
                        'city' => 'MONSENHOR GIL/PI',
                        'address1' => 'Av. Joel Mendes, 509',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'VALENÇA DO PIAUÍ/PI',
                        'address1' => 'Rua Arlindo Nogueira, 781',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'SÃO PEDRO DO PIAUÍ/PI',
                        'address1' => 'Av. Pres. Vargas, 545',
                        'address2' => 'Centro' // Assuming Centro based on layout, screenshot said 545 but looks like typo or specific block
                    ],
                    [
                        'city' => 'AMARANTE/PI',
                        'address1' => 'Rua Manoel Sobral, S/N',
                        'address2' => 'Centro'
                    ],
                    [
                        'city' => 'ÁGUA BRANCA/PI',
                        'address1' => 'Av. Jose Miguel, 3010',
                        'address2' => 'Centro'
                    ]
                ];

                foreach ($stores as $store):
                    ?>
                    <div
                        class="bg-white rounded-2xl p-8 shadow-sm hover:shadow-md transition duration-300 flex flex-col justify-between h-56">
                        <!-- Fixed height for uniformity -->
                        <div>
                            <h3 class="text-[#2323FA] font-bold text-lg mb-2 uppercase"><?php echo $store['city']; ?></h3>
                            <div class="text-gray-500 text-sm leading-relaxed">
                                <p><?php echo $store['address1']; ?></p>
                                <p><?php echo $store['address2']; ?></p>
                            </div>
                        </div>

                        <div class="flex items-center gap-3 mt-4">
                            <!-- Map Button -->
                            <a href="#"
                                class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center text-gray-600 hover:bg-[#2323FA] hover:text-white transition">
                                <i class="fa-solid fa-location-dot"></i>
                            </a>
                            <!-- Chat Button -->
                            <a href="#"
                                class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center text-gray-600 hover:bg-[#2323FA] hover:text-white transition">
                                <i class="fa-regular fa-comment-dots"></i> <!-- Or similar icon -->
                            </a>
                        </div>
                    </div>
                <?php endforeach; ?>

            </div>
        </section>

        <!-- Floating WhatsApp Button -->
        <a href="https://wa.me/<?php echo $config['whatsappNumber']; ?>" target="_blank"
            class="fixed bottom-6 right-6 bg-[#10B981] text-white p-4 rounded-full shadow-lg hover:bg-[#059669] transition z-50 flex items-center justify-center w-14 h-14">
            <i class="fa-brands fa-whatsapp text-2xl"></i>
        </a>

    </main>

    <?php include 'includes/footer.php'; ?>

    <!-- Scripts Globais -->
    <script src="assets/js/main.js"></script>
</body>

</html>