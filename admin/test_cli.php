<?php
// Check table structure
$host = '187.62.153.52';
$port = '5432';
$dbname = 'frota24_leads';
$user = 'admin';
$password = 'qualidade@trunks.57';

try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$dbname";
    $pdo = new PDO($dsn, $user, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
    ]);
    
    echo "Estrutura da tabela 'leads_frota':\n";
    echo "==================================\n\n";
    
    $stmt = $pdo->query("SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = 'leads_frota' ORDER BY ordinal_position");
    $columns = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    foreach ($columns as $col) {
        echo "- {$col['column_name']}\n";
        echo "  Tipo: {$col['data_type']}\n";
        echo "  Nullable: {$col['is_nullable']}\n\n";
    }
    
    echo "\nPrimeiros 2 registros:\n";
    echo "=====================\n\n";
    
    $stmt = $pdo->query("SELECT * FROM leads_frota LIMIT 2");
    $leads = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    foreach ($leads as $i => $lead) {
        echo "Registro " . ($i + 1) . ":\n";
        foreach ($lead as $key => $value) {
            echo "  $key: $value\n";
        }
        echo "\n";
    }
    
} catch (PDOException $e) {
    echo "Erro: " . $e->getMessage() . "\n";
}
?>
