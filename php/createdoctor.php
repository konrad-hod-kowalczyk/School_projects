<?php
require "database.php";
if (!isset($_SESSION)) {
    session_start();
}
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
    <form class="needs-validation" method="post">
        <h4>Rejestracja</h4>
        <div class="col-md-4">
        <label for="val1" class="form-label">Imię: </label> <br>
        <input type="text" class="form-control 1" id="val1" placeholder="imię" name="name" required/>
        <div class="invalid-feedback">
            Imię musi składać się tylko z liter
        </div>
        </div>
        <div class="col-md-4">
        <label for="val2" class="form-label">Nazwisko: </label> <br>
        <input type="text" class="form-control 2" id="val2" placeholder="nazwisko" name="surname" required/>
        <div class="invalid-feedback">
            Nazwisko musi się składać tylko z liter
        </div>
        </div>
        <div class="col-md-4">
        <label for="val3" class="form-label">Specjalizacja: </label> <br>
        <input type="text" class="form-control 3" id="val3" placeholder="laryngolog, dermatolog, lekarz pierwszego kontaktu"name="spec" required/>
        <div class="invalid-feedback">
            specjalizacja musi być jedną z podanych
        </div>
        </div>
        <div class="col-md-4">
        <label for="val4" class="form-label">Numer telefonu: </label> <br>
        <input type="text" class="form-control 6" id="val4" placeholder="---------" name="tel" required/>
        <div class="invalid-feedback">
            Pesel musi składać się z 9 cyfr
        </div>
        </div>
        <div class="col-md-4">
        <label for="val5" class="form-label">Numer gabinetu: </label> <br>
        <input type="text" class="form-control 5" id="val5" placeholder="12" name="room" required/>
        <div class="invalid-feedback">
            Przychodnia posiada tylko 20 gabinetów
        </div>
        </div>
        <div class="col-md-4">
        <label for="val6" class="form-label">Pesel: </label> <br>
        <input type="text" class="form-control 4" id="val6" placeholder="-----------" name="id" required/>
        <div class="invalid-feedback">
            Pesel musi składać się z 11 cyfr
        </div>
        </div>
        <div class="col-md-4">
        <label for="val6" class="form-label">Tytuł: </label> <br>
        <input type="text" class="form-control 7" id="val6" placeholder="dr P. Black" name="title" required/>
        </div>
        <div class="col-12">
        <button class="btn btn-primary" type="submit">Rejestracja lekarza</button>
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
        if(input.classList.contains('1') || input.classList.contains('2'))
        {
            if(input.value.length > 20 || input.checkValidity() === false) 
            {
                input.classList.add('is-invalid')
            }
            else
            {
                for(var i=0;i<input.value.length;i++)
                {
                    if(['0','1','2','3','4','5','6','7','8','9','\''].indexOf(input.value[i]) > -1) input.classList.add('is-invalid')
                    else if(i+1==input.value.length) input.classList.add('is-valid')
                }
            }
        }
        if(input.classList.contains('3'))
        {
            if(input.checkValidity() === false) input.classList.add('is-invalid');
            else 
            {
                if(input.value == 'laryngolog' || input.value == 'dermatolog' || input.value == 'lekarz pierwszego kontaku') input.classList.add('is-valid');
                else input.classList.add('is-invalid');
            }
        }
        if(input.classList.contains('4'))
        {
            if(input.value.length != 11 || input.checkValidity() === false) input.classList.add('is-invalid')
            else
            {
                for(var i=0;i<input.value.length;i++)
                {
                    if(['0','1','2','3','4','5','6','7','8','9'].indexOf(input.value[i])==-1) input.classList.add('is-invalid')
                    else if(i+1==input.value.length) input.classList.add('is-valid')
                }
            }
        }
        if(input.classList.contains('6'))
        {
            if(input.checkValidity() === false || input.value.length != 9) 
            {
                input.classList.add('is-invalid')
            }
            else
            {
                input.classList.add('is-valid')
            }
        }
        if(input.classList.contains('5'))
        {
            if(input.checkValidity() === false || parseInt(input.value) < 1 || parseInt(input.value) > 20) 
            {
                input.classList.add('is-invalid')
            }
            else
            {
                input.classList.add('is-valid')
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
        $name = $_POST['name'];
        $surname = $_POST['surname'];
        $spec = $_POST['spec'];
        $id = $_POST['id'];
        $tel = $_POST['tel'];
        $room = $_POST['room'];
        $title = $_POST['title'];
        $sql = "INSERT INTO doctors(name,surname,spec,nr_tel,nr_room,id_num,title) VALUES ('$name','$surname','$spec','$tel','$room','$id','$title');";
        if($name && $surname && $spec && $id && $tel && $room)
        {
            if(mysqli_query($conn,$sql))
            {
                $_SESSION['feedback']="success";
                header('Location: doctors.php');
            } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
        }
    }
    catch(Exception $e) {}
    $conn->close();
    ob_end_flush();
    ?>
</body>
</html>