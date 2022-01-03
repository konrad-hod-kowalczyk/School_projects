<?php
require "database.php";
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
    <style>
        table,th,td,tr{
            border: 1px solid black;        
        }
    </style>
</head>
<body>
    <?php
    error_reporting(0);
    echo "<div style='background-color: blue; height: 40px; display:block;'>";
    echo "<img src='logo.png' style='height: 40px;'>";
    echo "<a href='main.php'style='color:white;'> Strona Główna</a>";
    echo "<a href='info.php' style='color:white;'> Informacje </a>";
    echo "<a href='covid.php' style='color:white;'> Covid </a>";
    echo "<a href='closevisits.php' style='color:white;'> Najbliższe Wizyty </a>";
    echo "<a href='arrange.php' style='color:white;'> Umów Wizytę </a>";
    echo "<a style='pointer-events:none; color:yellow;'> Historia Wizyt </a>";
    echo "<div class='login' style='float:right; display:'inline-block'>
    <div style='color:white;'> Witaj ". $_SESSION['name'] ."
    <button class='btn btn-primary' onclick='redirect()' type='submit' method='post'>Wyloguj</button>
    </div></div>";
    echo "<h1>Twoja historia wizyt w przychodni Ptasia Maska</h1>";
    $conn = new mysqli($data->host,$data->db_user,$data->db_password,$data->db_name);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    $result = $conn->query("SELECT * FROM visits");
    $row = mysqli_fetch_array($conn->query("SELECT * FROM visits"));
    $counter=0;
    if($row)
    {
        echo "<table>
                <tr>
                <th> data </th>
                <th> dolegliwość </th>
                <th> lekarz </th>
                </tr>";
        while ($row = $result->fetch_assoc()) {
            if($row['patient']==$_SESSION['index'] && $row['data']<date("Y-m-d H:i:s"))
            {
                echo " <tr>
                <td>".$row['data']."</td>
                <td>".$row['description']."</td>
                <td>".$row['doctor']."</td>
                </tr>";
                $counter = $counter + 1;
            }
        }
        echo "</table>";
    }
    if($counter==0)
    {
        echo "<h3>Wygląda na to, że nie masz przeszłych wizyt do wyświetlenia</h3>";
        echo "<div style='display:inline-block'>";
        echo "<button onclick='arr();' class='btn btn-primary' type='submit'> Umów wizytę </button>";
        echo "</div>";
    }
    ?>
    <script>
        function redirect()
        {
            window.location.href = "logout.php";
        }
        function arr()
        {
            window.location.href = 'arrange.php';
        }
    </script>
</body>
</html>