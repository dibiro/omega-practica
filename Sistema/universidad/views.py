import json
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Estudiante, Materia, Asignacion

diccionario_consulta = {}


class VistaPrincipal(TemplateView):
    template_name = "index.html"


def vista_estudiante(request):
    estudiante = Estudiante.objects.all().order_by('pk')
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

    json_data = json.dumps(lista_consulta, indent=4)

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

    json_data = json.dumps(lista_consulta, indent=4)

    return HttpResponse(json_data, content_type='application/json')


def vista_asignacion_por_estudiante(request, pk):
    asignacion = Asignacion.objects.filter(id_estudiante__pk=pk)
    lista_consulta = []
    for i in asignacion:
        diccionario_consulta = {
            'id_asignacion': i.id,
            'materia_asignada': i.codigo_materia.nombre,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta, indent=4)

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

    json_data = json.dumps(lista_consulta, indent=4)

    return HttpResponse(json_data, content_type='application/json')


def vista_materias(request):
    materias = Materia.objects.all()
    lista_consulta = []
    for i in materias:
        diccionario_consulta = {
            'id_materia': i.id,
            'nombre': i.nombre,
            'estado': i.estado,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}

    json_data = json.dumps(lista_consulta, indent=4)
    lista_consulta = []
    return HttpResponse(json_data, content_type='application/json')


def vista_materias_nombre(request):
    materias = Materia.objects.all()
    lista_consulta = []
    for i in materias:
        if request.POST['nombre'] == i.nombre:
            diccionario_consulta = {
                'id_materia': i.id,
                'nombre': i.nombre,
            }
            lista_consulta.append(diccionario_consulta)
            diccionario_consulta = {}

    json_data = json.dumps(lista_consulta, indent=4)

    return HttpResponse(json_data, content_type='application/json')


def estudiante(request):
    msg = ''
    lista_errores = []
    if str(request.POST['nombre']) is '':
        msg = 'El nombre no puede estar vacio '
        lista_errores.append(msg)
    if str(request.POST['apellido']) is '':
        msg = 'El apellido no puede estar vacio'
        lista_errores.append(msg)
    if str(request.POST['email']) is '':
        msg = 'El email no puede estar vacio'
        lista_errores.append(msg)
    if str(request.POST['cedula']) is '':
        msg = 'La cedula no puede estar vacia'
        lista_errores.append(msg)
    if str(request.POST['edad']) is '':
        msg = 'La edad no puede estar vacia'
        lista_errores.append(msg)
    

    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores, indent=4)
    else:
        estudiante = Estudiante.objects.create(
            first_name=request.POST['nombre'],
            last_name=request.POST['apellido'],
            cedula=request.POST['cedula'],
            edad=request.POST['edad'],
            email=request.POST['email']
        )
        estudiante.save()
        dicc = {
            'id': estudiante.id,
            'nombre': estudiante.first_name,
            'apellido': estudiante.last_name,
            'cedula': estudiante.cedula,
            'edad': estudiante.edad,
            'email': estudiante.email,
        }
        json_data = json.dumps(dicc, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def materias(request):
    msg = ''
    lista_errores = []
    if str(request.POST['nombre_materia']) is '':
        msg = 'El nombre no puede estar vacio '
        lista_errores.append(msg)

    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores, indent=4)
        return HttpResponse(json_data, content_type='application/json')
    else:
        materia = Materia.objects.create(
            nombre=request.POST['nombre_materia']
        )
        materia.save()
        dicc = {
            'nombre': materia.nombre,
            'id': materia.id,
        }

        json_data = json.dumps(dicc, indent=4)
        return HttpResponse(json_data, content_type='application/json')


