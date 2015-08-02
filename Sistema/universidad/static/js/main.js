$(document).ready(function() 
{

    fill_student();
    evento_click_pestaña();
    evento_click_guardarUsuario();
});

var asignatura= $('.contenedor-asignatura');

var tablaEstudiante = $('#estudiantes').dataTable({
    'columnDefs': [
    { className: 'columna', 'targets': [2,4] }
  ]
});
    
var tablaMateria = $('#materia').dataTable();

var tablaAsignatura = $('#asignaturas_asociadas').dataTable({
    'scrollY': '200px',
    'searching': false,
    'bPaginate':false,
     
});
var tablaAsignaturaNoAsociadas = $('#asignaturas_noAsociadas').dataTable({
    'scrollY': '200px',
    'bPaginate':false,
    'searching': false,

});

function fill_student() {

    tablaEstudiante.fnClearTable();
    $.getJSON('/unerg/estudiante_json', function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData = [];
            addData.push(val.nombre);
            addData.push(val.apellido);
            addData.push(val.cedula);
            addData.push(val.edad);
            addData.push(val.email);
            if (val.estado) {
                addData.push("<div class='make-switch estado' ><input type='checkbox' class='status' data-id=" + val.id_estudiantee + " checked></div>");
            } else {
                addData.push("<div class='make-switch estado' ><input type='checkbox' class='status' data-id=" + val.id_estudiantee + "> </div>");
            }
            addData.push("<button class='btn btn-success asignaturas' data-id=" + val.id_estudiantee + ">mostrar</button>");
            tablaEstudiante.fnAddData(addData);

        });
        instanciandoSwitch();
        evento_click_asociaciones('/unerg/eliminar_estudiante_json/');
        evento_click_estudiante();
        tablaEstudiante.fnAdjustColumnSizing();

    })
}

function fill_materia() {
    tablaMateria.fnClearTable()
    $.getJSON('/unerg/materias_json', function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData= [];
            addData.push(val.nombre);
            if (val.estado) {
                addData.push("<div class='make-switch estado' ><input type='checkbox' class='statusM' data-id=" + val.id_materia + " checked></div>");
            } else {
                addData.push("<div class='make-switch estado' ><input type='checkbox' class='statusM' data-id=" + val.id_materia + "> </div>");
            }
            tablaMateria.fnAddData(addData);
        });
        instanciandoSwitch();
        evento_click_asociacionesMateria('/unerg/eliminar_materia_json/');
        tablaMateria.fnAdjustColumnSizing();
    });

}

function fill_asignaturas(id) {
    tablaAsignatura.fnClearTable();
    tablaAsignaturaNoAsociadas.fnClearTable();
    $.getJSON('/unerg/materias_asociadas_estudiante_json/' + id, function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData = [];
            addData.push(val.materia_asignada);
            addData.push("<div class='make-switch id='asignacion' data-id='" + id + "'><input type='checkbox'  class='desasigna' data-id='" + val.id_asignacion + "' checked></div>")
            tablaAsignatura.fnAddData(addData);
        });
        instanciandoSwitch();
        evento_click_asigna();
        tablaAsignatura.fnAdjustColumnSizing();


    });
    $.getJSON('/unerg/materias_no_asociadas_json/' + id, function(json, textStatus) {
        $.each(json, function(index, val) {
            var addData = [];
            addData.push(val.materia_no_asignada);
            addData.push("<div class='make-switch id_asignacion'data-id='" + id + "'><input type='checkbox'  class='asigna' data-id='" + val.codigo_materia + "'></div>")
            tablaAsignaturaNoAsociadas.fnAddData(addData);
        });
        instanciandoSwitch();
        evento_click_asigna();
        tablaAsignaturaNoAsociadas.fnAdjustColumnSizing();

    });
}

function update_state(id, direccion) {
    $.get(direccion + id);

}

function update_relation(id_estudiante, id_materia) {

    $.ajax({
            url: '/unerg/asignacion_guardar_json/' + id_estudiante,
            type: 'GET',
            dataType: 'json',
            data: {
                'codigo_materia': id_materia,
            },
            beforeSend: cook(xhr)
        })
        .done(function() {
            console.log('success');
            fill_asignaturas(id_estudiante);
        })
        .fail(function() {

            console.log('error');
        
        })
        .always(function() {

            
        });


}

function update_desasigna(id_materia, id_estudiante) {

    $.get('/unerg/asignacion_eliminar_json/' + id_materia, function() {
        fill_asignaturas(id_estudiante);
    });

}

function Agregando(direccion, valores) {
    $.ajax({
            url: direccion,
            type: 'POST',
            dataType: 'json',
            data: valores,
        })
        .done(function() {
            $('#myModal').modal('hide')
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            fill_materia();
            fill_student();
        });


};

function evento_click_estudiante() {
    $('.asignaturas').unbind('click');
    $('.asignaturas').on('click', function() {
        $('.cambio').css({
            width:'60%'
        });
        $('.columna').hide(500,function() {
            $('.ocultarAsignatura').show();
        });
        asignatura.show(3000, function() {
          fill_asignaturas($('.asignaturas').data('id'));
        });
    });
    $('.ocultarAsignatura').on('click', function() {
        $('.ocultarAsignatura').hide();
        $('.cambio').css({
            width:'90%'
        });
        $('.columna').show(500);
        asignatura.hide(2000); 
    });
}

function instanciandoSwitch() {
        $('.status,.statusM').bootstrapSwitch({
        'size': 'mini',
        'onColor': 'success',
        'offColor': 'default',
        'handleWidth': 10,
        'labelWidth': 1,
        'onText': "<i class='icon-checkmark'></i>",
        'offText': ""
    });
    $(".asigna,.desasigna").bootstrapSwitch({
        'size': 'mini',
        'onColor': 'success',
        'offColor': 'default',
        'handleWidth': 10,
        'labelWidth': 1,
        'onText': "<i class='icon-checkmark'></i>",
        'offText': ""
    });

}

function evento_click_asociaciones(url) {

    $('.status').on('switchChange.bootstrapSwitch', function(event) {
        update_state($(this).data('id'), url);
    });

}
function evento_click_asociacionesMateria(url) {

    $('.statusM').on('switchChange.bootstrapSwitch', function(event) {
        update_state($(this).data('id'), url);
    });

}
function evento_click_asigna() {
    $('.asigna').on('switchChange.bootstrapSwitch', function(event) {
        update_relation($('.id_asignacion').data('id'), $(this).data('id'));

    });
    $('.desasigna').on('switchChange.bootstrapSwitch', function(event) {
        update_desasigna($(this).data('id'), $('.id_asignacion').data('id'));

    })
}

function evento_click_guardarUsuario() {
    $('.agregar').submit(function(event) {
        Agregando($(this).attr('action'), $(this).serialize());
        return false;
    });
}
function evento_click_pestaña(){
    $('#cargar').on('click', function(){

       fill_materia();
    });
}
