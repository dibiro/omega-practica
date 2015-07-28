$(document).ready(function() {
	$.getJSON('/universidad/estudiante_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			 console.log(val.first_name)
			 console.log(val.last_name)
			 console.log(val.edad)
			 console.log(val.email)
		});
	});
});