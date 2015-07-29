from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import vista_materias, vista_estudiante, VistaPrincipal


urlpatterns = patterns(
    '',
    url(r'^estudiante_json/', vista_estudiante),
    url(r'^materias_json/', vista_materias),
    url(r'^', VistaPrincipal.as_view()),
)
