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
// check $_POST have been initialized , if true then print first and last name.
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $firstname = htmlspecialchars($_POST["firstname"]);
        $lastname = htmlspecialchars($_POST["lastname"]);
        echo $firstname."<br>".$lastname;
        
    }
?>        
</body>
</html>