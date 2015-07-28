from django.contrib import admin

from .models import Asignacion, Materia, Estudiante


admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Asignacion)
