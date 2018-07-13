<?php
    $oldname = isset($_POST["name"]) ? $_POST["name"] : '';
    $oldpass = isset($_POST["pass"]) ? $_POST["pass"] : '';
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
    if ($_POST["name"] == '' or ($_POST["pass"] == '')) {
        echo "User name and password are required";
    }
?>
</p>
<form method="POST">
User Name
<input type="text" name="name" value="<?= $oldname ?>"><br>
Password
<input type="password" name="pass" value="<?= $oldpass ?>"><br>  
<input type="submit" name="Login">    
</form>                
</body>
</html>