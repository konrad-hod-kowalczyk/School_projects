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
        .work{
            top:30px;
        }
        .alert-fixed {
    position:fixed; 
    top: 0px; 
    left: 0px; 
    width: 100%;
    z-index:9999; 
    border-radius:0px
}
    </style>
</head>
<body>
    <div class="work">
    <form class="form" style="display:block;" method="post">
        <div style="display:inline-block !important;">
            <h4>Logowanie</h4>
            <img src="logo.png">
        </div>
        <div class="col-md-4">
        <label for="val1" class="form-label">E-mail: </label> <br>
        <input class="form-control" id="val1" placeholder="sto@poczta.pl" name='LOG' required/>
        </div>
        <div class="col-md-4">
        <label for="val2" class="form-label">Hasło: </label> <br>
        <input type="password" class="form-control" id="val2" placeholder="Hasło" name='PASS' required/>
        </div>
        <div class="col-md-4">
            <input class="form-check-input" type="checkbox" value="true" id="flexCheckDefault" name="administration">
            <label class="form-check-label" for="flexCheckDefault">
                Administrator
            </label>
        </div>
        <button class="btn btn-primary" type="submit">Zaloguj</button>
        <a href="register.php">Nie masz konta? Zarejestruj się</a>
    </form>
    <a href="main.php">Strona dla niezalogowanych</a>
    </div>
    <?php
        error_reporting(0);
        $conn = new mysqli($data->host,$data->db_user,$data->db_password,$data->db_name);
        try
        {
            $log = $_POST['LOG'];
            $pass = $_POST['PASS'];
            $admin = $_POST['administration'];
        }
        catch(Exception $e) {}
        $access=false;
        if($admin=="true")
        {
            $result = $conn->query("SELECT * FROM admin");
            $row = mysqli_fetch_array($conn->query("SELECT * FROM admin"));
            while ($row = $result->fetch_assoc()) {
                if($row['mail']==$log && $row['password']==$pass)
                {
                    $access = true;
                    $_SESSION['admin']=$row['name'];
                    break;
                }
            }
        }
        else
        {
            $result = $conn->query("SELECT * FROM login");
            $row = mysqli_fetch_array($conn->query("SELECT * FROM login"));
            while ($row = $result->fetch_assoc()) {
                if($row['mail']==$log && $row['password']==$pass)
                {
                    $access = true;
                    $_SESSION['name']=$row['name'];
                    $_SESSION['index']=$row['id'];
                    break;
                }
            }
        }
        if($access)
        {
            $_SESSION['feedback']="success";
            header('Location: main.php');
        }
        else if($log !== null)
        {
            $log=null;
            $pass=null;
            $_SESSION['feedback']="failure";    
        }
        else if($log === null) unset($_SESSION['feedback']); 
        if($_SESSION['feedback']=="failure")
        {
            echo '<div class="alert alert-warning alert-dismissible fade show alert-fixed" role="alert">
            Błąd logowania
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>';
        }
        else if(($_SESSION['feedback']=="success"))
        {
            echo '<div class="alert alert-warning alert-dismissible fade show alert-fixed" role="alert">
            konto zostało utworzone
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>';   
        }
        $conn->close();
    ?>
</body>
</html>