from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import vista_materias, vista_estudiante, VistaPrincipal, vista_estudiante_cedula, vista_materias_nombre

urlpatterns = patterns(
    url(r'index/', VistaPrincipal.as_view()),
    url(r'estudiante_json/', vista_estudiante),
    url(r'materias_json/', vista_materias),
    url(r'estudiante_cedula_json/', vista_estudiante_cedula),
    url(r'materias_nombre_json/', vista_materias_nombre),
)
