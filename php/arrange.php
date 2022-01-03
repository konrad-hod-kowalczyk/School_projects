<?php
require "database.php";
if (!isset($_SESSION)) {
    session_start();
}
header('');
ob_start();
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
    echo "<a href='info.php' style='color:white;'> Informacje </a>";
    echo "<a href='covid.php' style='color:white;'> Covid </a>";
    echo "<a href='closevisits.php' style='color:white;'> Najbliższe Wizyty </a>";
    echo "<a style='pointer-events=none; color:yellow;'> Umów Wizytę </a>";
    echo "<a href='history.php' style='color:white;'> Historia Wizyt </a>";
    echo "<div class='login' style='float:right; display:'inline-block'>
    <div style='color:white;'> Witaj ". $_SESSION['name'] ."
    <button class='btn btn-primary' onclick='redirect()' type='submit' method='post'>Wyloguj</button>
    </div></div>";
    ?>
    <form class="needs-validation" method="post">
        <h4>Umawianie wizyty</h4>
        <div class="col-md-4">
        <label for="val1" class="form-label">Data i godzina: </label> <br>
        <input type="text" class="form-control 1" id="val1" placeholder="YYYY-MM-DD hh:mm:ss" name="data" required/>
        <div class="invalid-feedback">
            Data i czas muszą wyglądać tak jak podane oraz nie mogą być w przeszłości
        </div>
        </div>
        <div class="col-md-4">
        <label for="val1" class="form-label">Specjalność: </label> <br>
        <input type="text" class="form-control 2" id="val1" placeholder="laryngolog, dermatolog, lekarz pierwszego kontaktu" name="spec" required/>
        <div class="invalid-feedback">
            Tylko podane specjalności
        </div>
        </div>
        <div class="col-md-4">
        <label for="val3" class="form-label">Opis dolegliwości: </label> <br>
        <input type="text" class="form-control 3" id="val3" placeholder="Mam gorączkę i kaszel" name="desc" required/>
        <div class="invalid-feedback">
            proszę sobie nie żartować
        </div>
        </div>
        <button class="btn btn-primary" type="submit">Umów</button>
        </div>
    </form>
    <div id="div1"></div>
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
        if(input.classList.contains('3'))
        {
            if(input.checkValidity() === false) 
            {
                input.classList.add('is-invalid')
            }
            else
            {
                for(var i=0;i<input.value.length;i++)
                {
                    if(['0','1','2','3','4','5','6','7','8','9'].indexOf(input.value[i]) > -1) input.classList.add('is-invalid')
                    else if(i+1==input.value.length) input.classList.add('is-valid')
                }
            }
        }
        if(input.classList.contains('2'))
        {
            if(input.checkValidity() === false) input.classList.add('is-invalid')
            else 
            {
                if(input.value == 'laryngolog' || input.value == 'dermatolog' || input.value == 'lekarz pierwszego kontaku') input.classList.add('is-valid')
                else input.classList.add('is-invalid')
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
                if(mydate < Date.now()) input.classList.add('is-invalid')
                else input.classList.add('is-valid')
            }
        }
      }, false);
    });
  }, false);
})()
    </script>
    <?php
    error_reporting(0);
    $conn = new mysqli($data->host,$data->db_user,$data->db_password,$data->db_name);
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
    try
    {
        $data = $_POST['data'];
        $spec = $_POST['spec'];
        $desc = $_POST['desc'];
        $index = $_SESSION['index'];
        date("Y-m-d H:i:s",strtotime($date));
        $sql = "INSERT INTO visits(patient,data,description,doctor) VALUES ('$index','$data','$desc','$spec');";
        if($data && $desc && $spec)
        {
            if(mysqli_query($conn,$sql))
            {
                $_SESSION['feedback']="success";
                header('Location: closevisits.php');
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
    </script>
</body>
</html>