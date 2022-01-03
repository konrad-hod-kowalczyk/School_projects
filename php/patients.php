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
    if($_SESSION['feedback']=="success")
    {
        echo '<div class="alert alert-warning alert-dismissible fade show alert-fixed" role="alert">
            Usunięto pacjenta
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>';
        unset($_SESSION['feedback']);
    }
    echo "<div style='background-color: blue; height: 40px; display:block;'>";
    echo "<img src='logo.png' style='height: 40px;'>";
    echo "<a href='main.php'style='color:white;'> Strona Główna</a>";
    echo "<a href='info.php' style='color:white;'> Informacje </a>";
    echo "<a href='covid.php' style='color:white;'> Covid </a>";
    echo "<a href='summary.php' style='color:white;'> Podsumowanie </a>";
    echo "<a href='doctors.php' style='color:white;'> Lekarze </a>";
    echo "<a href='patients.php' style='color:white;'> Pacjenci </a>";
    echo "<a href='visits.php' style='color:white;'> Wizyty </a>";
    echo "<div class='login' style='float:right; display:'inline-block'>
    <div style='color:white;'> Bądź pozdrowiony ". $_SESSION['admin'] ."
    <button class='btn btn-primary' onclick='redirect()' type='submit' method='post'>Wyloguj</button>
    </div></div>";
    echo "<h1>Historia wizyt w przychodni Ptasia Maska</h1>";
    $conn = new mysqli($data->host,$data->db_user,$data->db_password,$data->db_name);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    $result = $conn->query("SELECT id,name,surname,birth,mail,id_num,adress,city FROM login");
    $row = mysqli_fetch_array($conn->query("SELECT id,name,surname,birth,mail,id_num,adress,city FROM login"));
    $counter=0;
    if($row)
    {
        echo "<table>
                <tr>
                <th> id </th>
                <th> imie </th>
                <th> nazwisko </th>
                <th> data urodzenia </th>
                <th> e-mail </th>
                <th> pesel </th>
                <th> adres </th>
                <th> miasto </th>
                </tr>";
        while ($row = $result->fetch_assoc()) 
        {
            echo " <tr>
            <td>".$row['id']."</td>
            <td>".$row['name']."</td>
            <td>".$row['surname']."</td>
            <td>".$row['birth']."</td>
            <td>".$row['mail']."</td>
            <td>".$row['id_num']."</td>
            <td>".$row['adress']."</td>
            <td>".$row['city']."</td>
            <td><button style='background-color:red;' onclick='del(".$row['id'].");' class='btn btn-primary' type='submit'> Usuń </button></td>
            </tr>";
            $counter = $counter + 1;
        }
        echo "</table>";
    }
    if($counter==0)
    {
        echo "<h3>Wygląda na to, że nikt nie uczęszcza do tej przychodni</h3>";
    }
    ?>
    <script>
        function redirect()
        {
            window.location.href = "logout.php";
        }
        function del(n)
        {
            window.location.href = "deletepatient.php?num="+n;
        }
    </script>
</body>
</html>