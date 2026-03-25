<?php

if(!isset($_SESSION)){
    session_start();
}

if($_POST['usuario'] == 'vetorial@vetorial.net' && $_POST['senha'] == 'vetorial'){
    $_SESSION['logado'] = true;
    header("Location:listar_usuarios.php");
}else{
    echo "Senha ou usuario invalidos!";
}
