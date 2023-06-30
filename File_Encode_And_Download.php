# PHP script to encode a file to base64 and downloaded it. It reads the content of the file 'file.dmp', encodes it in base64, saves it in a new file 'file.64'. 

<?php 

$a = file_get_contents('C:\\path\to\file.txt');

$myfile = file_put_contents('C:\path\to\file.64', base64_encode($a));

header('Content-Disposition: attachment; filename="file_B64"');
echo base64_encode($a);

?>
