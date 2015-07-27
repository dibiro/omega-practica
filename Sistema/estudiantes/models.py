from django.db import models

class estudiate(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	edad = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	
	def __unicode__(self):
		return self.first_name