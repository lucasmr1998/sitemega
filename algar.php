<?php require_once 'includes/config_algar.php'; ?>
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MegaLink - Variação Algar</title>

    <!-- Google Fonts: Barlow (Keeping same font as it is clean) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100&display=swap"
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
                            DEFAULT: '<?php echo $config['primaryColor']; ?>', dark: '<?php echo $config['primaryDarkColor']; ?>',
                        },
                        secondary: {
                            DEFAULT: '<?php echo $config['secondaryColor']; ?>',
                        },
                        accent: {
                            DEFAULT: '<?php echo $config['accentColor']; ?>',
                        }
                    }
                }
            }
        }
    </script>
</head>

<body class="font-sans antialiased text-gray-800 bg-white">

    <?php include 'includes/algar_header.php'; ?>

    <main>
        <?php
        include 'includes/sections/algar_hero.php';
        include 'includes/sections/algar_sub_header.php';
        include 'includes/sections/algar_offers.php';
        // include 'includes/sections/algar_smartphones.php';
        // include 'includes/sections/algar_banner.php';      // "Ainda não decidiu?"
        include 'includes/sections/algar_self_service.php';// Green Section
        include 'includes/sections/algar_app.php';         // App Section
        include 'includes/sections/algar_blog.php';        // "Aproveite o máximo"
        // Reuse some generic sections but styled via config colors automatically
        ?>

    </main>

    <?php include 'includes/footer.php'; ?>

    <script src="assets/js/main.js"></script>
</body>

</html>