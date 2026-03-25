<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <title>CRUD - Listar</title>
        
        <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
        <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
        <script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>

    </head>
    <body>
        <h1>Listar Usuário</h1>
        <br>
        <table id="example" class="display" style="width:100%">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>CPF</th>
                    <th>Premio</th>
                </tr>
            </thead>
            <tbody>
                <?php
                include_once("../conexao.php");

                $result_usuarios = "SELECT * FROM usuarios";
                $resultado_usuarios = mysqli_query($conn, $result_usuarios);
                while ($row_usuario = mysqli_fetch_assoc($resultado_usuarios)) {
                    echo"<tr>";
                    echo "<td>" . $row_usuario['nome'] . "</td>";
                    echo "<td>" . substr($row_usuario['cpf'], 0,3) . "</td>";
                    echo "<td>" . $row_usuario['premio'] . "</td>";
                    echo "</tr>";
                }
                ?>
            </tbody>
            <tfoot>
                <tr>
                    <th>Name</th>
                    <th>CPF</th>
                    <th>Premio</th>
                </tr>
            </tfoot>
        </table>

        <script>
        $(document).ready(function() {
            $('#example').DataTable();
        } );
        </script>
    </body>
</html>
</body>
</html>