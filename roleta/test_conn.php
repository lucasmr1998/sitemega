<?php
// DIAGNÓSTICO TEMPORÁRIO — REMOVA APÓS O TESTE
echo "<h3>Extensões MySQL disponíveis:</h3>";
echo "<p>mysqli: " . (extension_loaded('mysqli') ? '✅ SIM' : '❌ NÃO') . "</p>";
echo "<p>pdo_mysql: " . (extension_loaded('pdo_mysql') ? '✅ SIM' : '❌ NÃO') . "</p>";
echo "<p>pdo: " . (extension_loaded('pdo') ? '✅ SIM' : '❌ NÃO') . "</p>";
echo "<h3>Versão PHP: " . PHP_VERSION . "</h3>";
echo "<h3>Arquivo php.ini carregado:</h3><p>" . php_ini_loaded_file() . "</p>";
echo "<h3>Todas as extensões:</h3><pre>" . implode(', ', get_loaded_extensions()) . "</pre>";
?>
