from django.contrib import admin

from .models import Asignacion
from .models import Materia
from .models import Estudiante

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Asignacion)
