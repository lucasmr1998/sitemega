<?php
if (!isset($_SESSION)) {
    session_start();
}
// Endpoint AJAX — destrói a sessão do prêmio após o giro concluir
// Evita que o usuário atualize a página e gire novamente
if (isset($_SESSION['premio'])) {
    unset($_SESSION['premio']);
}
http_response_code(200);
echo json_encode(['ok' => true]);
?>
