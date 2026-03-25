<!DOCTYPE html>
<?php

if(!isset($_SESSION)){
    session_start();
}

if(!isset($_SESSION['logado']) || $_SESSION['logado'] != true){
    header("Location:login.php");
}

function horasEntreDatas($data){
    $datatime2 = new DateTime("now");
    $datatime1 = new DateTime($data);
    
    $data1 = $datatime1->format('Y-m-d H:i:s');
    $data2 = $datatime2->format('Y-m-d H:i:s');
    
    $diff = $datatime1->diff($datatime2);
    $horas = $diff->h + ($diff->days * 24);
    return $horas;
}

function retornaLocalidade($cidade_usuario, $bairro_usuario){
    if ($bairro_usuario == 'Cassino') {
        $localidade = 'cassino';
    } elseif ($cidade_usuario == 'Rio Grande') {
        $localidade = 'rio grande';
    } elseif ($cidade_usuario == 'Pelotas') {
        $localidade = 'pelotas';
    } elseif ($cidade_usuario == 'São José do Norte') {
        $localidade = 'sjn';
    }
    return $localidade;
}

?>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>Roleta Digital - Vetorial Internet</title>

        <!-- css -->
        <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
        <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
        <link href="css/nivo-lightbox.css" rel="stylesheet" />
        <link href="css/nivo-lightbox-theme/default/default.css" rel="stylesheet" type="text/css" />
        <link href="css/animate.css" rel="stylesheet" />
        <link href="css/style.css" rel="stylesheet">
        <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
        <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
        <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>

        <!-- template skin -->
        <link id="t-colors" href="color/default.css" rel="stylesheet">

        <!-- =======================================================
          Theme Name: Appland
          Theme URL: https://bootstrapmade.com/free-bootstrap-app-landing-page-template/
          Author: BootstrapMade
          Author URL: https://bootstrapmade.com
        ======================================================= -->
    </head>

    <body id="page-top" data-spy="scroll" data-target=".navbar-custom">


        <div id="wrapper">

            <nav class="navbar navbar-custom" role="navigation">
                <div class="container navigation">

                    <div class="navbar-header page-scroll">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse">
                            <i class="fa fa-bars"></i>
                        </button>
                        <a class="navbar-brand" href="index.html">
                            <img src="img/logo.png" alt="" width="150" height="40" />
                        </a>
                    </div>

                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
                        <ul class="nav navbar-nav">
                            <li>
                                <div id="cart"></div>
                                            <li class="active"><a href="sair.php">Sair</a></li>

                            </li>
                            
                        </ul>
                    </div>
                    <!-- /.navbar-collapse -->

                </div>
                <!-- /.container -->
            </nav>

                <div class="container">
                    <div class="row text-center heading">
                        <h2>Lista de Clientes</h2>
                    </div>


                    <div class="row">
                        <div class="col-md-12">
                            <table id="example" class="display" style="width:100%">
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>Name</th>
                                        <th>CPF</th>
                                        <th>Endereço</th>
                                        <th>Status</th>
                                        <th>Premio</th>
                                        <th>Data</th>
                                        <th>Responsável</th>
                                        <th>Canal de Origem</th>
                                        <th>Ações</th>

                                    </tr>
                                </thead>
                                <tbody>
                                    <?php
                                    include_once("./conexao.php");

                                    $result_usuarios = "SELECT * FROM usuarios";
                                    $resultado_usuarios = mysqli_query($conn, $result_usuarios);
                                    while ($row_usuario = mysqli_fetch_assoc($resultado_usuarios)) {
                                        echo"<tr>";
                                        echo "<td>" . $row_usuario['ID'] . "</td>";
                                        echo "<td>" . htmlspecialchars($row_usuario['nome']) . "</td>";
                                        // Mascarar CPF: mostra apenas os primeiros 3 e últimos 2 dígitos
                                        $cpf_raw = preg_replace('/\D/', '', $row_usuario['cpf']);
                                        $cpf_mask = strlen($cpf_raw) === 11
                                            ? substr($cpf_raw, 0, 3) . '.xxx.xxx-' . substr($cpf_raw, -2)
                                            : '***';
                                        echo "<td>" . $cpf_mask . "</td>";

                                        echo "<td>" . $row_usuario['endereco'] . "</td>";
                                        echo "<td>" . $row_usuario['status'] . "</td>";
                                        echo "<td>" . $row_usuario['premio'] . "</td>";
                                        echo "<td>" . $row_usuario['data_giro'] . "</td>";
                                        echo "<td>" . $row_usuario['responsavel_status'] . "</td>";
                                        echo "<td>" . $row_usuario['canal_origem'] . "</td>";
                                        if(horasEntreDatas($row_usuario['data_giro']) > 28 && $row_usuario['status'] == 'reservado'){
                                            $premio_atual = $row_usuario['premio'];
                                            $loc_expirado = retornaLocalidade($row_usuario['cidade'], $row_usuario['bairro']);
                                            // Atualiza status do usuário para "expirou"
                                            $st_exp_u = $conn->prepare("UPDATE usuarios SET status = 'expirou', responsavel_status = 'sistema' WHERE ID = ?");
                                            $st_exp_u->bind_param("i", $row_usuario['ID']);
                                            $st_exp_u->execute();
                                            $st_exp_u->close();
                                            // Devolve o prêmio ao estoque
                                            $st_exp_p = $conn->prepare("UPDATE premios SET quantidade = quantidade + 1 WHERE premio = ? AND localidade = ?");
                                            $st_exp_p->bind_param("ss", $premio_atual, $loc_expirado);
                                            $st_exp_p->execute();
                                            $st_exp_p->close();

                                            echo '<td> <button type="button" class="btn btn-danger">Passou 24h</button></td>';
                                        }elseif($row_usuario['status'] == 'expirou'){
                                            echo '<td> <button type="button" class="btn btn-danger">Passou 24h</button></td>';
                                        }else{
                                            echo '<td> <button type="button" class="btn btn-success" onclick="seleciona_id_contratou(' . ($row_usuario['ID'] + 0) . ')" data-toggle="modal" data-target="#modalcontratou">Validação</button></td>';
                                        }
                                        echo "</tr>";
                                    }
                                    ?>
                                </tbody>
                                <tfoot>
                                    <tr>
                                        <th>Id</th>
                                        <th>Name</th>
                                        <th>CPF</th>
                                        <th>Endereço</th>
                                        <th>Status</th>
                                        <th>Premio</th>
                                        <th>Data</th>
                                        <th>Responsável</th>
                                        <th>Canal de Origem</th>
                                        <th>Ações</th>

                                    </tr>
                                </tfoot>
                            </table>

                            <script>
                                $(document).ready(function () {
                                    $('#example').DataTable();
                                });
                            </script>
                        </div>
                    </div>
                </div>

            </section>
            <!-- /Section: content -->


        </div>
        <!-- Modal Contratou-->
        <div id="modalcontratou" class="modal fade" role="dialog">
            <div class="modal-dialog">

                <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <h4 class="modal-title">Contratou</h4>
                    </div>
                    <div class="modal-body">
                        <form id="validacao" action="status.php" method="post">
                            <input type="hidden" id="id_contratou" name="id_cliente" value="">
                            <input type="hidden" id="id_botao" name="botao" value="">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-group">
                                        <label for="exampleInputEmail1">Responsável:</label>
                                        <input  type="text" class="form-control" id="nomeresponsavel" name ="nomeresponsavel" id="nomeresponsavel" required>
                                    </div>
                                </div> 
                                
                        </form>
                    </div>
                            </div>
                    <div class="modal-footer">
                        <div class="row">
                            <div class="col-md-5">
                            <button type="button" class="btn btn-info" onclick="botao('aguardando_retorno')">Aguardando retorno</button>
                            </div>
                            <div class="col-md-3">
                                <button type="button" class="btn btn-success" onclick="botao('contratou')">Contratou</button>
                            </div>
                            <div class="col-md-4">
                            <button type="button" class="btn btn-danger" onclick="botao('nao_contratou')">Não contratou</button>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <div class="row">
                            <div class="col-md-4">
                                <button type="button" class="btn btn-warning" onclick="botao('analisefinanceira')" >Reprovou SPC</button>
                            </div>
                            <div class="col-md-4">
                                <button type="button" class="btn btn-primary" onclick="botao('inviavelcani')" >Inviavel Cani</button>
                            </div>
                            <div class="col-md-4">
                                <button type="button" class="btn btn-danger" onclick="botao('inviabilidadetec')" >Inviavel Tecnico</button>
                            </div>
                            
                        </div>
                    </div>
                </div>

            </div>
        </div>


        <script>
            function seleciona_id_contratou(id_cliente) {
                $("#id_contratou").val(id_cliente);
                
            }
        </script> 
        <script>
            function botao(nome) {
                if($("#nomeresponsavel").val().length > 3){
                    $("#id_botao").val(nome);
                    $("#validacao").submit();
                }else{
                    alert("Preencha o nome do responsável!")
                }
            }
        </script>
        <a href="#" class="scrollup"><i class="fa fa-angle-up active"></i></a>

        <!-- Core JavaScript Files -->
        <script src="js/bootstrap.min.js"></script>
        <script src="js/jquery.easing.min.js"></script>
        <script src="js/wow.min.js"></script>
        <script src="js/jquery.scrollTo.js"></script>
        <script src="js/nivo-lightbox.min.js"></script>
        <script src="js/custom.js"></script>

    </body>

</html>
