  <!DOCTYPE html>
<html lang="en">
<head>
  <title>GREETING BE</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- <meta http-equiv="refresh" content="1"> -->
  <!-- <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}"> -->
   <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script> -->
   
   <script type="text/javascript" src="jquery.js"></script>
   <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
   <!-- <script data-main="your-Scrpt.js" src="require.js"></script> -->
   
   <script>
     //begin emotion
  //    function jst()
  // {
  //   var i = 0;
  //   i = "<?php
  //     $myfile = fopen("/home/blueeyes1/smartbuilding/smartbuilding/smartbuilding/Blue_eyes/hide_on_push/emotion_values.txt", "r") or die("Unable to open file!");
  //   echo fgets($myfile);
  //   fclose($myfile);?>";
  //   console.log(i);
  //   return i;
  // }

setInterval(function () {
    $('#emotions').load("../Blue_eyes/hide_on_push/emotion_values.txt");
  },500)

  //end emotion

setInterval(function(){
   $('#myframe1').load("../Blue_eyes/hide_on_push/name_id.txt");
}, 500) /* time in milliseconds (ie 2 seconds)*/

setInterval(function(){
   $('#myframe2').load("../Blue_eyes/hide_on_push/donvi.txt");
}, 500) /* time in milliseconds (ie 2 seconds)*/

setInterval(function(){
  // var a=;
  $('#myframe3').html('<img src="static/robot/'+String(Math.floor((Math.random() * 10) + 1))+'.gif" width =  "60%"></img>');
}, 1000)
var i = 0;
setInterval(function(){
  if (i==2){
    i=0;
  }
  

  // var a=;
  $('#myframe6').html('<img src="static/robot/welcome_'+String(i)+'.jpg" width="80%"></img>');
  i=i+1;

}, 1000)
var j=0;
setInterval(function(){
  if (j==2){
    j=0;
  }
  

  // var a=;
  $('#myframe7').html('<img src="static/robot/kinhchao_'+String(j)+'.jpg"></img>');
  j=j+1;

}, 1000)

setInterval(function(){
  var now = new Date();
  var hour = now.getHours();
  if (hour>=0 && hour<12){
    a="morning";

  }
  else if(hour>=12 && hour<17){
    a="afternoon";
  }
  else{
    a="evening";
  }
  $('#myframe4').html('<img src="static/when/'+a+'.gif" width =  "30%"></img>');
}, 60000)

