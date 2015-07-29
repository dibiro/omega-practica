$(document).ready(function() {
	$('#estudiantes').dataTable();
	$('#materia').dataTable();
	$('#asignatura').dataTable();
	$.getJSON('/unerg/estudiante_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			 console.log(val.first_name)
			 console.log(val.last_name)
			 console.log(val.cedula)
			 console.log(val.edad)
			 console.log(val.email)
		});
	});
	$.getJSON('/unerg/materias_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			 console.log(val.nombre)
		});
	});
});