import json
from django.http import HttpResponse
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

    lista_consulta = []
    diccionario_consulta = {}
    if request.POST['nombre']:

        diccionario_consulta = {
            'nombre': request.POST['nombre'],
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}
        if request.POST['apellido']:
            diccionario_consulta = {
                'apellido': request.POST['apellido'],
            }
            lista_consulta.append(diccionario_consulta)
            diccionario_consulta = {}
            if request.POST['edad']:
                diccionario_consulta = {
                    'edad': request.POST['edad'],
                }
                lista_consulta.append(diccionario_consulta)
                diccionario_consulta = {}
            else:
                diccionario_consulta = {
                    'edads': 'Falta Colocar el Edad',
                }
                lista_consulta.append(diccionario_consulta)
                diccionario_consulta = {}
                json_data = json.dumps(lista_consulta)
        else:
            diccionario_consulta = {
                'Apellidos': 'Falta Colocar el Apellido',
            }
            lista_consulta.append(diccionario_consulta)
            diccionario_consulta = {}
            json_data = json.dumps(lista_consulta)
    else:
        diccionario_consulta = {
            'nombre': 'Falta Colocar el Nombre',
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}
        json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')
