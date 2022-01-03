<?php
if (!isset($_SESSION)) {
    session_start();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    error_reporting(0);
    unset($_SESSION['name']);
    unset($_SESSION['admin']);
    unset($_SESSION['index']);
    ?>
    <script>
        window.location.href = "main.php";
    </script>
</body>
</html>