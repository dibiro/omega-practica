from django.db import models


class Estudiante(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100, unique=True)
    edad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + " C.I:" + self.cedula + " Edad:" + self.edad + " Email:" + self.email


class Materia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nombre


class Asignacion(models.Model):
    codigo_materia = models.ForeignKey(Materia)
    id_estudiante = models.ForeignKey(Estudiante)

    def __unicode__(self):
        return ' Materia:' + self.codigo_materia.nombre + ' Estudante:' + self.id_estudiante.cedula + ' Nombre:' + self.id_estudiante.first_name
