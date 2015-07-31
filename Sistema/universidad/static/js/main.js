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
            if (val.estado) {
            	addData.push("<div class='make-switch' class='estado' ><input type='checkbox' class='status' data-id="+val.id_estudiantee+" checked></div>");
            }
            else{
            	addData.push("<div class='make-switch' class='estado' ><input type='checkbox' class='status' data-id="+val.id_estudiantee+"> </div>");
            }
            addData.push("<button class='btn btn-success asignaturas' data-id="+val.id_estudiantee+">asignatura</button>");
            tablaEstudiante.fnAddData(addData);

        });
        instanciandoSwitch();
        evento_click_asociaciones();
        evento_click_estudiante();
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
    tablaAsignaturaNoAsociadas.fnClearTable();
    $.getJSON('/unerg/materias_asociadas_estudiante_json/'+id, function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData=[];
            addData.push(val.materia_asignada);
            addData.push("<div class='make-switch'><input type='checkbox'  class='asigna' data-id='"+val.id_materia+"' checked></div>")
            tablaAsignatura.fnAddData(addData);
        });
       instanciandoSwitch();
       evento_click_asigna();
        tablaAsignatura.fnAdjustColumnSizing();

  
    });
    $.getJSON('/unerg/materias_no_asociadas_json/'+id, function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData=[];
            addData.push(val.materia_no_asignada);
            addData.push("<div class='make-switch'><input type='checkbox'  class='asigna' data-id='"+val.codigo_materia+"'></div>")
            tablaAsignaturaNoAsociadas.fnAddData(addData);
        });
        instanciandoSwitch();
        evento_click_asigna();
        tablaAsignaturaNoAsociadas.fnAdjustColumnSizing();

    });
 }
 function update_state(id){
 	$.get('/unerg/eliminar_estudiante_json/'+id,id);
 
 }

function evento_click_estudiante () {
    $('.asignaturas').unbind('click');
    $('.asignaturas').on('click', function() {
    	asignatura.show(3000);
        fill_asignaturas($(this).data('id'));
    });
}
function instanciandoSwitch(){
    $(".status").bootstrapSwitch({
            'size':'mini',
            'onColor':'success',
            'offColor':'danger',
            'handleWidth':10,
            'labelWidth':5,
            'onText':"<i class='icon-user-check'></i>",
            'offText':"<i class='icon-cross'></i>"
        });
     $(".asigna").bootstrapSwitch({
            'size':'mini',
            'onColor':'success',
            'offColor':'danger',
            'handleWidth':10,
            'labelWidth':5,
            'onText':"<i class='icon-check'></i>",
            'offText':"<i class='icon-cross'></i>"
        });

}
function evento_click_asociaciones(){
	$('.status').on('switchChange.bootstrapSwitch', function(event) {
        update_state($(this).data('id'));
    });	
}
function evento_click_asigna(){
    $('.asigna').on('switchChange.bootstrapSwitch',function(event){
        alert($(this).data('id'));
        //update_relation($(this).data('id'));
    })
}
