<html>
    <title> read hello</title>
    <body>
        <h1>Hello World</h1>
<?php
$name = $_GET['name'];
echo "Hello World! $name";
echo '<br />';
$job = 6 *5;
echo 'test';
echo '<br />';
echo "good job $job\n";
echo "abc" . "cdd";
$x = "abc";
$y = "def";
$z = $x.$y;
echo "$z\n";
echo "<pre>\n";
echo "</pre>";
print hash('sha256', 'Omas Pelikan');
require "fail.php"
?>
    </body>
</html>