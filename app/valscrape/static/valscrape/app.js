function stockGraph(value1,value2,name1,name2) {
	
	var barChartData = {
		labels : [ name1, name2 ],
		datasets : [
			{
				fillColor : "rgba(220,220,220,0.5)",
				strokeColor : "rgba(220,220,220,0.8)",
				highlightFill: "rgba(220,220,220,0.75)",
				highlightStroke: "rgba(220,220,220,1)",
				data : [value1,value2]
			},
			{
				fillColor : "rgba(151,187,205,0.5)",
				strokeColor : "rgba(151,187,205,0.8)",
				highlightFill : "rgba(151,187,205,0.75)",
				highlightStroke : "rgba(151,187,205,1)",
				data : [value2]
			}
		]
	}
	window.onload = function(){
		var ctx = document.getElementById("canvas").getContext("2d");
		window.myBar = new Chart(ctx).Bar(barChartData, {
			responsive : true
		});
	}
	console.log('inside')
}
// stockGraph(10,15,"no","yes")

function list_companies(array) {
		$('#company_list').empty();
		for(var i = 0; i < array.length; i++){
			var element = array[i]
			$('#company_list').append("<li><a href='/get/"+element+"'>"+element+"</a></li>");
		}
	}

function trythis() {
	stockGraph(10,15,"no","yes");
}

$(document).ready(function(){
	trythis()

	// $.get('/all', function(data){
	// 	if(data['error']){
	// 		alert(data['error'])
	// 	} else { 
	// 	list_companies(data['stocks']);
	// 	}
	// }, 'json');
	// stockGraph(10,15,"no","yes")
	$.get('/get', function(data){
		console.log('try')
		trythis()
		console.log('past here')
	},'json');
		// function(data){
		// // var element = "<div style='width: 50%''><canvas id='canvas' height='450' width='600'></canvas></div>"
		// // $('#graph').append(element);
		// console.log('hello');
		// var tuple1 = data['pe'][0];
		// var tuple2 = data['pe'][1];
		// stockGraph(10,15,"no","yes");
		// console.log(parseInt(tuple1[1]),parseInt(tuple2[1]),tuple1[0],tuple2[0]);
		// stockGraph(parseInt(tuple1[1]),parseInt(tuple2[1]),tuple1[0],tuple2[0]);


})