def asignacion(request, pk):
    lista_errores = []
    msg = ''
    try:
        estudiante = Estudiante.objects.get(id=pk)
        materia = Materia.objects.get(id=request.GET['codigo_materia'])
    except:
        if estudiante is '':
            msg = 'Estudiante no existe o valor invalido'
            lista_errores.append(msg)
        if materia is '':
            msg = 'Materia no existe o valor invalido'
            lista_errores.append(msg)
    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores, indent=4)

    else:
        asignacion = Asignacion.objects.create(codigo_materia=codigo, id_estudiante=pk)
        asignacion.save()
        dicc = {}
        dicc = {
            'respuesta': 'reguistrado exitosamente'
        }
        json_data = json.dumps(dicc, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def desasignacion(request, pk):
    msg = ''
    lista_errores = []
    try:
        asignacion = Asignacion.objects.get(id=pk)
    except:
        if asignacion is '':
            msg = 'Asignacion no existe o valor invalido'
            lista_errores.append(msg)

    if msg is '':
        asignacion = Asignacion.objects.get(id=pk)
        asignacion.delete()
        dicc = {
            'respuesta': 'Asignacion Eliminada'
        }
        json_data = json.dumps(dicc, indent=4)
    else:
        json_data = json.dumps(lista_errores, indent=4)
    return HttpResponse(json_data, content_type='application/json')


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
    json_data = json.dumps(lista_asociacion, indent=4)
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
            if m.estado is True:
                diccionario_consulta = {
                    'codigo_materia': m.id,
                    'materia_no_asignada': m.nombre,
                }
                lista_consulta.append(diccionario_consulta)
                diccionario_consulta = {}

    json_data = json.dumps(lista_consulta, indent=4)

    return HttpResponse(json_data, content_type='application/json')


def materias_asociadas_estudiante(request, pk):
    asignacion = Asignacion.objects.filter(id_estudiante__pk=pk)
    diccionario_consulta = {}
    lista_consulta = []

    for i in asignacion:
        diccionario_consulta = {
            'id_asignacion': i.id,
            'materia_asignada': i.codigo_materia.nombre,
        }
        lista_consulta.append(diccionario_consulta)
        diccionario_consulta = {}
    json_data = json.dumps(lista_consulta, indent=4)

    return HttpResponse(json_data, content_type='application/json')


def eliminar_estudiante(request, pk):
    msg = ''
    estudiante = Estudiante.objects.get(id=pk)
    if str(estudiante.first_name) is '':
        msg = 'Estudiante no existe'

    if msg is '':
        if estudiante.estado is True:
            estudiante.estado = False
        else:
            estudiante.estado = True
        estudiante.save()
        msg = 'Estado del Estudiante ' + estudiante.first_name + ' cambiado'
        lista = []
        lista.append(msg)
    json_data = json.dumps(lista, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def eliminar_materia(request, pk):
    msg = ''
    try:
        materia = Materia.objects.get(id=pk)
    except:
        msg = 'Materia no existe'
    if msg is '':
        if materia.estado is True:
            materia.estado = False
        else:
            materia.estado = True
        materia.save()
        msg = 'Estado de la Materia %s cambiado' % (materia.nombre)
        dicc = {
            'respuesta': msg
        }
    json_data = json.dumps(dicc, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def actualizar_estudiante(request, pk):
    msg = ''
    lista_errores = []
    try:
        estudiante = Estudiante.objects.get(id=pk)
    except:
        msg = 'Estudiante no existe'
        lista_errores.append(msg)
    if msg is '':
        if str(request.POST['nombre']) is '':
            msg = 'El nombre no puede estar vacio '
            lista_errores.append(msg)
        if str(request.POST['apellido']) is '':
            msg = 'El apellido no puede estar vacio'
            lista_errores.append(msg)
        if str(request.POST['email']) is '':
            msg = 'El email no puede estar vacio'
            lista_errores.append(msg)
        if str(request.POST['cedula']) is '':
            msg = 'La cedula no puede estar vacia'
            lista_errores.append(msg)
        if str(request.POST['edad']) is '':
            msg = 'La edad no puede estar vacia'
            lista_errores.append(msg)
        
    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores, indent=4)
    else:
        estudiante.first_name = request.POST['nombre']
        estudiante.last_name = request.POST['apellido']
        estudiante.cedula = request.POST['cedula']
        estudiante.edad = request.POST['edad']
        estudiante.email = request.POST['email']
        estudiante.save()
        dicc = {
            'id': estudiante.id,
            'nombre': estudiante.first_name,
            'apellido': estudiante.last_name,
            'cedula': estudiante.cedula,
            'edad': estudiante.edad,
            'email': estudiante.email,
        }
        json_data = json.dumps(dicc, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def actualizar_materia(request, pk):
    msg = ''
    lista_errores = []
    try:
        materias = Materia.objects.get(id=pk)
    except:
        msg = 'materias no existe'
        lista_errores.append(msg)
    if msg is '':
        if str(request.POST['nombre_materia']) is '':
            msg = 'El nombre de la materia no puede venir vacio'
            lista_errores.append(msg)
    if msg is '':
        materias.nombre = request.POST['nombre_materia']
        materias.save()
    if len(lista_errores) > 0:
        json_data = json.dumps(lista_errores, indent=4)
    else:
        dicc = {
            'nombre': materias.nombre,
            'id': materias.id,
        }
        json_data = json.dumps(dicc, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def actualizar_asignacion(request, pk):
    msg = ''
    try:
        asignacion = Asignacion.objects.get(id=pk)
        estudiante = Estudiante.objects.get(id=request.POST['id_estudiante'])
        materia = Materia.objects.get(id=request.POST['codigo_materia'])
    except:
        if asignacion is '':
            msg = 'Asignacion no existe o valor invalido '
        if estudiante is '':
            msg = msg + 'Estudiante no existe o valor invalido '
        if materia is '':
            msg = msg + 'Materia no existe o valor invalido'

    if msg is '':
        asignacion.codigo_materia = request.POST['codigo_materia']
        asignacion.id_estudiante = request.POST['id_estudiante']
        asignacion.save()
        msg = 'Reguistro del Asignacion del estudiante %s %s %s con la materia %s cambiado' % (asignacion.id_estudiante.first_name, asignacion.id_estudiante.last_name, asignacion.id_estudiante.cedula, asignacion.codigo_materia.nombre)
    json_data = json.dumps(msg, indent=4)
    return HttpResponse(json_data, content_type='application/json')
