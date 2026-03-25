<?php
/**
 * Authentication Helper Functions
 * Manages user sessions and login/logout functionality
 */

// Start session if not already started
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Admin credentials (in production, use database with hashed passwords)
define('ADMIN_USERNAME', 'admin');
define('ADMIN_PASSWORD', 'ABCSTGMEGA@2026'); // Change this to a secure password

/**
 * Check if user is logged in
 */
function isLoggedIn() {
    return isset($_SESSION['admin_logged_in']) && $_SESSION['admin_logged_in'] === true;
}

/**
 * Validate login credentials
 */
function validateLogin($username, $password) {
    if ($username === ADMIN_USERNAME && $password === ADMIN_PASSWORD) {
        $_SESSION['admin_logged_in'] = true;
        $_SESSION['admin_username'] = $username;
        $_SESSION['login_time'] = time();
        return true;
    }
    return false;
}

/**
 * Logout user
 */
function logout() {
    session_unset();
    session_destroy();
}

/**
 * Require login - redirect to login page if not authenticated
 */
function requireLogin() {
    if (!isLoggedIn()) {
        header('Location: login.php');
        exit;
    }
}

/**
 * Get logged in username
 */
function getLoggedInUser() {
    return $_SESSION['admin_username'] ?? null;
}

/**
 * Check session timeout (optional - 2 hours)
 */
function checkSessionTimeout($timeout = 7200) {
    if (isset($_SESSION['login_time'])) {
        $elapsed = time() - $_SESSION['login_time'];
        if ($elapsed > $timeout) {
            logout();
            return false;
        }
        // Update login time
        $_SESSION['login_time'] = time();
    }
    return true;
}
?>
