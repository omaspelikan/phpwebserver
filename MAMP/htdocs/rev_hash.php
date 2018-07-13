<!DOCTYPE html>
<html>
<head>
    <title>Reverse Hash to Pin</title>
    <link rel="stylesheet" href="style.css">
</head>
    <body id="hash">
        
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="GET">
                <input type="text" name="md5" size=40>
                <input type="submit" name="Submit">
            </form>
            <?php
                show_hash(15);
                echo "<br>";
                $time_start = microtime(True);
               if ($_SERVER["REQUEST_METHOD"] == "GET") {
                    $pin = bf_hash($_GET["md5"]);
                    if ($pin === FALSE) {
                        echo "PIN not found."."<br>";
                        $time_period = microtime(True) - $time_start;
                        echo "Total time elpased: ".$time_period;
                    } else {
                        echo "PIN value is ".str_pad($pin,4,"0",STR_PAD_LEFT)."<br>"; 
                        $time_period = microtime(True) - $time_start;
                        echo "Total time elpased: ".$time_period;
                    }
                        
               } 
               function bf_hash($hashv) {
                   // compare hash value with 4 digit number from 0000 to 9999.
                   $found = FALSE;
                   $count = 1;
                    for($i="0";$i<="9999";$i++){
                        if ($hashv == hash("md5", str_pad($i,4,"0",STR_PAD_LEFT))) {
                            $found = True;
                            echo "Total count ".$count."<br>";
                            return $i;
                        }
                        $count++;
                    }
                    echo "Total count ".$i."<br>";                    
                    return $found;                   
               }
               function show_hash($number) {
                   // print 4 digit number PIN value from 0 to $number and padding 0 to become 4 digit.
                    echo "Debug Output"."<br>";
                        for($i="0";$i<=$number;$i++) {
                            echo hash('md5', str_pad($i,4,"0",STR_PAD_LEFT))." ".str_pad($i,4,"0",STR_PAD_LEFT)."<br>";
                        }
                } 
            ?>     
    </body>
</html>