$(document).ready(function() { 

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
			 addData.push(val.estado);
			 addData.push("<a class='btn btn-success asignaturas' href='/unerg/asignacion_estudiante_json/"+val.id_estudiantee+"' >asignatura</button>");
			 tablaEstudiante.fnAddData(addData);

		});
		tablaEstudiante.fnAdjustColumnSizing();

		$('.asignaturas').on("click", function(){	
		
		asignatura.show(1000);
		var id= $('.asignaturas').attr('href');
		$.load(id ,fill_asignatura(id));

		});

	})

	}

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

	function fill_asignatura(id){
		
		var tablaAsignatura= $('#asignaturas').dataTable({
		'sScrollInfinite':true,
		'bPaginate':false,
		'searching':false,
		});

	$.getJSON(id, function(json, textStatus) {
		$.each(json, function(index, val) {
			 var addData=[];
			 addData.push(val.materia_asignada)
			tablaAsignatura.fnAddData(addData);
		});
		tablaMateria.fnAdjustColumnSizing();
		
	})
}