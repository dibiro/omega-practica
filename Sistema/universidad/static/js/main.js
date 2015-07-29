$(document).ready(function() {
	var tablaEstudiante= $('#estudiantes').dataTable();
	var tablaMateria= $('#materia').dataTable();
	var tablaAsignatura= $('#asignatura').dataTable();

	fill_student();

	$.getJSON('/unerg/materias_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			var addData=[];
			 addData.push(val.nombre);
			 tablaMateria.fnAddData(addData);	
		});
		tablaMateria.fnAdjustColumnSizing();
	});
	$.getJSON('/unerg/asignacion_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			 var addData=[];
		});
	});
});

function fill_student () {
	$.getJSON('/unerg/estudiante_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			
			 var addData=[];
			 addData.push(val.nombre);
			 addData.push(val.apellido);
			 addData.push(val.cedula);
			 addData.push(val.edad);
			 addData.push(val.email);
			 tablaEstudiante.fnAddData(addData);
		});
		tablaEstudiante.fnAdjustColumnSizing();

	});
}