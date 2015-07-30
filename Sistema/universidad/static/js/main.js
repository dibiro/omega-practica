$(document).ready(function() { 
//temporar luego se cambiara de sitio
	var tablaAsignatura= $('#asignaturas').dataTable({
		'sScrollInfinite':true,
		'bPaginate':false,
		'searching':false,
	});
	//contenedor de asignaturas
	var asignatura= $('.contenedor-asignatura');
	//ocultando las asignaturas al iniciar la pagina

	 asignatura.hide();

	//boton para  mostrar el contenedor de asignaturas
	$('.asignatura').on("click", function(){
		alert("me ejecuto");
		muestrame(asignatura);
	});

	fill_student();
	fill_materia();

})
//mostrando asignaturas
function muestrame(asignatura){
	asignatura.show(1000);
}
//llenado de la dataTable estudiantes 
	function fill_student () {
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
			 addData.push("<a class='btn btn-success' class='asignatura'>asignatura</a>");
			 tablaEstudiante.fnAddData(addData);

		});
		tablaEstudiante.fnAdjustColumnSizing();
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
);
**/