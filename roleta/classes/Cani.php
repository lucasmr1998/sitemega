<?php

require_once "Utils.php";

class Cani{
    
    public function __construct(){
        Utils::iniciarSessao();        
    }

    private $cep = 0, $numero = 0;

    public function consultaCEP($cep, $numero){
        
        if($this->cep == $cep && $this->numero == $numero){
            return array("response" => "success");
        }else{
            if(strlen(Utils::soNumero($cep)) != 8){
                return array("response" => "error", "message" => "tamanho errado de cpf");
            } 
            if($cep == '96225000'){
                $_SESSION['cidade'] = "São José do Norte";
                $_SESSION['tecnologia'] = "ftth";
                $_SESSION['enderecoComp'] = "São José do Norte";
                return array("response" => "success");
            }
            $post = [
                'funcao' => 'viab',
                'chave_acesso' => 'b4eb124c259f3ce1fb2da7a4dbe0373d',
                'cep' => "$cep",
                'num' => "$numero"
            ];
            
            $ch = curl_init('https://canicontrol.vetorial.net/api/externo/viabilidade.php');
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
            
            $curl_response = curl_exec($ch);
            
            if($curl_response === false){
                return array("response" => "error", "message" => "erro ao executar curl");
            }

            curl_close($ch);
            $json_response = json_decode($curl_response,true);
            Utils::debug($json_response);
            if(sizeof($json_response) < 1){
                $_SESSION['cidade'] = "nao_encontrada";
                $_SESSION['tecnologia'] = "nao_encontrada";
                $_SESSION['enderecoComp'] = "nao_encontrada";
                return array("response" => "success");
            }else{
                $_SESSION['cidade'] = $json_response['cidade'];
                $_SESSION['enderecoComp'] = $json_response['enderecoComp'];
                $tecnologia = null;
                foreach ($json_response['viabilidade'] as $key => $value) {
                    if(is_null($tecnologia)){
                        $tecnologia = $key;
                    }elseif($tecnologia == 'ftth'){
                        break;
                    }elseif($tecnologia == 'rf'){
                        $tecnologia = $key;
                    }elseif($tecnologia == 'fttn' && $key == 'ftth'){
                        $tecnologia = $key;
                    }
                }
                $_SESSION['tecnologia'] = $tecnologia;
                //die("$tecnologia");
                return array("response" => "success");
            }
        }
    }

    public static function consultaTecnologia(){
        Utils::iniciarSessao();
        if(!isset($_SESSION['tecnologia'])){
            //TODO: redireciona para a tela de localidade, verificar solucao
            Utils::redirecionaLocal("localidades/index.php");
        }else{
            return $_SESSION['tecnologia'];
        }
    }
    public static function consultaCidade(){
        Utils::iniciarSessao();
        if(!isset($_SESSION['cidade'])){
            //TODO: redireciona para a tela de localidade, verificar solucao
            Utils::redirecionaLocal("localidades/index.php");
        }else{
            return $_SESSION['cidade'];
        }
    }
    public static function consultaEndereco(){
        Utils::iniciarSessao();
        if(!isset($_SESSION['enderecoComp'])){
            //TODO: redireciona para a tela de localidade, verificar solucao
            Utils::redirecionaLocal("localidades/index.php");
        }else{
            return $_SESSION['enderecoComp'];
        }
    }

}