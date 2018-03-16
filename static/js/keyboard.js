/**
* Keys Handling
* by Antoine ORDONEZ
**/

var i = 0;

function changeImage(next, rejected, verified) {
	var url = "imageviewer&id=" + i + "&rejected=" + rejected + "&verified=" + verified;

	document.getElementById("imgClickAndChange").src = url;
}

document.onkeydown = function(e) {
	var rejected = false;
	var verified = false;
	var next = 0;

	switch (e.keyCode) {
		case 88:
			next = 1;
			rejected = true;
			verified = true;
			break;
		case 80:
			next = 1;
			rejected = false;
			verified = true;
			break;
		case 37:
		case 40:
			next = -1;
			break;
		case 38:
		case 39:
			next = 1;
			break;
	}
	if (next != 0) {
		i += next;
		changeImage(next, rejected, verified);
	}
};
