<?php
    for ($i='1';$i<='30';$i++) {
        echo str_pad($i,4,"0",STR_PAD_LEFT)." value is ".hash("md5",str_pad($i,4,"0",STR_PAD_LEFT))."\n";
    }
    echo hash("md5" ,"0001")."\n";
    echo hash("md5" ,"0002")."\n";
    echo hash("md5" ,"0003")."\n";
    $b = array(1,2,3);
    print_r($b);
    $result = array("rock","paper","scissors");
    echo $result[rand(0,2)]."<br>";
?>