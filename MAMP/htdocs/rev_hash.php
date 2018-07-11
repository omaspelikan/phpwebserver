<!DOCTYPE html>
<html>
    <title>Reverse Hash to Pin</title>
    <body>
        
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="GET">
                <input type="text" name="md5" size=40>
                <input type="submit" name="Submit">
            </form>
            <?php
               if ($_SERVER["REQUEST_METHOD"] == "GET") {
                    $pin = bf_hash($_GET["md5"]);
                    if ($pin === FALSE) {
                        echo "PIN not found.";
                    } else {
                        echo "PIN value is ".str_pad($pin,4,"0",STR_PAD_LEFT); 
                    }
                        
               } 
               function bf_hash($hashv) {
                   $found = FALSE;
                    for($i="0";$i<="9999";$i++){
                        if ($hashv == hash("md5", str_pad($i,4,"0",STR_PAD_LEFT))) {
                            $found = True;
                            return $i;
                        }
                    }                    
                    return $found;                   
               }
            ?>     
    </body>
</html>