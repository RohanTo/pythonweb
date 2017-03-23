#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """ 
<html>
<head><title>My Python Project</title>
<link href="menu.css" rel="stylesheet" />
<style>
#outer{
width:1000px;
height:1100px;
/*border:1px solid black;*/
margin:0 auto;
border-radius:25px;
}
#menu{
width:1000px;
height:50px;
background-color:white;
border-radius:25px 25px 0px 0px;
}
#header{
width:1000px;
height:150px;
}
#logo{
width:150px;
height:150px;
background-color:aqua;
float:left;
}
#banner{
width:850px;
height:150px;
background-color:navy;
float:left;
}
#slider{
width:1000px;
height:250px;
background-color:gray;
}
#container{
width:1000px;
height:600px;
}
#left{
width:300px;
height:600px;
background-color:aqua;
float:left;
}
#main{
width:700px;
height:600px;
background-color:white;
float:left;
}
#footer{
width:1000px;
height:50px;
background-color:black;
border-radius:0px 0px 25px 25px;
color:white;
text-align:center;
}

</style>
<script>
var imgno=1;
function moveslider()
{
if(imgno>4)
imgno=1;
document.getElementById("slide").src="images/"+imgno+".jpg";
imgno++;
window.setTimeout("moveslider()",2000);
}
</script>
</head>
<body bgcolor="violet" onload="moveslider()">
<form>
<div id="outer"> 
<div id="menu">
<ul>
<li><a href="index.py">Home</a></li>
<li><a href="about.py">About us</a></li>
<li><a href="Registration.py">Registration</a></li>
<li><a href="login.py">Login</a></li>
</ul>
</div>
<div id="header">
<div id="logo">
<img src="images/logo.jpg" width="150" height="150" /></div>
<div id="banner">
<img src="images/banner.gif" width="850" height="150" /></div>
</div>
<div id="slider"><img id="slide" width="1000" height="250" /></div>
<div id="container">
<div id="left"></div>
<div id="main"></div>
</div>
<div id="footer"></div>
</div>
</form>
</body>
</html>