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
    echo "<div style='background-color: blue; height: 40px; display:block;'>";
    echo "<img src='logo.png' style='height: 40px;'>";
    echo "<a href='main.php'style='color:white;'> Strona Główna</a>";
    echo "<a href='info.php' style='color:white'> Informacje </a>";
    echo "<a style='pointer-events: none; color:yellow;'> Covid </a>";
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
    ?>
    <h1>Przychodnia Ptasia Maska informuje:</h1>
    <h3>Pandemia nadal trwa</h3>
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