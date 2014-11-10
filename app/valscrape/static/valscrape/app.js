function list_companies(array) {
		$('#company_list').empty();
		for(var i = 0; i < array.length; i++){
			var element = array[i]
			var bar = "<form name='update' class='button' id='button"+element+"' action = 'chart/"+element+"/bar' method = 'POST'><input type='hidden' name='csrfmiddlewaretoken' value='bDgmoBnOLL3Kvh16ZI7hiJeNQVBmianV'><input type = 'submit' value = 'Bar Graph'></form>";
			var polar = "<form name='delete' class='button' id='buttOn"+element+"' action = 'chart/"+element+"/polar' method = 'POST'><input type='hidden' name='csrfmiddlewaretoken' value='bDgmoBnOLL3Kvh16ZI7hiJeNQVBmianV'><input type = 'submit' value = 'Polar Area Chart'></form>";
			
			$('#company_list').append("<li class='companies' id='id"+element+"'>"+element+bar+polar+"</li>");
			$('.button').hide();
		}
	}


$(document).ready(function(){
	$.get('all', function(data){
		list_companies(data['companies']);
	}, 'json');

	$("ul").on('click','.companies', function(){
		var current_id = this.id.slice(2,this.id.length)
		console.log(current_id)
		$('#button'+current_id).toggle();
		$('#buttOn'+current_id).toggle();
	});

})
