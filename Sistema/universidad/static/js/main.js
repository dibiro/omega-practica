$(document).ready(function() { 

    asignatura.hide();
    fill_student();
    fill_materia();


})
var asignatura= $('.contenedor-asignatura');
var tablaEstudiante= $('#estudiantes').dataTable({
    'scrollX':true
});

var tablaMateria= $('#materia').dataTable();

var tablaAsignatura= $('#asignaturas_asociadas').dataTable({
    'scrollX':true,
    'bPaginate':false,
    'searching':false,
});
var tablaAsignaturaNoAsociadas= $('#asignaturas_noAsociadas').dataTable({
    'sScrollInfinite':true,
    'bPaginate':false,
    'searching':false,
});

function fill_student () {
    tablaEstudiante.fnClearTable();
    $.getJSON('/unerg/estudiante_json', function(json, textStatus) {
        $.each(json, function(index, val) {		
            var addData=[];
            addData.push(val.nombre);
            addData.push(val.apellido);
            addData.push(val.cedula);
            addData.push(val.edad);
            addData.push(val.email);
            if (val.id_estudiantee) {
            	addData.push("<div class='make-switch' class='estado' ><input type='checkbox' name='my-checkbox' data-id="+val.id_estudiantee+" checked></div>");
            }
            else{
            	addData.push("<div class='make-switch' class='estado' ><input type='checkbox' name='my-checkbox' data-id="+val.id_estudiantee+"> </div>");
            }
            addData.push("<button class='btn btn-success asignaturas' data-id="+val.id_estudiantee+">asignatura</button>");
            tablaEstudiante.fnAddData(addData);

        });
        evento_click_asociaciones();
        evento_click_estudiante();
        $("[name='my-checkbox']").bootstrapSwitch({
        	'size':'mini',
        	'onColor':'success',
        	'offColor':'danger',
        	'handleWidth':10,
        	'labelWidth':5,
        	'onText':"<i class='icon-user-check'></i>",
        	'offText':"<i class='icon-cross'></i>"
        });
        tablaEstudiante.fnAdjustColumnSizing();
      
    })
}

function fill_materia(){

    $.getJSON('/unerg/materias_json', function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData=[];
            addData.push(val.nombre);
            tablaMateria.fnAddData(addData);	
        });
        tablaMateria.fnAdjustColumnSizing();
    });

}

function fill_asignaturas(id){
    tablaAsignatura.fnClearTable();
    $.getJSON('/unerg/materias_asociadas_estudiante_json/'+id, function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData=[];
            addData.push(val.materia_asignada);
            addData.push("<div class='make-switch'><input type='checkbox'  name='asignar' checked></div>")
            tablaAsignatura.fnAddData(addData);
        });
        $("[name='asignar']").bootstrapSwitch({
        	'size':'mini',
        	'onColor':'success',
        	'offColor':'danger',
        	'handleWidth':10,
        	'labelWidth':5,
        	'onText':"<i class='icon-check'></i>",
        	'offText':"<i class='icon-cross'></i>"
        });
        tablaAsignatura.fnAdjustColumnSizing();

  
    });

 }
 function update_state(id){
 	$.get('/unerg/eliminar_estudiante_json/'+id);
 
 }

function evento_click_estudiante () {
    $('.asignaturas').unbind('click');
    $('.asignaturas').on('click', function() {
        fill_asignaturas($(this).data('id'));
        asignatura.show(1000);
    });
}
function evento_click_asociaciones(){
	$("[name='my-checkbox']").on('switchChange.bootstrapSwitch', function(event) {
        update_state($(this).data('id'));
    });	
}