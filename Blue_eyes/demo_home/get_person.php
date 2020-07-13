<?php
	require_once 'connect.php';

	if ($_SERVER['REQUEST_METHOD'] == 'GET') {
		if (isset($_GET['room_id'])) {
			$roomId = $_GET['room_id'];
			$sql = "SELECT * from person where room_id=:room_id";
			$query = $dbh->prepare($sql);
			$query->bindParam(':room_id',$roomId,PDO::PARAM_STR);
			$query->execute();
			$results=$query->fetchAll(PDO::FETCH_OBJ);
			var_dump($results);
			foreach ($results as $value) {
				echo '<option>-- Chọn người ở --</option>';
				echo '<option value="'. $value->id .'">'. $value->name .'</option>';
      		}
		}
	}
?>