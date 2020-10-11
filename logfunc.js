 
var cred1=[{email:"div@gmail.com",pwd:"jva"},{email:"rinu@gmail.com",pwd:"html"}];


function check(){
	var x=0;
for (var i = cred1.length - 1; i >= 0; i--) {


 if(document.getElementById("i1").value==cred1[i].email&&document.getElementById("i2").value==cred1[i].pwd)
	{x=9;
 		window.location="home.html";
	}
	}
	if (x==0) {
		alert("Invalid User");
	}


}

