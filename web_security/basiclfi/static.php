<?php

if(isset($_GET['static_file']) && !is_array($_GET['static_file'])){
    $filename = $_GET['static_file'];

    $content = @file_get_contents('static/' . $filename);
    if($content === FALSE){
        header('HTTP/1.1 404');
        die('');
    }

    $filename_parts = explode('.', $filename);
    $extension = end($filename_parts);
    
    switch($extension){
        case "js":
            header('Content-Type: application/javascript');
            break; 
        case "css":
            header('Content-Type: text/css');
            break;
        case "png":
            header('Content-Type: image/png');
            break;
        default:
            header('Content-Type: binary/octet-stream');
    }

    echo $content;

}
