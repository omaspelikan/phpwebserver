<?php
    //$oldname = isset($_POST["name"]) ? $_POST["name"] : '';
    //$oldpass = isset($_POST["pass"]) ? $_POST["pass"] : '';
    $salt = 'XyZzy12*_';                        // password = XyZzy12*_php123
    $stored_hash = hash('md5', $salt.'php123'); // hash value of password
    $md5 = hash('md5', $_POST['pass']);               // hash value of user input password

    function login($hash, $md5) {
        // check login name is not empty and check password is not empty and correct.
        // Redirect to game.php if login success.
        if (($_POST["name"]=='') or ($_POST['pass']=='')) {
            echo "User name and password are required";
        } elseif ($_POST["pass"] != '' and ($hash != $md5)) {
            echo "Incorrect password";
        } else {
            header("Location: game.php?name=".urlencode($_POST["name"]));
            exit();
        }
    }
?>





<!DOCTYPE html>
<html>
<head>
<title>Please Log In</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<p class="error">
<?php
    login($stored_hash, $md5);
?>
</p>
<form method="POST">
User Name
<input type="text" name="name"><br>
Password
<input type="password" name="pass"><br>  
<input type="submit" name="Login">    
</form>                
</body>
</html>