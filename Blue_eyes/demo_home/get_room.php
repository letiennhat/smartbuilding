<?php
	require_once 'connect.php';

	if ($_SERVER['REQUEST_METHOD'] == 'GET') {
		if (isset($_GET['home_id'])) {
			$homeId = $_GET['home_id'];
			$sql = "SELECT * from room where home_id=:home_id";
			$query = $dbh->prepare($sql);
			$query->bindParam(':home_id',$homeId,PDO::PARAM_STR);
			$query->execute();
			$results=$query->fetchAll(PDO::FETCH_OBJ);
			foreach ($results as $value) {
				echo '<option>-- Chọn phòng --</option>';
				echo '<option value="'. $value->id .'">'. $value->name .'</option>';
      		}
		}
	}
?>