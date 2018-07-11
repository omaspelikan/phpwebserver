<!DOCTYPE html>
<html>
    <title>Reverse Hash to Pin</title>
    <body>
        
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="GET">
                <input type="text" name="hashvalue">
                <input type="submit" name="Submit">
            </form>
            <?php
               if ($_SERVER["REQUEST_METHOD"] == "GET") {
                   
                    echo "<br>"."PIN value is ".str_pad(bf_hash($_GET["hashvalue"]),4,"0",STR_PAD_LEFT);
               } 
               function bf_hash($hashv) {
                   $found = FALSE;
                    for($i="0";$i<="9999";$i++){
                        if ($hashv == hash("md5", str_pad($i,4,"0",STR_PAD_LEFT))) {
                            $found = True;
                            //echo "<br>"."PIN value is ". str_pad($i,4,"0",STR_PAD_LEFT);
                            return $i;
                        }
                    }
                    if ($found === FALSE) {
                        echo "PIN not found.";
                    }
               }
            ?>     
    </body>
</html>