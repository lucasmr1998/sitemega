<?php require_once 'includes/config.php'; ?>
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Megalink - Mega Rastreamento</title>

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
                        }
                    }
                }
            }
        }
    </script>
</head>

<body class="font-sans antialiased text-black bg-white">

    <?php include 'includes/header.php'; ?>

    <main>
        <?php
        include 'includes/sections/tracking_hero.php';
        include 'includes/sections/tracking_features.php';
        include 'includes/sections/tracking_benefits.php';
        include 'includes/sections/tracking_app.php';
        include 'includes/sections/tracking_cta.php';
        ?>
    </main>

    <?php include 'includes/footer.php'; ?>

    <!-- Scripts Globais -->
    <script src="assets/js/main.js"></script>
    <script src="assets/js/form-handler.js"></script>
</body>

</html>