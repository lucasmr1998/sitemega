<?php

include_once("./conexao.php");

if (!isset($_SESSION)) {
    session_start();
}

// Somente admins logados podem acessar
if (!isset($_SESSION['logado']) || $_SESSION['logado'] !== true) {
    header("Location: login.php");
    die();
}

if ($_POST['botao'] === "editar") {
    $premio_nome  = trim($_POST['premio_nome']);
    $premio_qtd   = (int) $_POST['premio_qtd'];
    $premio_local = trim($_POST['premio_local']);
    $id_premio    = (int) $_POST['id_premio'];

    $stmt = $conn->prepare("UPDATE premios SET premio = ?, quantidade = ?, localidade = ? WHERE id = ?");
    $stmt->bind_param("sisi", $premio_nome, $premio_qtd, $premio_local, $id_premio);

    if ($stmt->execute()) {
        $stmt->close();
        header('Location: ./premios.php');
        die();
    } else {
        $stmt->close();
        header('Location: ./premios.php?erro=1');
        die();
    }
}

header('Location: ./premios.php');
die();
?>