<?php
require 'database.php';
ob_start();
if (!isset($_SESSION)) {
    session_start();
}
header('');
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
    echo "<a href='summary.php' style='color:white;'> Podsumowanie </a>";
    echo "<a href='doctors.php' style='color:white;'> Lekarze </a>";
    echo "<a href='patients.php' style='color:white;'> Pacjenci </a>";
    echo "<a href='visits.php' style='pointer-events:none; color:yellow;'> Wizyty </a>";
    echo "<div class='login' style='float:right; display:'inline-block'>
    <div style='color:white;'> Bądź pozdrowiony ". $_SESSION['admin'] ."
    <button class='btn btn-primary' onclick='redirect()' type='submit' method='post'>Wyloguj</button>
    </div></div>";
    echo "<h1>Edycja Wizyty</h1>";
    $num = $_GET['num'];
    ?>
    <form class="needs-validation" method="post">
        <div class="col-md-4">
        <label for="val1" class="form-label">Data: </label> <br>
        <input type="text" class="form-control 1" id="val1" placeholder="YYYY-MM-DD hh:mm:ss" name="data"/>
        <div class="invalid-feedback">
            Data musi wyglądać tak jak podana, oraz nie może znajdować się w przeszłości
        </div>
        </div>
        <div class="col-md-4">
        <label for="val2" class="form-label">Lekarz: </label> <br>
        <input type="text" class="form-control 2" id="val2" placeholder="lekarz" name="doctor"/>
        <div class="invalid-feedback">
            Nazwa musi się składać tylko z liter
        </div>
        </div>
        <div style="display: inline-block;">
            <button class="btn btn-primary" type="submit">Zatwierdź</button>
            <button class="btn" type ="submit" onlick="ret();">Anuluj</button>
        </div>
    </form>
    <script>
        (function() {
  'use strict';
  window.addEventListener('load', function() {
    // fetch all the forms we want to apply custom style
    var inputs = document.getElementsByClassName('form-control')

    // loop over each input and watch blur event
    var validation = Array.prototype.filter.call(inputs, function(input) {
      input.addEventListener('blur', function(event) {
        // reset
        input.classList.remove('is-invalid')
        input.classList.remove('is-valid')
        if(input.classList.contains('2'))
        {
            if(input.checkValidity() === false) 
            {
                input.classList.add('is-invalid')
            }
            else
            {
                for(var i=0;i<input.value.length;i++)
                {
                    if(['0','1','2','3','4','5','6','7','8','9'].indexOf(input.value[i]) > -1) input.classList.add('is-invalid');
                    else if(i+1==input.value.length) input.classList.add('is-valid');
                }
            }
        }
        if(input.classList.contains('1'))
        {
            if(input.value[4] != '-' || input.value[7] != '-' || input.value[10] != ' ' || input.value[13] != ':' || input.value[16] != ':' || input.checkValidity() === false) input.classList.add('is-invalid')
            else
            {
                var dt = input.value.split(' ');
                var parts = dt[0].split('-');
                var time = dt[1].split(':');
                var mydate = new Date(parts[0], parts[1] - 1, parts[2], time[0], time[1], time[2]);
                if(mydate < Date.now()) input.classList.add('is-invalid');
                else input.classList.add('is-valid');
            }
        }
      }, false);
    });
  }, false);
})()
        function redirect()
        {
            window.location.href = "index.php";
        }
    </script>
    <?php
    //error_reporting(0);
    $conn = new mysqli($data->host,$data->db_user,$data->db_password,$data->db_name);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    try
    {
        $spec = $conn->query("SELECT doctor FROM visits WHERE id = $num")->fetch_row()[0];
        echo "<div style='display:block;'>";
        echo "<div> Proponowana data: ".$conn->query("SELECT data FROM visits WHERE id = $num")->fetch_row()[0]."</div>";
        echo "<div> Lekarz: ".$conn->query("SELECT doctor FROM visits WHERE id = $num")->fetch_row()[0]."</div>";
        $result = $conn->query("SELECT * FROM doctors");
        $row = mysqli_fetch_array($conn->query("SELECT * FROM doctors"));
        $counter=0;
        echo "<table>
                <tr>
                <th> imie </th>
                <th> nazwisko </th>
                <th> specjalizacja </th>
                <th> numer telefonu </th>
                <th> numer gabinetu </th>
                <th> tytuł </th>
                </tr>";
        while ($row = $result->fetch_assoc()) 
            {
                if($row['spec']==$spec)
                {
                    echo " <tr>
                    <td>".$row['name']."</td>
                    <td>".$row['surname']."</td>
                    <td>".$row['spec']."</td>
                    <td>".$row['nr_tel']."</td>
                    <td>".$row['nr_room']."</td>
                    <td><form method='post'><input style='background-color:green' name='title' type='submit' value='".$row['title']."'/></form></td>
                    </tr>";
                    $counter = $counter + 1;
                }
            }
        echo "</table>";
        if($counter == 0)
        {
            echo "<h2>Wygląda na to że nie ma doktora o podanej specjalizacji. Oznacza to, że system posiada lukę</h2>";
        }
    }
    catch(Exception $e) {}
    try
    {
        echo "</div>";
        if($_POST['data']) $data = $_POST['data'];
        else $data = $conn->query("SELECT data FROM visits WHERE id = $num")->fetch_row()[0];
        if($_POST['title']) 
        {
            $doc = $_POST['title'];
            echo "<script>document.getElementById('val2').value = '".$doc."'</script>";
        }
        $doc = $_POST['doctor'];
        echo $data;
        date("Y-m-d H:i:s",strtotime($data));
        $sql = "UPDATE visits SET data = '$data',doctor = '$doc',confirmation = 1 WHERE id = $num;";
        if($data && $doc)
        {
            if(mysqli_query($conn,$sql))
            {
                $_SESSION['feedback']="success";
                header('Location: visits.php');
            } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
        }
    }
    catch(Exception $e) {}
    $conn->close();
    ob_end_flush();
    ?>
    <script>
        function redirect()
        {
            window.location.href = "logout.php";
        }
        function ret()
        {
            window.location.href= "visits.php";
        }
    </script>
</body>
</html>