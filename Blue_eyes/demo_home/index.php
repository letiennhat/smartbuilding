<?php
	require_once 'connect.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Demo Sbulding</title>
	<link rel="stylesheet" href="css/bootstrap.css">
</head>
<body>
	<div class="container-fluid">
		<form action="">
			<div class="row">
			<div class="col-md-3">
		  		<div class="form-group">
				    <label for="exampleFormControlSelect1">Nhà</label>
				    <select class="form-control" id="home">
				    	<option value="">--Chọn nhà--</option>
				      <?php
			    		$sql = "SELECT * from home";
						$query = $dbh->prepare($sql);
						$query->execute();
						$results=$query->fetchAll(PDO::FETCH_OBJ);
			      		foreach ($results as $value) { ?>
						<option value="<?php echo $value->id ?>"> <?php echo $value->name ?></option>
			      		<?php
			      		}
				      ?>
				    </select>
			  	</div>
			</div>
			<div class="col-md-3">
		  		<div class="form-group">
				    <label for="exampleFormControlSelect1">Phòng</label>
				    <select class="form-control" id="room">
				    </select>
			  	</div>
			</div>
			<div class="col-md-3">
		  		<div class="form-group">
				    <label for="exampleFormControlSelect1">Người ở</label>
				    <select class="form-control" id="person">
				    </select>
			  	</div>
			</div>
		</div>
		</form>
	</div>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
<script src="js/bootstrap.js"></script>
<script>
	$(document).on('change', '#home', function(event) {
		var home_id = $(this).val();
		jQuery.ajax({
		  url: 'get_room.php',
		  type: 'GET',
		  data: {
		  	home_id: home_id
		  },
		  success: function(data) {
		    $('#room').empty();
		    $('#room').append(data);
		  },
		});
	});

	$(document).on('change', '#room', function(event) {
		var room_id = $(this).val();
		jQuery.ajax({
		  url: 'get_person.php',
		  type: 'GET',
		  data: {
		  	room_id: room_id
		  },
		  success: function(data) {
		    $('#person').empty();
		    $('#person').append(data);
		  },
		});
	});
</script>
</body>
</html>
