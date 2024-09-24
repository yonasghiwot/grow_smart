<?php

/*
  Alsan Parajuli
  Complete project details at https://theiotprojects.com/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*/

$servername = "192.185.6.134";

// REPLACE with your Database name
$dbname = "ethioeap_AA_Administration";
// REPLACE with Database user
$username = "ethio_Addis";
// REPLACE with Database user password
$password = "a120m!Vm";

// Keep this API Key value to be compatible with the ESP8266 code provided in the project page. 
// If you change this value, the ESP8266 sketch needs to match
$api_key_value = "EthioLeapPass";

$api_key = $timeStamp = $temperature = $humidity = $ph = $ec = "";

$fullURL = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
//'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
// Use parse_url() function to parse the URL 
// and return an associative array which
// contains its various components

$url_components = parse_url($fullURL);

  
// Use parse_str() function to parse the
// string passed via URL
parse_str($url_components['query'], $params);

print $params['api_key'];
print $params['timeStamp'];
print $params['temperature'];
print $params['humidity'];
print $params['ph'];
print $params['ec'];


if ($params['api_key'] != "0") {
    //$api_key = test_input($_POST["api_key"]);
     $api_key = $params['api_key'];

    if($api_key == $api_key_value) {

        $timeStamp = test_input($params['timeStamp']);
        $temperature = test_input($params["temperature"]);
        $humidity = test_input($params["humidity"]);
        $ph = test_input($params["ph"]);
        $ec = test_input($params["ec"]);
        
        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        } 
        
        $sql = "INSERT INTO sensordata (TimeStamp, Temprature, Humidity, PH, EC)
        VALUES ('" . $timeStamp . "','" . $temperature . "','" . $humidity . "', '" . $ph . "', '" . $ec . "')";
        
        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    
        $conn->close();
    }
    else {
        echo "Wrong API Key provided.";
    }

}
else {
    echo "No data posted with HTTP POST.";
}

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}