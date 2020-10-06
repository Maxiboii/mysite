var lst = [['Івано-Франківська', 1364715, 13968, 0.99999], ['Волинська', 1029847, 8325, 0.8084], ['Вінницька', 1538041, 6452, 0.4195], ['Дніпропетровська', 3161664, 6422, 0.2031], ['Донецька', 4118050, 3650, 0.0886], ['Житомирська', 1202633, 6265, 0.5209], ['Закарпатська', 1252318, 10004, 0.7988], ['Запорізька', 1678303, 4284, 0.2553], ['Київська', 1783191, 9428, 0.5287], ['Кіровоградська', 927297, 1141, 0.123], ['Луганська', 2129902, 1140, 0.0535], ['Львівська', 2505624, 20826, 0.8312], ['Миколаївська', 1114857, 3369, 0.3022], ['Одеська', 2373168, 14069, 0.5928], ['Полтавська', 1380191, 2512, 0.182], ['Рівненська', 1150980, 12770, 0.99999], ['Сумська', 1061903, 4677, 0.4404], ['Тернопільська', 1035415, 13996, 0.99999], ['Харківська', 2647060, 19588, 0.74], ['Херсонська', 1023090, 1250, 0.1222], ['Хмельницька', 1250227, 6432, 0.5145], ['Черкаська', 1185786, 4295, 0.3622], ['Чернівецька', 899246, 14787, 0.99999], ['Чернігівська', 985141, 4409, 0.4476], ['м.Київ', 2963489, 23602, 0.7964]];
var map = document.getElementById('svg');

var oblasti = [];
for (var i = 3; i < map.childNodes.length-1; i += 2) {
	oblasti.push(map.childNodes[i].id.toString());
};
oblasti = oblasti.sort();

var count = 0;
for (var i = 0; i < oblasti.length; i++) {
	var number = (Math.round( 100*255*(1-lst[count][3]) )/100).toString();
	document.getElementById(oblasti[i]).style.fill = 'rgb(249, '.concat(number, ', ', number, ')');
	count += 1;
};

var utility = {date:'2 жовтня 2020', cases:'4 633'};
document.getElementById('cases').innerHTML = 'Випадків сьогодні: <strong>' + utility.cases + '</strong>';
document.getElementsByTagName('h2')[0].childNodes[1].childNodes[1].innerHTML = 'Дані станом на ' + utility.date;

var a_count = 0;
for (var i = 1; i < 2*oblasti.length; i += 2) {
	document.getElementById('tbody').childNodes[i].childNodes[1].childNodes[0].innerHTML = lst[a_count][0];
	document.getElementById('tbody').childNodes[i].childNodes[3].childNodes[0].innerHTML = lst[a_count][1];
	document.getElementById('tbody').childNodes[i].childNodes[5].childNodes[0].innerHTML = lst[a_count][2];
	document.getElementById('tbody').childNodes[i].childNodes[7].childNodes[0].innerHTML = lst[a_count][3];
	a_count += 1;
};
