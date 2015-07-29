import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Estudiante, Materia, Asignacion

diccionario_consulta = {}


class VistaPrincipal(TemplateView):
    template_name = "index.html"


def vista_estudiante(request):
    estudiante = Estudiante.objects.all()
    lista_consulta = []
    for i in estudiante:
        diccionario_consulta = {
            'nombre': i.first_name,
            'apellido': i.last_name,
            'cedula': i.cedula,
            'edad': i.edad,
            'email': i.email,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def vista_asignacion(request):
    asignacion = Asignacion.objects.all()
    lista_consulta = []
    for i in asignacion:
        diccionario_consulta = {
            'nombre': i.first_name,
            'apellido': i.last_name,
            'cedula': i.cedula,
            'edad': i.edad,
            'email': i.email,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def vista_estudiante_cedula(request):
    estudiante = Estudiante.objects.all()
    lista_consulta = []
    for i in estudiante:
        if request.POST['cedula'] == i.cedula:
            diccionario_consulta = {
                'nombre': i.first_name,
                'apellido': i.last_name,
                'cedula': i.cedula,
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
    for i in materias:
        diccionario_consulta = {
            'id': i.id,
            'nombre': i.nombre,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)
    lista_consulta = []
    return HttpResponse(json_data, content_type='application/json')


def vista_materias_nombre(request):
    materias = Materia.objects.all()
    lista_consulta = []
    for i in materias:
        if request.POST['nombre'] == i.nombre:
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

            if request.POST['edad'] and int(request.POST['edad']):
                diccionario_consulta = {
                    'edad': request.POST['edad'],
                }
                lista_consulta.append(diccionario_consulta)
                diccionario_consulta = {}
                if request.POST['email']:
                    diccionario_consulta = {
                        'email': request.POST['email'],
                    }
                    lista_consulta.append(diccionario_consulta)
                    diccionario_consulta = {}
                else:
                    diccionario_consulta = {
                        'emails': 'Falta Colocar el email',
                    }
                    lista_consulta.append(diccionario_consulta)
                    diccionario_consulta = {}
                    json_data = json.dumps(lista_consulta)
            else:
                diccionario_consulta = {
                    'edads': 'Falta Colocar el Edad o No un valor numerico',
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


def materias(request):
    lista_consulta = []
    if request.POST['nombre_materia']:

        diccionario_consulta = {
            'nombre': request.POST['nombre_materia'],
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}
    else:
        diccionario_consulta = {
            'nombre': 'Falta Colocar el Nombre de la Materia',
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def asignacion(request):
    lista_consulta = []
    if request.POST['id_materia']:

        diccionario_consulta = {
            'id_materia': request.POST['id_materia'],
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}
        if request.POST['id_estudiante']:

            diccionario_consulta = {
                'id_estudiante': request.POST['id_estudiante'],
            }
            lista_consulta.append(diccionario_consulta)
            diccionario_consulta = {}
        else:
            diccionario_consulta = {
                'id_estudiante': 'Falta Colocar el estudiante',
            }
            lista_consulta.append(diccionario_consulta)
            diccionario_consulta = {}
    else:
        diccionario_consulta = {
            'id_materia': 'Falta Colocar la Materia',
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')
