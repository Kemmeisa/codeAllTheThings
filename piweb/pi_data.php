<?php
//address of the server where db is installed
$servername = "localhost";

//username to connect to the db
//the default value is root
$username = "root";

//password to connect to the db
//this is the value you would have specified during installation of WAMP stack
$password = "root99";

//name of the db under which the table is created
$dbName = "test";

//establishing the connection to the db.
$conn = new mysqli($servername, $username, $password, $dbName);

//checking if there were any error during the last connection attempt
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

//enter in sample data
$sql = "CREATE TABLE top_odi_wicket_takers(
      player varchar(255),
        wickets integer,
        PRIMARY KEY (player)
    )";

mysqli_query($conn, $sql);

$sql = "INSERT INTO top_odi_wicket_takers(player, wickets) VALUES('MA Starc', 34)";
mysqli_query($conn, $sql);
$sql = "INSERT INTO top_odi_wicket_takers(player, wickets) VALUES('ST Finn', 27)";
mysqli_query($conn, $sql);
$sql = "INSERT INTO top_odi_wicket_takers(player, wickets) VALUES('Imran Tahir', 25)";
mysqli_query($conn, $sql);
$sql = "INSERT INTO top_odi_wicket_takers(player, wickets) VALUES('M Morkel', 21)";
mysqli_query($conn, $sql);
$sql = "INSERT INTO top_odi_wicket_takers(player, wickets) VALUES('TA Boult', 36)";
mysqli_query($conn, $sql);

//the SQL query to be executed
$query = "SELECT * FROM top_odi_wicket_takers";

//storing the result of the executed query
$result = $conn->query($query);

//initialize the array to store the processed data
$jsonArray = array();

//check if there is any data returned by the SQL Query
if ($result->num_rows > 0) {
  //Converting the results into an associative array
  while($row = $result->fetch_assoc()) {
    $jsonArrayItem = array();
    $jsonArrayItem['label'] = $row['player'];
    $jsonArrayItem['value'] = $row['wickets'];
    //append the above created object into the main array.
    array_push($jsonArray, $jsonArrayItem);
  }
}

//Closing the connection to DB
$conn->close();

//set the response content type as JSON
header('Content-type: application/json');
//output the return value of json encode using the echo function. 
echo json_encode($jsonArray);
?>
