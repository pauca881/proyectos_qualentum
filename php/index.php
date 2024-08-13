<!DOCTYPE html>
<!-- PT Pau Cañizares-->
<html>
<head>
    <title>Formulario Lab0</title>
</head>
<body>
    <h1>Información usuario</h1>
    <form action="index.php" method="post">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre" required><br><br>

        <label for="edad">Edad:</label>
        <input type="number" id="edad" name="edad" required><br><br>

        <label for="color">Color favorito:</label>
        <input type="text" id="color" name="color" required><br><br>

        <input type="submit" value="Enviar">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = isset($_POST['nombre']) ? $_POST['nombre'] : '';
        $edad = isset($_POST['edad']) ? $_POST['edad'] : '';
        $color = isset($_POST['color']) ? $_POST['color'] : '';

        function generar_array($nombre, $edad, $color) {
            return array(
                "nombre" => $nombre,
                "edad" => $edad,
                "color" => $color
            );
        }

        function guardar_fichero($array) {
            if ($array['edad'] < 18) {
                $file = 'menores_17.txt';
            } elseif ($array['edad'] >= 18 && $array['edad'] < 30) {
                $file = 'entre_18_30.txt';
            } else {
                $file = 'mayores_30.txt';
            }

            $contenido = "El usuario {$array['nombre']} tiene como color favorito {$array['color']} \n";
            file_put_contents($file, $contenido, FILE_APPEND);
        }

        if ($nombre != '' && $edad != '' && $color != '') {
            $array_asociativo = generar_array($nombre, $edad, $color);
            guardar_fichero($array_asociativo);
            echo "Script finalizado";
        } else {
            echo "No se ha recibido ninguna información";
        }
    }
    ?>
</body>
</html>
