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
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Ptasia Maska</title>
</head>
<body>
    <?php
    error_reporting(0);
    if($_SESSION['feedback']=="success")
    {
        echo '<div class="alert alert-warning alert-dismissible fade show alert-fixed" role="alert">
            Zalogowano pomyślnie
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>';
        unset($_SESSION['feedback']);
    }
    echo "<div style='background-color: blue; height: 40px; display:block;'>";
    echo "<img src='logo.png' style='height: 40px;'>";
    echo "<a style='pointer-events: none; color:yellow;'> Strona Główna </a>";
    echo "<a href='info.php' style='color:white;'> Informacje </a>";
    echo "<a href='covid.php' style='color:white;'> Covid </a>";
    if(isset($_SESSION['name']))
    {
        echo "<a href='closevisits.php' style='color:white;'> Najbliższe Wizyty </a>";
        echo "<a href='arrange.php' style='color:white;'> Umów Wizytę </a>";
        echo "<a href='history.php' style='color:white;'> Historia Wizyt </a>";
        echo "<div class='login' style='float:right; display:'inline-block'>
        <div style='color:white;'> Witaj ". $_SESSION['name'] ."
        <button class='btn btn-primary' onclick='redirect()' type='submit' method='post'>Wyloguj</button>
    </div></div>";
    }
    else if(isset($_SESSION['admin']))
    {
        echo "<a href='summary.php' style='color:white;'> Podsumowanie </a>";
        echo "<a href='doctors.php' style='color:white;'> Lekarze </a>";
        echo "<a href='patients.php' style='color:white;'> Pacjenci </a>";
        echo "<a href='visits.php' style='color:white;'> Wizyty </a>";
        echo "<div class='login' style='float:right; display:'inline-block'>
        <div style='color:white;'> Bądź pozdrowiony ". $_SESSION['admin'] ."
        <button class='btn btn-primary' onclick='redirect()' type='submit' method='post'>Wyloguj</button>
    </div></div>";
    }
    else
    {
        echo "<div class='login' style='float:right;'>
        <button class='btn btn-primary' onclick='login()' type='submit'>Zaloguj</button>
    </div></div>";
    }
    echo "</div>";
    ?>
    <h1>Witamy w przychodni Ptasia Maska<h1>
    <img src="logo.png">
    <script>
        function redirect()
        {
            window.location.href = "logout.php";
        }
        function login()
        {
            window.location.href = "index.php";
        }
    </script>
</body>
</html>