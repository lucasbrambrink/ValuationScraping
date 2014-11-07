function list_companies(array) {
		$('#company_list').empty();
		for(var i = 0; i < array.length; i++){
			var element = array[i]
			$('#company_list').append("<li>"+element+"</li>");
		}
	}


$(document).ready(function(){
	$.post()
	$.get('/all', function(data){
		if(data['error']){
			alert(data['error'])
		} else { 
		console.log(data['stocks'])
		list_companies(data['stocks']);
		}
	}, 'json');

})
