<!DOCTYPE html>
<html>
<title>Omas Pelikan PHP</title>
<body>
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post">
    First name:<br/>
    <input type="text" name="firstname"><br>
    Last Name:<br/>
    <input type="text" name="lastname"><br>
    <input type="submit" value="submit">
</form>
<?php
    if ($_POST["firstname"] != '') {
        echo $_POST["firstname"]."<br>";
    }
    if ($_POST["lastname"] != '') {
        echo $_POST["lastname"]."<br>";
    }    
?>        
</body>
</html>