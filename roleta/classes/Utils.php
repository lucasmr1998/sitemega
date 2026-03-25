<?php

// init.php
// Ficheiro de inicialização de configurações gerais
define('ROOT',$_SERVER['DOCUMENT_ROOT']);

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require_once ROOT.'/vendor/autoload.php';

class Utils{

    public static $http = "http";

    public static function soNumero($str) {
        return preg_replace("/[^0-9]/", "", $str);
    }

    public static function redireciona($url){
        header("Location:".self::$http."://$url");
    }

    public static function redirecionaLocal($url){
        header("Location:" . self::$http ."://" . $_SERVER[HTTP_HOST] . "/" .$url);
    }

    public static function mostraErros(){
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);
    }

    public static function iniciarSessao(){
        if(!isset($_SESSION)){
            session_start();
        }
    }

    public static function debug($var){
        echo "<pre>";
        print_r($var);
        echo "</pre>";
    }

    public static function diebug($var){
        echo "<pre>";
        print_r($var);
        echo "</pre>";
        die();
    }

    public static function temLocalidade(){
        return isset($_SESSION['tecnologia']);
    }
    //TODO: Verificar o destinatário padrão
    public static function enviaEmail($assunto, $mensagem, $destinatario = "'hallanneves@gmail.com'"){
        
        $mail = new PHPMailer(true);
        try {
            $mail->SMTPDebug = 0;
            $mail->isSMTP();
            $mail->CharSet = 'UTF-8';
            $mail->SMTPAuth = true;
            $mail->Host = 'mail.devopers.com.br';
            $mail->Username = 'hallan@devopers.com.br';
            $mail->Password = '99427489';
            $mail->SMTPSecure = 'tls';
            $mail->Port = 587;

            $mail->setFrom('hallan@devopers.com.br', 'Hallan DevOpers');
            $mail->addAddress($destinatario);

            $mail->isHTML(true);
            $mail->Subject = $assunto;
            $mail->Body    = $mensagem;

            $mail->send();
        } catch (Exception $e) {
            echo 'Message could not be sent. Mailer Error: ', $mail->ErrorInfo;
        }
    }

}
