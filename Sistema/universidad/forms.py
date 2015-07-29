from django import forms
from .models import Estudiante, Materia

class formulario_estudiante(forms.ModelForm):

   class Meta:
      model = Estudiante