$(document).ready(function() {
	var tablaEstudiante= $('#estudiantes').dataTable();
	var tablaMateria= $('#materia').dataTable();
	var tablaAsignatura= $('#asignatura').dataTable();

	$.getJSON('/unerg/estudiante_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			var row = $('<tr />')
			 /**$("<td />").text(val.nombre).appendTo(row)
			 $("<td />").text(val.apellido).appendTo(row)
			 $("<td />").text(val.cedula).appendTo(row)
			 $("<td />").text(val.edad).appendTo(row)
			 $("<td />").text(val.email).appendTo(row)
			 row.appendTo('#estudiantes');**/

		});
	});
	$.getJSON('/unerg/materias_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			 console.log(val.nombre)
		});
	});
});