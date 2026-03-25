<?php
    $servidor = "srv1078.hstgr.io";
    $usuario  = "u635775069_megalink";
    $senha    = "Gremio271293@";
    $dbname   = "u635775069_megalink";

    // Criar a conexão
    $conn = mysqli_connect($servidor, $usuario, $senha, $dbname);
    mysqli_set_charset($conn, "utf8mb4");

    if (!$conn) {
        die("Falha na conexão: " . mysqli_connect_error());
    }
?>