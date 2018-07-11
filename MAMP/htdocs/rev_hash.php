<!DOCTYPE html>
<html>
    <title>Reverse Hash to Pin</title>
    <body>
        
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="GET">
                <input type="text" name="md5" size=40>
                <input type="submit" name="Submit">
            </form>
            <?php
                show_hash(15);
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
                    echo "Debug Output"."<br>";
                        for($i="0";$i<="15";$i++) {
                            echo hash('md5', str_pad($i,4,"0",STR_PAD_LEFT))." ".str_pad($i,4,"0",STR_PAD_LEFT)."<br>";
                        }
                } 
            ?>     
    </body>
</html>