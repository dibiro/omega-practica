from django.conf.urls import patterns, url
from .views import vista_materias, desasignacion, materias_asociadas_estudiante, materias_no_asociadas, estudiante, materias, asignacion, vista_asignacion_por_estudiante, vista_asignacion, vista_estudiante, VistaPrincipal, vista_estudiante_cedula, vista_materias_nombre, asociar_materia, eliminar_estudiante, eliminar_materia

urlpatterns = patterns(
    url(r'^index/', VistaPrincipal.as_view()),
    url(r'^estudiante_json/', vista_estudiante),
    url(r'^estudiante_guardar_json/', estudiante),
    url(r'^materias_guardar_json/', materias),
    url(r'^asignacion_guardar_json/(?P<pk>[0-9]+)', asignacion),
    url(r'^asignacion_eliminar_json/(?P<pk>[0-9]+)', desasignacion),
    url(r'^materias_json/', vista_materias),
    url(r'^asignacion_json/', vista_asignacion),
    url(r'^estudiante_cedula_json/', vista_estudiante_cedula),
    url(r'^materias_nombre_json/', vista_materias_nombre),
    url(r'^materias_no_asociadas_json/(?P<pk>[0-9]+)', materias_no_asociadas),
    url(r'^materias_asociadas_estudiante_json/(?P<pk>[0-9]+)', materias_asociadas_estudiante),
    url(r'^asignacion_estudiante_json/(?P<pk>[0-9]+)', vista_asignacion_por_estudiante),
    url(r'^asociar_materia_json/(?P<pk>[0-9]+)', asociar_materia),
    url(r'^eliminar_estudiante_json/(?P<pk>[0-9]+)/(?P<estado>[a-z]+)', eliminar_estudiante),
    url(r'^eliminar_materia_json/(?P<pk>[0-9]+)/(?P<estado>[a-z]+)', eliminar_materia),
)
