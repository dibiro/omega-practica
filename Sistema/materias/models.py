from django.db import models

class estudiate(models.Model):
	nombre = models.CharField(max_length=100)
	seccion = models.CharField(max_length=100)
	aula = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.nombre