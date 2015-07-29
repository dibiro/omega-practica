import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from .models import Estudiante, Materia


class VistaPrincipal(TemplateView):
    template_name = "index.html"


def vista_estudiante(request):
    estudiante = Estudiante.objects.all()
    lista_consulta = []
    diccionario_consulta = {}

    for i in estudiante:
        diccionario_consulta = {
            'nombre': i.first_name,
            'apellido': i.last_name,
            'edad': i.edad,
            'email': i.email,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def vista_materias(request):
    materias = Materia.objects.all()
    lista_consulta = []
    diccionario_consulta = {}

    for i in materias:
        diccionario_consulta = {
            'id': i.id,
            'nombre': i.nombre,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')

def estudiante(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })