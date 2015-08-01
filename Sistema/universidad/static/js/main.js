$(document).ready(function() 
{

    fill_student();
    fill_materia();
    evento_click_guardarUsuario();

});
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') 
    {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken= getCookie('csrftoken');


var asignatura= $('.contenedor-asignatura');
var tablaEstudiante = $('#estudiantes').dataTable({
    'scrollX': true,
    'scrollY': '200px',
    'scrollCollapse': true,
});

var tablaMateria = $('#materia').dataTable({
    'scrollY': '200px',
    'scrollCollapse': true,

});

var tablaAsignatura = $('#asignaturas_asociadas').dataTable({
    'scrollX': true,
    'scrollY': '200px',
    'scrollCollapse': true,
    'bPaginate': false,
    'searching': false,
});
var tablaAsignaturaNoAsociadas = $('#asignaturas_noAsociadas').dataTable({
    'scrollX': true,
    'scrollY': '200px',
    'scrollCollapse': true,
    'bPaginate': false,
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
            addData.push("<button class='btn btn-success asignaturas' data-id=" + val.id_estudiantee + ">asignatura</button>");
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
                addData.push("<div class='make-switch estado' ><input type='checkbox' class='status' data-id=" + val.id_materia + " checked></div>");
            } else {
                addData.push("<div class='make-switch estado' ><input type='checkbox' class='status' data-id=" + val.id_materia + "> </div>");
            }
            tablaMateria.fnAddData(addData);
        });
        instanciandoSwitch();
        evento_click_asociaciones('/unerg/eliminar_materia_json/');
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
            addData.push("<div class='make-switch id_asignacion' data-id='" + id + "'><input type='checkbox'  class='desasigna' data-id='" + val.id_asignacion + "' checked></div>")
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
            type: 'POST',
            dataType: 'json',
            data: {
                'codigo_materia': id_materia,
            },
            beforeSend: cook()
        })
        .done(function() {
            console.log('success');
        })
        .fail(function() {

            console.log('error');
        
        })
        .always(function() {
            fill_asignaturas(id_estudiante);
        });

    function cook(xhr) {
        xhr.setRequestHeader('X-CSRFToken' , csrftoken);

    };

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
            width:'65%'
        });
        asignatura.show(2000);
        fill_asignaturas($(this).data('id'));
    });
}

function instanciandoSwitch() {
    $(".status").bootstrapSwitch({
        'size': 'mini',
        'onColor': 'success',
        'offColor': 'default',
        'handleWidth': 10,
        'labelWidth': 5,
        'onText': "<i class='icon-user-check'></i>",
        'offText': "<i class='icon-cross'></i>"
    });
    $(".asigna,.desasigna").bootstrapSwitch({
        'size': 'mini',
        'onColor': 'success',
        'offColor': 'default',
        'handleWidth': 10,
        'labelWidth': 5,
        'onText': "<i class='icon-check'></i>",
        'offText': "<i class='icon-cross'></i>"
    });

}

function evento_click_asociaciones(url) {

    $('.status').on('switchChange.bootstrapSwitch', function(event) {
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