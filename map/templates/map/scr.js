var map = document.getElementById('svg');

var oblasti = [];
for (var i = 3; i < map.childNodes.length-1; i += 2) {
	oblasti.push(map.childNodes[i].id.toString());
};
oblasti = oblasti.sort();

var count = 0;
for (var i = 0; i < oblasti.length; i++) {
    var indx = document.getElementById('tbody').childNodes[i+1].childNodes[7].childNodes[0].innerHTML;
    var n = parseInt(document.getElementById('n').innerHTML.split(" ")[2], 10);
	var number = (Math.round( 100*255*(1-indx*n) )/100).toString();
	document.getElementById(oblasti[i]).style.fill = 'rgb(249, '.concat(number, ', ', number, ')');
	count += 1;
};
