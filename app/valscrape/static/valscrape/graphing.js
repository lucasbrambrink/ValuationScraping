function barChart(chart_labels,chart_data,chart_average) {
	
	var barChartData = {
		labels : chart_labels,
		datasets : [
			{
				fillColor : "rgba(220,220,220,0.5)",
				strokeColor : "rgba(220,220,220,0.8)",
				highlightFill: "rgba(220,220,220,0.75)",
				highlightStroke: "rgba(220,220,220,1)",
				data : chart_average
			},
			{
				fillColor : "rgba(151,187,205,0.5)",
				strokeColor : "rgba(151,187,205,0.8)",
				highlightFill : "rgba(151,187,205,0.75)",
				highlightStroke : "rgba(151,187,205,1)",
				data : chart_data
			}
		]
	}
	var ctx = document.getElementById("canvas").getContext("2d");
	new Chart(ctx).Bar(barChartData, {
		responsive : true
	});
}

function polarAreaChart(chart_labels,chart_data) {
		var polarData = []
		var polarColor = ["#F7464A","#46BFBD","#FDB45C","#949FB1","#4D5360"]
		var polarHL = ["#FF5A5E","#5AD3D1","#FFC870","#A8B3C5","#616774",]
		for(var i = 0; i < chart_labels.length; i++){
			polarData.push({
					value: chart_data[i],
					color: polarColor[i],
					highlight: polarHL[i],
					label: chart_labels[i]
				})
		}
	var ctx = document.getElementById("canvas").getContext("2d");
	new Chart(ctx).PolarArea(polarData, {
			responsive:true
		});
	};



$(document).ready(function(){
	$.get('/valscrape/render',{ SYMBOL: $('#symbol').text() }, function(data){
		console.log(data['bar'])
		if (data['polar']){
		polarAreaChart(data['polar'][0],data['polar'][1])
		} else {
		barChart(data['bar'][0],data['bar'][1],data['bar'][2])
		}
	}, 'json');


})