</script>
<style type="text/css">
@font-face{
    font-family: "Myriad-Pro";  
    src: url(http://www.anaveer.in/honda/font/MYRIADPRO-REGULAR.OTF) format("truetype");
}
.welcome_{ font-family:Myriad-Pro; }

.emotion{
  align : center;
}
</style>

  <link rel="stylesheet" href="ui_2.css">
  <!--script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script-->
</head>
<?php
  $bg = array('backgroundtet.jpg', 'background1.jpg', 'background2.jpg', 'background3.jpg', 'background4.jpg', 'background5.jpg' ); // array of filenames

  $i = rand(0, count($bg)-1); // generate random number size of the array
  $selectedBg = "$bg[$i]"; // set variable equal to which random filename was chosen
?>
<script type="text/javascript">
  setInterval(function(){
    $('body').css('background-image','url(static/background/background'+String(Math.floor(Math.random()*5)+1)+'.jpg')
  },60000)
</script>
<style type="text/css">

body{
/*background: url(static/background/<?php echo $selectedBg; ?>) no-repeat;*/
background-repeat:no-repeat;  background-attachment: fixed;
background-position: 0px -16px;background-size: 100% 100%;
}
</style>
<body> <!--background="static/robot/background_main_.jpg" style="background-repeat:no-repeat;  background-attachment: fixed;
background-position: 0px -16px;background-size: 100% 100%;"-->
  <div class="container-fluid">
    <!-- chia space -->
      <div class="row">
        <div class="col-sm-12"><p></p></div>
      </div>
      <div class="row">
        <div class="col-sm-12"><p></p></div>
      </div>
      <!-- <div class="row">
        <div class="col-sm-12"><p></p></div>
      </div>
      <div class="row">
        <div class="col-sm-12"><p></p></div>
      </div> -->
      <!-- <div class="row">
        <div class="col-sm-12"><p></p></div>
      </div>
      <div class="row">
        <div class="col-sm-12"><p></p></div>
      </div> -->

    <!-- chia space -->
    <div class="row">
                <div class="col-sm-6"><p></p></div>
      </div>
      <div class="row">
        
          <div class="col-sm-5">
            <!--NULL-->
            
          </div>
          
          <div class="col-sm-5" align="center">
          

          <div class="col-sm-2" align="center">
            
            <img src="static/logo_dhdn.jpg" width="120%">
          
          </div>
          <div class="col-sm-1"></div>
            
            <div class="col-sm-2" align="center">
              
              <img src="static/logo_bkdn.jpg" width="120%">
              <!--NULL-->
            </div>

          

        </div>    

        <div class="col-sm-2" align="center">
            <canvas id="canvas" width="200" height="200"
              style="background-color:#ffffff"> 
                <script>
                  var canvas = document.getElementById("canvas");
                  var ctx = canvas.getContext("2d");
                  var radius = canvas.height / 2;
                  ctx.translate(radius, radius);
                  radius = radius * 0.90
                  setInterval(drawClock, 1000);

                  function drawClock() {
                    drawFace(ctx, radius);
                    drawNumbers(ctx, radius);
                    drawTime(ctx, radius);
                  }

                  function drawFace(ctx, radius) {
                    var grad;
                    ctx.beginPath();
                    ctx.arc(0, 0, radius, 0, 2*Math.PI);
                    ctx.fillStyle = 'white';
                    ctx.fill();
                    grad = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05);
                    grad.addColorStop(0, '#333');
                    grad.addColorStop(0.5, 'white');
                    grad.addColorStop(1, '#333');
                    ctx.strokeStyle = grad;
                    ctx.lineWidth = radius*0.1;
                    ctx.stroke();
                    ctx.beginPath();
                    ctx.arc(0, 0, radius*0.1, 0, 2*Math.PI);
                    ctx.fillStyle = '#333';
                    ctx.fill();
                  }

                  function drawNumbers(ctx, radius) {
                    var ang;
                    var num;
                    ctx.font = radius*0.15 + "px arial";
                    ctx.textBaseline="middle";
                    ctx.textAlign="center";
                    for(num = 1; num < 13; num++){
                      ang = num * Math.PI / 6;
                      ctx.rotate(ang);
                      ctx.translate(0, -radius*0.85);
                      ctx.rotate(-ang);
                      ctx.fillText(num.toString(), 0, 0);
                      ctx.rotate(ang);
                      ctx.translate(0, radius*0.85);
                      ctx.rotate(-ang);
                    }
                  }

                  function drawTime(ctx, radius){
                      var now = new Date();
                      var hour = now.getHours();
                      var minute = now.getMinutes();
                      var second = now.getSeconds();
                      //hour
                      hour=hour%12;
                      hour=(hour*Math.PI/6)+
                      (minute*Math.PI/(6*60))+
                      (second*Math.PI/(360*60));
                      drawHand(ctx, hour, radius*0.5, radius*0.07);
                      //minute
                      minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
                      drawHand(ctx, minute, radius*0.8, radius*0.07);
                      // second
                      second=(second*Math.PI/30);
                      drawHand(ctx, second, radius*0.9, radius*0.02);
                  }

                  function drawHand(ctx, pos, length, width) {
                      ctx.beginPath();
                      ctx.lineWidth = width;
                      ctx.lineCap = "round";
                      ctx.moveTo(0,0);
                      ctx.rotate(pos);
                      ctx.lineTo(0, -length);
                      ctx.stroke();
                      ctx.rotate(-pos);
                  }
                </script>
              </canvas>
              <p>
              <div class="col-sm-2" align="center"><div class="col-sm-1" align="center"><iframe src="http://free.timeanddate.com/clock/i73gna6l/n95/fs30/ftb/tt1/tw0/tm1" frameborder="0" width="186" height="36"></iframe></div>
              </div></p>

              <!-- <div class="col-sm-1" align="left"> -->

            </div>
            <!-- <div class="row" align="center"><img src="static/robot/sun.png" width="1%"> -->
              <!-- weather widget start <div align="center" id="m-booked-small-t1-5172"> <div class="booked-weather-120x100 w100-bg" style="background-color:#ffffff; color:#333333; border-radius:4px; -moz-border-radius:4px; width:118px !important; border:none"> <a target="_blank" style="background-color:#2373ca; color:#ffffff;" href="https://www.booked.net/weather/da-nang-33810" class="booked-weather-120x100-city">Da Nang</a> <a target="_blank" class="booked-weather-120x100-bottom" href="https://www.booked.net/"><img src="//s.bookcdn.com/images/letter/s5.gif" alt="booked.net" /></a> <div class="booked-weather-120x100-degree w18"><span class="plus">+</span>22&deg;<sub class="booked-weather-120x100-type">C</sub></div> <div class="booked-weather-120x100-high-low"> <p>High: <span class="plus">+</span>23&deg;</p> <p>Low: <span class="plus">+</span>17&deg;</p> </div> <div style="background-color:#ffffff; color:#333333;" class="booked-weather-120x100-date">Sat, 04.01.2020</div> </div> </div><script type="text/javascript"> var css_file=document.createElement("link"); css_file.setAttribute("rel","stylesheet"); css_file.setAttribute("type","text/css"); css_file.setAttribute("href",'https://s.bookcdn.com/css/w/bw-120-100.css?v=0.0.1'); document.getElementsByTagName("head")[0].appendChild(css_file); function setWidgetData(data) { if(typeof(data) != 'undefined' && data.results.length > 0) { for(var i = 0; i < data.results.length; ++i) { var objMainBlock = document.getElementById('m-booked-small-t1-5172'); if(objMainBlock !== null) { var copyBlock = document.getElementById('m-bookew-weather-copy-'+data.results[i].widget_type); objMainBlock.innerHTML = data.results[i].html_code; if(copyBlock !== null) objMainBlock.appendChild(copyBlock); } } } else { alert('data=undefined||data.results is empty'); } } </script> <script type="text/javascript" charset="UTF-8" src="https://widgets.booked.net/weather/info?action=get_weather_info&ver=6&cityID=33810&type=11&scode=124&ltid=3458&domid=w209&anc_id=39288&cmetric=1&wlangID=1&color=ffffff&wwidth=118&header_color=2373ca&text_color=333333&link_color=ffffff&border_form=3&footer_color=ffffff&footer_text_color=333333&transparent=0"></script> weather widget end -->  
            <!-- </div> -->

            <div class="row">
              
              <div class="col-sm-3"></div>
              <div class="col-sm-6" align="center"><a id="myframe6"></a></div>
              <div class="col-sm-3"></div>
              <!-- <div class="col-sm-3"></div> -->

            </div>

            <div class="row">
              
              <div class="col-sm-3" align = "center"><img src="static/welcome/cogaiaodai.png" width="50%" height = "200%"></div>

              <div class="col-sm-6">
              <p id="emotions"></p>
                <p class="kinhchao">Kính Chào</p>
                
                <div class="row">
                  <div class="col-sm-6"><p></p></div>
                </div>
                <div class="row">
                  <div class="col-sm-6"><p></p></div>
                </div><p id="myframe1" class="certificate"></p>
                <div class="row">
                  <div class="col-sm-6"><p></p></div>
                </div>
                <div class="row">
                  <div class="col-sm-6"><p></p></div>
                </div><p id="myframe2" class="certificate"></p></div>
              <!-- <div class="col-sm-3"></div> -->
              <div class="col-sm-3" align="center" >
                <!--img src="static/robot/sayhi.gif" width="30%" height="100%"--><img src="static/welcome/changtraiaodai.png" width="95%" height="200%">
              </div>
              


            </div>
            <div class = "row">
                

                   <!-- <img src="static/robot/sayhi_1.gif" width="100%" > -->
                <!-- </div> -->
                <div class="col-sm-12" ><!-- <p align=" center"> -->
                  <marquee scrollamount="10" scrolldelay="30" style="height: 100%; width: 100%;">
                    <img src="haveanicedy.png" width="100%"> 
                    <!--h1 style="color : red; font-size:70pt;font-family:arial;"--><!--p class = "event" >HAVE A NICE DAY</p-->
                  </marquee>
                </div>
                <div class="col-sm-2"></div>
            </div>

      </div>


    </div>


  </div>





<p class="wd-footer" align="center">© Bản quyền Trường Đại học Bách khoa - Đại học Đà Nẵng </p>

</body>
</html>