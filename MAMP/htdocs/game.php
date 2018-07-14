<?php
    if (! isset($_GET['name'])) {
        die("Name parameter missing");
    }
    if (isset($_POST['exit'])) {
        header('Location: index.php');
    }
?>
<!DOCTYPE html>
<html>
<head>
<title>Game</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<h1>Rock Paper Scissors</h1>
<p>
<?php echo "Welcome ".$_GET["name"]; ?>
</p>
<form method="POST">
    <select name="choice">
        <option value="Rock">Rock</option>
        <option value="Paper">Paper</option>
        <option value="Scissors">Scissors</option>     
    </select>
    <input type="submit" value="Play" name='submit' id='buttom'>
    <input type="submit" value="Logout" name='exit' id='buttom'>
</form>
<br>
<p id='instro'>Please select a strategy and press Play.</p>
</body>
</html>