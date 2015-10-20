from django.db import models


# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=50)
	alumno = models.CharField(max_length=80)
	pais = models.CharField(max_length=20)
	calificacion = models.CharField(max_length=10)
	descripcion = models.TextField(max_length=200)

	def __unicode__(self):
		return self.nombre