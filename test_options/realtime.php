<?php
$connection = mysql_connect('0.0.0.0', 'root', 'letiennhat'); //The Blank string is the password
mysql_select_db('mysqldb1');

$query = "SELECT * FROM manager"; //You don't need a ; like you do in SQL
$result = mysql_query($query);

echo "<table>"; // start a table tag in the HTML

while($row = mysql_fetch_array($result)){   //Creates a loop to loop through results
echo "<tr><td>" . $row['name'] . "</td><td>" . $row['age'] . "</td></tr>";  //$row['index'] the index here is a field name
}

echo "</table>"; //Close the table in HTML

mysql_close(); //Make sure to close out the database connection
?>