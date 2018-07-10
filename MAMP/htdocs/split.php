<?php 
// split.php
echo "Welcom to Split demo";
echo '<br/>';
$demo = array("sdfadf","adfadfa","jjjjjj","7890");
print_r($demo);
foreach ($demo as $a) {
    echo $a;
    echo '<br/>';
}
$split_st = "this is a book";

$demo = explode(' ',$split_st);
foreach ($demo as $a) {
    echo $a;
    echo '<br/>';
}
var_dump($demo);
$demo[] = 878;
print_r($demo);
echo '<br/>';
echo array_search(878,$demo);
?>