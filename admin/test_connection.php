<?php
/**
 * Database Connection Test Script
 * This script helps diagnose connection issues
 */

echo "<h1>PostgreSQL Connection Test</h1>";
echo "<pre>";

// Check if PDO PostgreSQL driver is installed
echo "1. Checking PDO PostgreSQL driver...\n";
if (extension_loaded('pdo_pgsql')) {
    echo "   ✓ PDO PostgreSQL driver is installed\n\n";
} else {
    echo "   ✗ PDO PostgreSQL driver is NOT installed\n";
    echo "   Please install it with: sudo apt-get install php-pgsql\n\n";
    exit;
}

// Database credentials
$host = '187.62.153.52';
$port = '5432';
$dbname = 'frota24_leads';
$user = 'admin';
$password = 'qualidade@trunks.57';

echo "2. Connection parameters:\n";
echo "   Host: $host\n";
echo "   Port: $port\n";
echo "   Database: $dbname\n";
echo "   User: $user\n\n";

// Test connection
echo "3. Attempting to connect...\n";
try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$dbname";
    $pdo = new PDO($dsn, $user, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_TIMEOUT => 5
    ]);
    
    echo "   ✓ Connection successful!\n\n";
    
    // Test query
    echo "4. Testing query...\n";
    $stmt = $pdo->query("SELECT version()");
    $version = $stmt->fetch(PDO::FETCH_ASSOC);
    echo "   PostgreSQL Version: " . $version['version'] . "\n\n";
    
    // List tables
    echo "5. Listing tables...\n";
    $stmt = $pdo->query("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'");
    $tables = $stmt->fetchAll(PDO::FETCH_COLUMN);
    
    if (count($tables) > 0) {
        echo "   Tables found:\n";
        foreach ($tables as $table) {
            echo "   - $table\n";
        }
    } else {
        echo "   No tables found in public schema\n";
    }
    
    echo "\n6. Checking 'leads_frota' table...\n";
    try {
        $stmt = $pdo->query("SELECT COUNT(*) as count FROM leads_frota");
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        echo "   ✓ 'leads_frota' table exists\n";
        echo "   Total records: " . $result['count'] . "\n\n";
        
        // Show table structure
        echo "7. Table structure:\n";
        $stmt = $pdo->query("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'leads_frota' ORDER BY ordinal_position");
        $columns = $stmt->fetchAll(PDO::FETCH_ASSOC);
        foreach ($columns as $col) {
            echo "   - {$col['column_name']} ({$col['data_type']})\n";
        }
        
    } catch (PDOException $e) {
        echo "   ✗ Error accessing 'leads_frota' table: " . $e->getMessage() . "\n";
        echo "   The table might not exist or you don't have permission to access it.\n";
    }
    
} catch (PDOException $e) {
    echo "   ✗ Connection failed!\n";
    echo "   Error: " . $e->getMessage() . "\n\n";
    
    echo "Possible issues:\n";
    echo "   - The database server might be down or unreachable\n";
    echo "   - The IP address might be blocked by firewall\n";
    echo "   - The credentials might be incorrect\n";
    echo "   - The database name might not exist\n";
    echo "   - PostgreSQL might not be configured to accept remote connections\n";
}

echo "</pre>";
?>
