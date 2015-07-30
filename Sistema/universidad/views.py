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
            'id_estudiantee': i.id,
            'nombre': i.first_name,
            'apellido': i.last_name,
            'cedula': i.cedula,
            'edad': i.edad,
            'email': i.email,
            'estado': i.estado,
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
            'nombre_estudiante': i.id_estudiante.first_name,
            'apellido_de_estudiante': i.id_estudiante.last_name,
            'cedula_del_ estudiante': i.id_estudiante.cedula,
            'materia_asignada': [],
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def vista_asignacion_por_estudiante(request, pk):
    asignacion = Asignacion.objects.filter(id_estudiante__pk=pk)
    lista_consulta = []
    for i in asignacion:
        diccionario_consulta = {
            'id': i.id,
            'materia_asignada': i.codigo_materia.nombre,
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
            'estado': i.estado,
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
    lista_guardado = []
    lista_errores = []
    if request.POST['nombre'] is not '':

        diccionario_consulta = {
            'first_name': request.POST['nombre'],
        }
        lista_guardado.append(diccionario_consulta)
        diccionario_consulta = {}
        if request.POST['apellido'] is not '':
            diccionario_consulta = {
                'last_name': request.POST['apellido'],
            }
            lista_guardado.append(diccionario_consulta)
            diccionario_consulta = {}

            if request.POST['edad'] is not '' and int(request.POST['edad']):
                diccionario_consulta = {
                    'edad': request.POST['edad'],
                }
                lista_guardado.append(diccionario_consulta)
                diccionario_consulta = {}
                if request.POST['email'] is not '':
                    diccionario_consulta = {
                        'email': request.POST['email'],
                    }
                    lista_guardado.append(diccionario_consulta)
                    diccionario_consulta = {}
                    if request.POST['ceduala'] is not '':
                        diccionario_consulta = {
                            'ceduala': request.POST['ceduala'],
                        }
                        lista_guardado.append(diccionario_consulta)
                        diccionario_consulta = {}

                    else:
                        diccionario_consulta = {
                            'cedula': 'Falta Colocar el cedula',
                        }
                        lista_errores.append(diccionario_consulta)
                        diccionario_consulta = {}
                        json_data = json.dumps(lista_errores)
                else:
                    diccionario_consulta = {
                        'emails': 'Falta Colocar el email',
                    }
                    lista_guardado.append(diccionario_consulta)
                    diccionario_consulta = {}
                    json_data = json.dumps(lista_errores)
            else:
                diccionario_consulta = {
                    'edads': 'Falta Colocar el Edad o No un valor numerico',
                }
                lista_errores.append(diccionario_consulta)
                diccionario_consulta = {}
                json_data = json.dumps(lista_errores)
        else:
            diccionario_consulta = {
                'Apellidos': 'Falta Colocar el Apellido',
            }
            lista_errores.append(diccionario_consulta)
            diccionario_consulta = {}
            json_data = json.dumps(lista_errores)
    else:
        diccionario_consulta = {
            'nombre': 'Falta Colocar el Nombre',
        }
        lista_errores.append(diccionario_consulta)
        diccionario_consulta = {}

    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores)

        return HttpResponse(json_data, content_type='application/json')
    else:
        estudiante = Estudiante(**lista_guardado)
        estudiante.save()

        json_data = json.dumps(lista_guardado)
        return HttpResponse(json_data, content_type='application/json')


def materias(request):
    lista_guardado = []
    lista_errores = []
    if request.POST['nombre_materia'] is not '':

        diccionario_consulta = {
            'nombre': request.POST['nombre_materia'],
        }
        lista_guardado.append(diccionario_consulta)
        diccionario_consulta = {}
    else:
        diccionario_consulta = {
            'nombre': 'Falta Colocar el Nombre de la Materia',
        }
        lista_errores.append(diccionario_consulta)
        diccionario_consulta = {}

    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores)

        return HttpResponse(json_data, content_type='application/json')
    else:
        materias = Materia(**lista_guardado)
        materias.save()

        json_data = json.dumps(lista_guardado)
        return HttpResponse(json_data, content_type='application/json')


def asignacion(request, pk):
    lista_guardado = []
    lista_materias = request.POST.get['lista_para_asociar']
    diccionario_consulta = {}
    if len(lista_materias) > 0:
        for i in lista_materias:
            diccionario_consulta = {
                'codigo_materia': i,
                'id_estudiante': pk,
            }
            lista_guardado.append(diccionario_consulta)
            diccionario_consulta = {}
        json_data = json.dumps(lista_guardado)
        asignacion = Asignacion(**lista_guardado)
        asignacion.save()

        return HttpResponse(json_data, content_type='application/json')


def desasignacion(request, pk):
    lista_materias = request.POST.get['lista_para_desasociar']
    if len(lista_materias) > 0:
        for i in lista_materias:
            asignacion = Asignacion.objects.get(id__pk=i)
            asignacion.delete()
    return HttpResponse('materias desvinculada')


def asociar_materia(request):
    estudiante = request.POST['id_estudiante']
    lista_materias = request.POST['materias']
    asociacion = {}
    lista_asociacion = []
    for i in lista_materias:
        asociacion = {
            'codigo_materia': lista_materias,
            'id_estudiante': estudiante,
        }
        lista_asociacion.append(asociacion)
        asociacion = {}
    materias = Asignacion(**lista_asociacion)
    materias.save()
    json_data = json.dumps(lista_asociacion)
    return HttpResponse(json_data, content_type='application/json')


def materias_no_asociadas(request, pk):
    lista_consulta = []
    diccionario_consulta = {}
    asignacion = Asignacion.objects.filter(id_estudiante__pk=pk)
    lista_asig = []
    for l in asignacion:
        lista_asig.append(l.codigo_materia.id)
    lista_materias = Materia.objects.all()
    for m in lista_materias:
        if m.id not in lista_asig:
            diccionario_consulta = {
                'id': m.id,
                'materia_no_asignada': m.nombre,
            }
            lista_consulta.append(diccionario_consulta)
            diccionario_consulta = {}

    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def materias_asociadas_estudiante(request, pk):
    asignacion = Asignacion.objects.filter(id_estudiante__pk=pk)
    diccionario_consulta = {}
    lista_consulta = []

    for i in asignacion:
        diccionario_consulta = {
            'id': i.id,
            'materia_asignada': i.codigo_materia.nombre,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}
    json_data = json.dumps(lista_consulta)

    return HttpResponse(json_data, content_type='application/json')


def eliminar_estudiante(request, pk, estado):
    estudiante = Estudiante.objects.get(id__pk=pk)
    estudiante.estado = estado
    estudiante.save()
    return HttpResponse('Estudiante Eliminado')


def eliminar_materia(request, pk, estado):
    materia = Materia.objects.get(id__pk=pk)
    materia.estado = estado
    materia.save()
    return HttpResponse('Materia Eliminada')
