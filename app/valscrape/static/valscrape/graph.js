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
	window.onload = function(){
		var ctx = document.getElementById("canvas").getContext("2d");
		window.myBar = new Chart(ctx).Bar(barChartData, {
			responsive : true
		});
	}
}
function radarChart(chart_labels,chart_data,chart_average) {
	
	var radarChartData = {
		labels: chart_labels,
		datasets: [
			{
				label: "Data",
				fillColor: "rgba(220,220,220,0.2)",
				strokeColor: "rgba(220,220,220,1)",
				pointColor: "rgba(220,220,220,1)",
				pointStrokeColor: "#fff",
				pointHighlightFill: "#fff",
				pointHighlightStroke: "rgba(220,220,220,1)",
				data: chart_data
			},
			{
				label: "Average",
				fillColor: "rgba(151,187,205,0.2)",
				strokeColor: "rgba(151,187,205,1)",
				pointColor: "rgba(151,187,205,1)",
				pointStrokeColor: "#fff",
				pointHighlightFill: "#fff",
				pointHighlightStroke: "rgba(151,187,205,1)",
				data: chart_average
			}
		]
	};

	window.onload = function(){
		window.myRadar = new Chart(document.getElementById("canvas").getContext("2d")).Radar(radarChartData, {
			responsive: true
		});
	}
}
function lineChart(chart_labels,chart_data,chart_average) { 
	
	var lineChartData = {
			labels : chart_labels,
			datasets : [
				{
					label: "My First dataset",
					fillColor : "rgba(220,220,220,0.2)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(220,220,220,1)",
					data : chart_data
				},
				{
					label: "My Second dataset",
					fillColor : "rgba(151,187,205,0.2)",
					strokeColor : "rgba(151,187,205,1)",
					pointColor : "rgba(151,187,205,1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(151,187,205,1)",
					data : chart_average
				}
			]

		}

	window.onload = function(){
		var ctx = document.getElementById("canvas").getContext("2d");
		window.myLine = new Chart(ctx).Line(lineChartData, {
			responsive: true
		});
	}
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

		// var polarData = [
		// 		{
		// 			value: 300,
		// 			color:"#F7464A",
		// 			highlight: "#FF5A5E",
		// 			label: "Red"
		// 		},
		// 		{
		// 			value: 50,
		// 			color: "#46BFBD",
		// 			highlight: "#5AD3D1",
		// 			label: "Green"
		// 		},
		// 		{
		// 			value: 100,
		// 			color: "#FDB45C",
		// 			highlight: "#FFC870",
		// 			label: "Yellow"
		// 		},
		// 		{
		// 			value: 40,
		// 			color: "#949FB1",
		// 			highlight: "#A8B3C5",
		// 			label: "Grey"
		// 		},
		// 		{
		// 			value: 120,
		// 			color: "#4D5360",
		// 			highlight: "#616774",
		// 			label: "Dark Grey"
		// 		}

		// 	];

	window.onload = function(){
		var ctx = document.getElementById("chart-area").getContext("2d");
		window.myPolarArea = new Chart(ctx).PolarArea(polarData, {
			responsive:true
		});
	};
}
// New Text Goes Underneath


barChart(['PE','EV / EBITDA','EV / Revenue','Debt / Equity','Return on Equity',' Free Cash / Revenue'],[16.69,4.1,3.73,32.57,10.14,0.645],[20.523,2.451,3.601,40.453,7.859,0.0])