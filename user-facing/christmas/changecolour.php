<?php
$res = array('status' => NULL);
header('Content-Type: application/json');

// Check for hex parameter
if (empty($_GET['hex'])) {
    echo json_encode($res);
    exit;
}

// $hex colour
$colourhex = $_GET['hex'];

// Send request
$ch = curl_init("http://XX.XX.XX.XX:8001/colour/$colourhex"); // change this to your home IP address
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_USERAGENT, "ArulZilla/1.0");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 3);
$output = curl_exec($ch);
curl_close($ch);

// JSON output
$res['status'] = $output;
echo json_encode($res);
?>
