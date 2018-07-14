<?php
    if (! isset($_GET['name'])) {
        die("Name parameter missing");
    }

    if (isset($_POST['exit'])) {
        header('Location: index.php');
    }
    
    $human = isset($_POST["choice"]) ? $_POST["choice"] : '';
    $select = array('Rock','Paper','Scissors');
    $computer = $select[rand(0,2)];

    function check($computer, $human) {
        if ($computer == $human) {
            return "Tie";
        } elseif (($computer == 'Paper') and ($human == 'Rock')) {
            return "You Lose";
        } elseif (($computer == 'Scissors') and ($human == 'Paper')) {
            return "You Lose";
        } elseif (($computer == 'Rock') and ($human == 'Scissors')) {
            return "You Lose";
        } else {
            return "You Win";
        }
    }
    function show_result($human,$computer) {
        // only print result if $_POST[] is initialized and $_POST['choice'] have value other than NULL.
        if (($_SERVER["REQUEST_METHOD"] == "POST") and (isset($_POST['choice']))) {
            echo "Human=".$human." "."Computer=".$computer." "."Result=".check($computer,$human)."<br>";
            //"Human=$_POST['choice']"." "."Computer=$computer"." "."Result=".check($computer,$human);
        }
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
    <select name='choice'>
        <option value='' selected disabled hidden>Select</option>
        <option value="Rock">Rock</option>
        <option value="Paper">Paper</option>
        <option value="Scissors">Scissors</option>     
    </select>                         
    <input type="submit" value="Play" name='submit' id='buttom'>
    <input type="submit" value="Logout" name='exit' id='buttom'>
</form>
<br>
<p id='instro'>Please select a strategy and press Play.<br>
<?php 
    show_result($human,$computer);                                                                                                                                  
    //echo '<br>';
    //print_r($human);
    //echo '<br>';
    //print_r($computer);
?>
</p>
</body>
</html>