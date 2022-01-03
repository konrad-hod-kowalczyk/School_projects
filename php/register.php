<?php
    require "database.php";
    ob_start();
    if (!isset($_SESSION)) {
        session_start();
    }
    $_SESSION['doc'] = new DOMDocument();
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
        <label for="val3" class="form-label">Data urodzenia(uwaga! wpisanie np. 15 miesiąca poskutkuje wybraniem marca następnego roku): </label> <br>
        <input type="text" class="form-control 3" id="val3" placeholder="yyyy-mm-dd" name="date" required/>
        <div class="invalid-feedback">
            Data musi wyglądać tak jak podana czyli yyyy-mm-dd i nie może być większa od dzisiejszej oraz mniejsza od 1900-01-01
        </div>
        </div>
        <div class="col-md-4">
        <label for="val4" class="form-label">Pesel: </label> <br>
        <input type="text" class="form-control 4" id="val4" placeholder="-----------" name="id" required/>
        <div class="invalid-feedback">
            Pesel musi składać się z 11 cyfr
        </div>
        </div>
        <div class="col-md-4">
        <label for="val5" class="form-label">Adres Zamieszkania: </label> <br>
        <input type="text" class="form-control 5" id="val5" placeholder="Aeneriona 12" name="address" required/>
        </div>
        <div class="col-md-4">
        <label for="val6" class="form-label">Miasto: </label> <br>
        <input type="text" class="form-control 6" id="val6" placeholder="Lothern" name="city" required/>
        </div>
        <div class="col-md-4">
        <label for="val7" class="form-label">E-mail: </label> <br>
        <input type="text" class="form-control 7" id="val7" placeholder="sto@poczta.pl" name="mail" required/>
        <div class="invalid-feedback">
            E-mail musi być zgodny z tymi instrukcjami (nie wszystkimi ale cśśśś) https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjh7pKJmYn1AhXisosKHRvXC2QQFnoECAoQAw&url=https%3A%2F%2Fwww.upgrad.com%2Fblog%2Femail-validation-in-javascript%2F&usg=AOvVaw2zLKMTvKfld9_RicL2U6t7
        </div>
        </div>
        <div class="col-md-4">
        <label for="val8" class="form-label">Hasło: </label> <br>
        <input type="password" class="form-control 8" id="val8" placeholder="Hasło" name="password" required/>
        <div class="invalid-feedback">
            Hasło musi być conajmniej długie na 8 znaków
        </div>
        </div>
        <div class="col-12">
        <button class="btn btn-primary" type="submit">Rejestracja</button>
        <a href="index.php">Masz już konto? Zaloguj się</a>
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
            if(input.value[4] != '-' || input.value[7] != '-' || input.checkValidity() === false) input.classList.add('is-invalid')
            else
            {
                var parts = input.value.split('-');
                var mydate = new Date(parts[0], parts[1] - 1, parts[2]);
                if(mydate > Date.now() || mydate < new Date(1900,0,1)) input.classList.add('is-invalid')
                else input.classList.add('is-valid')
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
        if(input.classList.contains('5') || input.classList.contains('6'))
        {
            if(input.checkValidity() === false) 
            {
                input.classList.add('is-invalid')
            }
            else
            {
                input.classList.add('is-valid')
            }
        }
        if(input.classList.contains('7'))
        {
            if(input.value[0]=='.' || input.value[input.value.length-1]=='.' || input.value[0]==':' || input.value[input.value.length-1]==':' || input.value[0]==';' || input.value[input.value.length-1]==';' || input.value[0]==',' || input.value[input.value.length-1]==',' || input.value[0]=='_' || input.value[input.value.length-1]=='_' || input.checkValidity() === false) input.classList.add('is-invalid')
            else
            {
                var at=0;
                for(var i=0;i<input.value.length;i++)
                {
                    if(input.value[i]=='@' && at==1) 
                    {
                        input.classList.add('is-invalid')
                        break
                    }
                    else if(input.value[i]=='@' && at==0)
                    {
                        if(`#*+&'!%@?{^}”.,/;:`.indexOf(input.value[i-1])>-1 || `#*+&'!%@?{^}”.,/;:`.indexOf(input.value[i+1])>-1)
                        {
                            input.classList.add('is-invalid')
                            break
                        }
                        else at=1
                    } 
                    if(`qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890#*+&'!%@?{^}”.,/;:`.indexOf(input.value[i])==-1)
                    {
                        input.classList.add('is-invalid')
                        break
                    }
                    if(`#*+&'!%@?{^}”.,/;:`.indexOf(input.value[i])>-1 && `#*+&'!%@?{^}”.,/;:`.indexOf(input.value[i-1])>-1)
                    {
                        input.classList.add('is-invalid')
                        break
                    }
                    if(i+1==input.value.length) input.classList.add('is-valid')
                }
            }
        }
        if(input.classList.contains('8'))
        {
            if(input.value.length < 8 || input.checkValidity() === false) input.classList.add('is-invalid')
            else input.classList.add('is-valid')
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
        $date = $_POST['date'];
        date("Y-m-d",strtotime($date));
        $id = $_POST['id'];
        $address = $_POST['address'];
        $city = $_POST['city'];
        $mail = $_POST['mail'];
        $pass = $_POST['password'];
        $sql = "INSERT INTO login(name,surname,birth,id_num,adress,city,mail,password) VALUES ('$name','$surname','$date','$id','$address','$city','$mail','$pass');";
        if($name && $surname && $date && $id && $address && $city && $mail && $pass)
        {
            if(mysqli_query($conn,$sql))
            {
                $_SESSION['feedback']="success";
                header('Location: index.php');
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