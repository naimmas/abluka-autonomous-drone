
hostName = "192.168.1.13"
serverPort = 8080
html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.slidecontainer {
  width: 100%;
}

.slider {
  -webkit-appearance: none;
  width: 100%;
  height: 15px;
  border-radius: 5px;
  background: #d3d3d3;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
}

.slider:hover {
  opacity: 1;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background: #04AA6D;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background: #04AA6D;
  cursor: pointer;
}
</style>
</head>
<body>

<h1>Color Range Sliders</h1>
<div class="slidecontainer">
  <p>Low Hue: <span id="lowHueOut"></span></p>
  <input type="range" min="0" max="255" value="100" class="slider" id="lowHueIn">
  <p>Low Saturation: <span id="lowSatOut"></span></p>
  <input type="range" min="0" max="255" value="168" class="slider" id="lowSatIn">
  <p>Low Value: <span id="lowValOut"></span></p>
  <input type="range" min="0" max="255" value="40" class="slider" id="lowValIn">
  <p>High Hue: <span id="highHueOut"></span></p>
  <input type="range" min="0" max="255" value="145" class="slider" id="highHueIn">
  <p>High Saturation: <span id="highSatOut"></span></p>
  <input type="range" min="0" max="255" value="255" class="slider" id="highSatIn">
  <p>High Value: <span id="highValOut"></span></p>
  <input type="range" min="0" max="255" value="255" class="slider" id="highValIn">
</div>

<h1>Kernels Size Sliders</h1>
<div class="slidecontainer">
  <p>Morph kernel size: <span id="MkerOut"></span></p>
  <input type="range" min="1" max="20" value="5" class="slider" id="MkerIn">
  <p>Gauss kernel size: <span id="GkerOut"></span></p>
  <input type="range" min="1" max="20" value="5" class="slider" id="GkerIn">
</div>
  
<h1>Ortalama payi Slider</h1>
<div class="slidecontainer">
  <p>Ortlama payi: <span id="OpayOut"></span></p>
  <input type="range" min="1" max="150" value="80" class="slider" id="OpayIn">
</div>
  <button onclick="resetAll()">Varsayilanlari ayarla</button>
  <p id="resetBtn"></p>
    <script>

var sliderLhue = document.getElementById("lowHueIn");
var sliderLsat = document.getElementById("lowSatIn");
var sliderLval = document.getElementById("lowValIn");
var sliderHhue = document.getElementById("highHueIn");
var sliderHsat = document.getElementById("highSatIn");
var sliderHval = document.getElementById("highValIn");
var sliderMker = document.getElementById("MkerIn");
var sliderGker = document.getElementById("GkerIn");
var sliderOpay = document.getElementById("OpayIn");

var oHueL = document.getElementById("lowHueOut");
var oSatL = document.getElementById("lowSatOut");
var oValL = document.getElementById("lowValOut");
var oHueH = document.getElementById("highHueOut");
var oSatH = document.getElementById("highSatOut");
var oValH = document.getElementById("highValOut");
var oMker = document.getElementById("MkerOut");
var oGker = document.getElementById("GkerOut");
var oOpay = document.getElementById("OpayOut");

oHueL.innerHTML = sliderLhue.value;
oSatL.innerHTML = sliderLsat.value;
oValL.innerHTML = sliderLval.value;
oHueH.innerHTML = sliderHhue.value;
oSatH.innerHTML = sliderHsat.value;
oValH.innerHTML = sliderHval.value;
oMker.innerHTML = sliderMker.value;
oGker.innerHTML = sliderGker.value;
oOpay.innerHTML = sliderOpay.value;

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

function resetAll(){
  //100, 168, 40, 145, 255, 255, 5, 5
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderLhue?value=100", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderLsat?value=168", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderLval?value=40", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderHhue?value=145", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderHsat?value=255", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderHval?value=255", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderMker?value=5", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderGker?value=5", true);
  xhr.send();
  sleep(100);
xhr.open("GET", "/sliderOpay?value=80", true);
  xhr.send();
  sleep(100);
  sliderLhue.value = 100
  sliderLsat.value = 168
  sliderLval.value = 40
  sliderHhue.value = 145
  sliderHsat.value = 255
  sliderHval.value = 255
  sliderMker.value = 5
  sliderGker.value = 5
  sliderOpay.value = 80
  oHueL.innerHTML = sliderLhue.value;
  oSatL.innerHTML = sliderLsat.value;
  oValL.innerHTML = sliderLval.value;
  oHueH.innerHTML = sliderHhue.value;
  oSatH.innerHTML = sliderHsat.value;
  oValH.innerHTML = sliderHval.value;
  oMker.innerHTML = sliderMker.value;
  oGker.innerHTML = sliderGker.value;
  oOpay.innerHTML = sliderOpay.value;
  document.getElementById("resetBtn").innerHTML = "Ok";
}
sliderLhue.oninput = function() {
  oHueL.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderLhue?value="+this.value, true);
  xhr.send();
}
sliderLsat.oninput = function() {
  oSatL.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderLsat?value="+this.value, true);
  xhr.send();
}
sliderLval.oninput = function() {
  oValL.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderLval?value="+this.value, true);
  xhr.send();
}
sliderHhue.oninput = function() {
  oHueH.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderHhue?value="+this.value, true);
  xhr.send();
}
sliderHsat.oninput = function() {
  oSatH.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderHsat?value="+this.value, true);
  xhr.send();
}
sliderHval.oninput = function() {
  oValH.innerHTML = this.value;
  document.getElementById("resetBtn").innerHTML = "";
  console.log(this.value);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderHval?value="+this.value, true);
  xhr.send();
}
sliderMker.oninput = function() {
  oMker.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderMker?value="+this.value, true);
  xhr.send();
}
sliderGker.oninput = function() {
  oGker.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderGker?value="+this.value, true);
  xhr.send();
}
sliderOpay.oninput = function() {
  oOpay.innerHTML = this.value;
  console.log(this.value);
  document.getElementById("resetBtn").innerHTML = "";
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/sliderOpay?value="+this.value, true);
  xhr.send();
}
</script>

</body>
</html>
"""
import imagezmq
cameraServers = ("RawImage", "FinalImage")
cameraSender = imagezmq.ImageSender(connect_to='tcp://' + hostName + ':5555')

class globalVars:
    oHueL = 0
    oSatL = 0
    oValL = 0
    oHueH = 0
    oSatH = 0
    oValH = 0
    oMker = 0
    oGker = 0
    oOpay = 0
    isNew = False
