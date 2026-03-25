<?php

include_once("conexao.php");

if (!isset($_SESSION)) {
    session_start();
}

// ── Helpers ───────────────────────────────────────────────────────────────────
function retornaLocalidade($cidade_usuario, $bairro_usuario) {
    if ($bairro_usuario == 'Cassino') {
        return 'cassino';
    } elseif ($cidade_usuario == 'Rio Grande') {
        return 'rio grande';
    } elseif ($cidade_usuario == 'Pelotas') {
        return 'pelotas';
    } elseif ($cidade_usuario == 'São José do Norte') {
        return 'sjn';
    }
    return 'rio grande';
}

function devolve_premio($conn, $premio_atual, $localidade) {
    $st = $conn->prepare("UPDATE premios SET quantidade = quantidade + 1 WHERE premio = ? AND localidade = ?");
    $st->bind_param("ss", $premio_atual, $localidade);
    $st->execute();
    $st->close();
}

function insere_log($conn, $responsavel, $acao_nova, $acao_antiga, $aonde) {
    $st = $conn->prepare("INSERT INTO logs(responsavel, acao_nova, acao_antiga, aonde) VALUES (?, ?, ?, ?)");
    $st->bind_param("ssss", $responsavel, $acao_nova, $acao_antiga, $aonde);
    $st->execute();
    $st->close();
}

function atualiza_status($conn, $novo_status, $responsavel, $id_cliente) {
    $st = $conn->prepare("UPDATE usuarios SET status = ?, responsavel_status = ? WHERE ID = ?");
    $st->bind_param("ssi", $novo_status, $responsavel, $id_cliente);
    $st->execute();
    $st->close();
}

// ── Valida entrada ────────────────────────────────────────────────────────────
if (empty($_POST['id_cliente']) || !is_numeric($_POST['id_cliente'])) {
    header('Location: ./listar_usuarios.php');
    die();
}

$id_cliente  = (int) $_POST['id_cliente'];
$botao       = $_POST['botao'] ?? '';
$responsavel = trim($_POST['nomeresponsavel'] ?? '');

// ── Carrega dados do cliente ──────────────────────────────────────────────────
$stmt = $conn->prepare("SELECT * FROM usuarios WHERE ID = ?");
$stmt->bind_param("i", $id_cliente);
$stmt->execute();
$resultado = $stmt->get_result();
$row_usuario = $resultado->fetch_assoc();
$stmt->close();

if (!$row_usuario) {
    header('Location: ./listar_usuarios.php');
    die();
}

$premio_atual = $row_usuario['premio'];
$status_atual = $row_usuario['status'];
$aonde        = $row_usuario['nome'];
$localidade   = retornaLocalidade($row_usuario['cidade'], $row_usuario['bairro']);

// ── Processa ação ─────────────────────────────────────────────────────────────
switch ($botao) {

    case "contratou":
        if ($status_atual != "contratou") {
            insere_log($conn, $responsavel, $botao, $status_atual, $aonde);
            atualiza_status($conn, 'contratou', $responsavel, $id_cliente);
        }
        break;

    case "aguardando_retorno":
        if ($status_atual != "Aguardando retorno") {
            insere_log($conn, $responsavel, $botao, $status_atual, $aonde);
            atualiza_status($conn, 'Aguardando Retorno', $responsavel, $id_cliente);
        }
        break;

    case "nao_contratou":
        if ($status_atual == "reservado" || $status_atual == "contratou") {
            devolve_premio($conn, $premio_atual, $localidade);
        }
        if ($status_atual != "Não contratou") {
            insere_log($conn, $responsavel, $botao, $status_atual, $aonde);
            atualiza_status($conn, 'Não contratou', $responsavel, $id_cliente);
        }
        break;

    case "inviabilidadetec":
        if ($status_atual == "reservado" || $status_atual == "contratou") {
            devolve_premio($conn, $premio_atual, $localidade);
        }
        if ($status_atual != "Inviavel Tecnicamente") {
            insere_log($conn, $responsavel, $botao, $status_atual, $aonde);
            atualiza_status($conn, 'Inviavel Tecnicamente', $responsavel, $id_cliente);
        }
        break;

    case "inviavelcani":
        if ($status_atual == "reservado" || $status_atual == "contratou") {
            devolve_premio($conn, $premio_atual, $localidade);
        }
        if ($status_atual != "Inviavel Cani") {
            insere_log($conn, $responsavel, $botao, $status_atual, $aonde);
            atualiza_status($conn, 'Inviavel Cani', $responsavel, $id_cliente);
        }
        break;

    case "analisefinanceira":
        if ($status_atual == "reservado" || $status_atual == "contratou") {
            devolve_premio($conn, $premio_atual, $localidade);
        }
        if ($status_atual != "Reprovou no SPC") {
            insere_log($conn, $responsavel, $botao, $status_atual, $aonde);
            atualiza_status($conn, 'Reprovou SPC', $responsavel, $id_cliente);
        }
        break;
}

header('Location: ./listar_usuarios.php');
die();
?>