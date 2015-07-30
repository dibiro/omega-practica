$(document).ready(function() { 

	var tablaAsignatura= $('#asignaturas').dataTable({
		'sScrollInfinite':true,
		'bPaginate':false,
		'searching':false,
	});
	var asignatura= $('.contenedor-asignatura');
	asignatura.hide();
	fill_student(asignatura);
	fill_materia();

})


	function fill_student (asignatura) {
		var tablaEstudiante= $('#estudiantes').dataTable({
			'scrollX':true
		});

		$.getJSON('/unerg/estudiante_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			
			 var addData=[];
			 addData.push(val.nombre);
			 addData.push(val.apellido);
			 addData.push(val.cedula);
			 addData.push(val.edad);
			 addData.push(val.email);
			 addData.push("<a class='btn btn-success asignaturas' >asignatura</a>");
			 tablaEstudiante.fnAddData(addData);

		});
		tablaEstudiante.fnAdjustColumnSizing();

		$('.asignaturas').on("click", function(){
		
		asignatura.show(1000);
	});
	})


	}
//llenado de la dataTable Materia
	function fill_materia(){

		var tablaMateria= $('#materia').dataTable();
		$.getJSON('/unerg/materias_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			var addData=[];
			 addData.push(val.nombre);
			 tablaMateria.fnAddData(addData);	
		});
		tablaMateria.fnAdjustColumnSizing();
	});

	}


/**asignaciones
	$.getJSON('/unerg/asignacion_json', function(json, textStatus) {
		$.each(json, function(index, val) {
			 var addData=[];
			 addData.push(val.materia_asignada)
			tablaAsignatura.fnAddData(addData);
		});
		tablaMateria.fnAdjustColumnSizing();

	});
);*/

