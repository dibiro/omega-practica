$(document).ready(function() {
	var tablaEstudiante= $('#estudiantes').dataTable();
	var tablaMateria= $('#materia').dataTable();
	var tablaAsignatura= $('#asignaturas').dataTable({
		'sScrollInfinite':true,
		'bPaginate':false
	});
	//contenedor de asignaturas
	var asignatura= $('.contenedor-asignatura');
	//ocultando las asignaturas al iniciar la pagina
	 
	//boton para  mostrar el contenedor de asignaturas
	var mostrar = $('#asignatura');

	$.getJSON('/unerg/estudiante_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			
			 var addData=[];
			 addData.push(val.nombre);
			 addData.push(val.apellido);
			 addData.push(val.cedula);
			 addData.push(val.edad);
			 addData.push(val.email);
			 addData.push("<a class='btn btn-success' id='asignatura' href=/unerg/estudiante_json?=val.cedula>asignatura</a>");
			 tablaEstudiante.fnAddData(addData);

		});
		tablaEstudiante.fnAdjustColumnSizing();

	});
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
			 addData.push(val.materia_asignada)
			tablaAsignatura.fnAddData(addData);
		});
		tablaMateria.fnAdjustColumnSizing();

	});
});