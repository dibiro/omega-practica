from django.db import models


class Estudiante(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __unicode__(self):
        return self.first_name


class Materia(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Asignacion(models.Model):
    codigo_materia = models.ForeignKey(Materia)
    id_estudiante = models.ForeignKey(Estudiante)

    