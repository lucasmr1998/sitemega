<?php

if (!isset($_SESSION)) {
    session_start();
}

include_once("conexao.php");

$_SESSION['nome']   = $nome_usuario     = trim($_POST['nome']);
$telefone_usuario   = trim($_POST['telefone']);
$email_usuario      = trim($_POST['email']);
$cpf_usuario        = trim($_POST['cpf']);
$cep_usuario        = trim($_POST['cep']);
$cidade_usuario     = trim($_POST['cidade']);
$estado_usuario     = trim($_POST['estado']);
$endereco_usuario   = trim($_POST['rua']) . " Nº " . trim($_POST['numero_casa']);
$bairro_usuario     = trim($_POST['bairro']);
$canal              = trim($_POST['canal']);

if (strtolower($bairro_usuario) == 'cassino') {
    $bairro_usuario = 'Cassino';
}

// ── 1. Verifica CPF duplicado ─────────────────────────────────────────────────
$stmt = $conn->prepare("SELECT * FROM usuarios WHERE cpf = ? LIMIT 1");
$stmt->bind_param("s", $cpf_usuario);
$stmt->execute();
$resultado = $stmt->get_result();
$row_usuario = mysqli_fetch_assoc($resultado);

$_SESSION['premio'] = $row_usuario['premio'] ?? null;

if ($resultado->num_rows > 0) {
    $_SESSION['erro'] = "jah_cadastrado";
    $stmt->close();
    header("Location:index.php");
    die();
}
$stmt->close();

// ── 2. Determina localidade ───────────────────────────────────────────────────
if ($bairro_usuario == 'Cassino') {
    $localidade = 'cassino';
} elseif ($cidade_usuario == 'Rio Grande') {
    $localidade = 'rio grande';
} elseif ($cidade_usuario == 'Pelotas') {
    $localidade = 'pelotas';
} elseif ($cidade_usuario == 'São José do Norte') {
    $localidade = 'sjn';
} else {
    $localidade = 'rio grande'; // fallback padrão
}

// ── 3. Busca prêmios disponíveis para a localidade ───────────────────────────
$stmt2 = $conn->prepare("SELECT * FROM premios WHERE localidade = ? AND quantidade > 0");
$stmt2->bind_param("s", $localidade);
$stmt2->execute();
$result = $stmt2->get_result();

$premios = [];

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $premios[] = $row["premio"];
    }
} else {
    $_SESSION['erro'] = "acabau_premio";
    $stmt2->close();
    header("Location:index.php");
    die();
}
$stmt2->close();

// ── 4. Sorteia o prêmio e mapeia para posição da roleta ───────────────────────
$indice_premio = rand(0, count($premios) - 1);
$premio_sorteado = $premios[$indice_premio];

$roleta = 0;

switch ($premio_sorteado) {
    case "desconto 120 reais":
        $posicoes = [3, 10];
        break;
    case "desconto 60 reais":
        $posicoes = [1, 9];
        break;
    case "1 mês de internet grátis":
        $posicoes = [4, 7];
        break;
    case "2 meses de internet grátis":
        $posicoes = [6];
        break;
    case "3 meses de internet grátis":
        $posicoes = [11];
        break;
    case "50% de desconto na taxa de instalação":
        $posicoes = [2, 8];
        break;
    case "Taxa de instalação grátis":
        $posicoes = [5, 12];
        break;
    default:
        $posicoes = [4];
        break;
}
$roleta = $posicoes[array_rand($posicoes)];

// ── 5. Insere o usuário no banco ──────────────────────────────────────────────
$stmt3 = $conn->prepare(
    "INSERT INTO usuarios(nome, cpf, email, telefone, cep, endereco, bairro, cidade, estado, premio, canal_origem, status)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'reservado')"
);
$stmt3->bind_param(
    "sssssssssss",
    $nome_usuario,
    $cpf_usuario,
    $email_usuario,
    $telefone_usuario,
    $cep_usuario,
    $endereco_usuario,
    $bairro_usuario,
    $cidade_usuario,
    $estado_usuario,
    $premio_sorteado,
    $canal
);
$stmt3->execute();
$stmt3->close();

// ── 6. Decrementa estoque do prêmio ──────────────────────────────────────────
$stmt4 = $conn->prepare("UPDATE premios SET quantidade = quantidade - 1 WHERE localidade = ? AND premio = ?");
$stmt4->bind_param("ss", $localidade, $premio_sorteado);
$stmt4->execute();
$stmt4->close();

$_SESSION['premio'] = $roleta;

header("Location:index.php");
die();
