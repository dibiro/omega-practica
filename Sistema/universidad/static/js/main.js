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
			 addData.push("<button class='btn btn-success asignaturas' value='"+val.id_estudiantee+"' >asignatura</button>");
			 tablaEstudiante.fnAddData(addData);

		});
		tablaEstudiante.fnAdjustColumnSizing();

		$('.asignaturas').on("click", function(){	
		asignatura.show(1000);
		fill_asignatura()
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

	function fill_asignatura(){
	var id= $('.asignaturas').attr('value')
	$.getJSON('/unerg/asignacion_estudiante_json/'+id, function(json, textStatus) {
		$.each(json, function(index, val) {
			 var addData=[];
			 addData.push(val.materia_asignada)
			tablaAsignatura.fnAddData(addData);
		});
		tablaMateria.fnAdjustColumnSizing();

	});
}
