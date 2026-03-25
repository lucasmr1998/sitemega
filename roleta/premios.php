<!DOCTYPE html>
<?php

if(!isset($_SESSION)){
    session_start();
}

if(!isset($_SESSION['logado']) || $_SESSION['logado'] != true){
    header("Location:login.php");
}

?>
<!DOCTYPE html>
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
                            </li>
                            <!-- MENU -->

                        </ul>
                    </div>
                    <!-- /.navbar-collapse -->

                </div>
                <!-- /.container -->
            </nav>

            <section id="content1" class="home-section">

                <div class="container">
                    <div class="row text-center heading">
                        <h3>Lista de Premios</h3>
                    </div>


                    <div class="row">
                        <div class="col-md-12">
                            <table id="example" class="display" style="width:100%">
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>Premio</th>
                                        <th>Quantidade</th>
                                        <th>Localidade</th>
                                        <th>Ações</th>

                                    </tr>
                                </thead>
                                <tbody>
                                    <?php
                                    include_once("./conexao.php");

                                    $result_premios = "SELECT * FROM premios";
                                    $resultado_premios = mysqli_query($conn, $result_premios);
                                    while ($row_premio = mysqli_fetch_assoc($resultado_premios)) {
                                        echo"<tr>";
                                        echo "<td>" . $row_premio['id'] . "</td>";
                                        echo "<td>" . $row_premio['premio'] . "</td>";
                                        echo "<td>" . $row_premio['quantidade'] . "</td>";
                                        echo "<td>" . $row_premio['localidade'] . "</td>";
                                        echo '<td> <button type="button" class="btn btn-success" onclick="seleciona_id_premio(' . $row_premio['id'] . ')" data-toggle="modal" data-target="#modalpremio">Editar</button>
 </td>';
                                        echo "</tr>";
                                    }
                                    ?>
                                </tbody>
                                <tfoot>
                                    <tr>
                                        <th>ID</th>
                                        <th>Premio</th>
                                        <th>Quantidade</th>
                                        <th>Localidade</th>
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
        <div id="modalpremio" class="modal fade" role="dialog">
            <div class="modal-dialog">

                <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <h4 class="modal-title">Editar - Prêmio</h4>
                    </div>
                    <div class="modal-body">
                        <form id="validacao" action="atualiza_premio.php" method="post">
                            <input type="hidden" id="id_premio" name="id_premio" value="">
                            <input type="hidden" id="id_botao" name="botao" value="">
                            <div class="row">
                                <div class="col-md-12">
                                    <div class="form-group">
                                        <label for="exampleInputEmail1">Prêmio:</label>
                                        <input  type="text" class="form-control" name ="premio_nome" id="premio_nome" required>
                                        <label for="exampleInputEmail1">Quantidade:</label>
                                        <input  type="text" class="form-control" name ="premio_qtd" id="premio_qtd" required>
                                        <label for="exampleInputEmail1">Localidade:</label>
                                        <input  type="text" class="form-control" name ="premio_local" id="premio_local" required>
                                    </div>
                                </div> 

                        </form>
                    </div>
                </div>
                <div class="modal-footer">

                    <button type="button" class="btn btn-success" onclick="botao('editar')">Editar</button>;

                </div>

            </div>

        </div>
    </div>


    <script>
        function seleciona_id_premio(id_premio) {
            $("#id_premio").val(id_premio);
        }
    </script> 
    <script>
        function botao(nome) {
            if ($("#premio_nome").val().length > 3) {
                $("#id_botao").val(nome);
                $("#validacao").submit();
            } else {
                alert("preencha o mimimim")
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
