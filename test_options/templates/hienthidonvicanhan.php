<!DOCTYPE html>
<html>
<head>
	<title>donvi</title>
	<script>
		function showInput(str) {
			if (str=="")
			{
				document.getElementById("txtHint").innerHTML="";
			}
			else{
				if (str=="unknown"){
					document.getElementById("txtHint").innerHTML=' <input type="submit" name="choose_donvi" value="Go"> ';
					// document.write();
				}
				else{

					document.getElementById("txtHint").innerHTML='<h2> Xin mời chọn tên bạn muốn xem </h2><textarea name="name_input" width = "200" height = "200"></textarea></br><input type="submit" name="choose_donvi" value="Go">';
				}
			}
		}
	</script>
</head>
<body>
	
	<form action="/hienthi_donvi_canhan" method="POST">
		<!-- <strong style="color: red;">Chỉ hiện thỉ trong vòng 1 tháng</strong> -->
		<h1> Xin mời chọn đơn vị bạn muốn xem </h1>
		<select name="choose_donvi_canhan" onchange="showInput(this.value)">
				<option value="">Chọn Đơn Vị</option>
			{%for op in donvi[:-1]%}
				<option value="{{op[0]}}">{{op[0]}}</option>
			{%endfor%}
		</select>
		<div id="txtHint"></div>
		


	</form>
</body>
</html>