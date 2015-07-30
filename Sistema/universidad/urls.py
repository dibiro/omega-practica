from django.conf.urls import patterns, url
from .views import vista_materias, estudiante, materias, asignacion, vista_asignacion_por_estudiante, vista_asignacion, vista_estudiante, VistaPrincipal, vista_estudiante_cedula, vista_materias_nombre

urlpatterns = patterns(
    url(r'^index/', VistaPrincipal.as_view()),
    url(r'^estudiante_json/', vista_estudiante),
    url(r'^estudiante_guardar_json/', estudiante),
    url(r'^materias_guardar_json/', materias),
    url(r'^asignacion_guardar_json/', asignacion),
    url(r'^materias_json/', vista_materias),
    url(r'^asignacion_json/', vista_asignacion),
    url(r'^estudiante_cedula_json/', vista_estudiante_cedula),
    url(r'^materias_nombre_json/', vista_materias_nombre),
    url(r'^asignacion_estudiante_json/(?P<pk>[0-9]+)', vista_asignacion_por_estudiante),
)
