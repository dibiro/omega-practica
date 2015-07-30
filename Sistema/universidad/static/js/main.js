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

var tablaAsignatura= $('#asignaturas').dataTable({
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
            addData.push("<div class='make-switch'><input type='checkbox'  name='my-checkbox'  checked data-size></div>");
            addData.push("<button class='btn btn-success asignaturas' data-id="+val.id_estudiantee+">asignatura</button>");
            tablaEstudiante.fnAddData(addData);

        });
        evento_click_estudiante();
        tablaEstudiante.fnAdjustColumnSizing();
        $("[name='my-checkbox']").bootstrapSwitch();
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

function fill_asignatura(id){
    tablaAsignatura.fnClearTable();
    $.getJSON('/unerg/materias_asociadas_estudiante_json/'+id, function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData=[];
            addData.push(val.materia_asignada)
            tablaAsignatura.fnAddData(addData);
        });
        tablaAsignatura.fnAdjustColumnSizing();

    })
}

function evento_click_estudiante () {
    $('.asignaturas').unbind('click');
    $('.asignaturas').on('click', function() {
        fill_asignatura($(this).data('id'));
        asignatura.show(1000);
    });
}