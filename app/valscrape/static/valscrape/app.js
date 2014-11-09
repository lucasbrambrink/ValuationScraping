function list_companies(array) {
		$('#company_list').empty();
		for(var i = 0; i < array.length; i++){
			var element = array[i]
			$('#company_list').append("<li><a href='/chart/"+element+"'>"+element+"</a></li>");
		}
	}



$(document).ready(function(){
	$.get('/all', function(data){
		list_companies(data['companies']);
	}, 'json');

})
