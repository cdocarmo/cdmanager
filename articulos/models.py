# coding=UTF-8
from django.db import models
from utils.thumbs import ImageWithThumbsField


# Create your models here.

class Familia(models.Model):
	"""docstring for Familia"""
	nombre = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombre

class SubFamilia(models.Model):
	nombre = models.CharField(max_length=200)
	familia = models.ForeignKey(Familia)

	def __unicode__(self):
		return self.nombre

class Articulo(models.Model):
	codigo = models.AutoField(primary_key=True,blank=True)
	nombre = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	familia = models.ForeignKey(Familia)
	subfamilia = models.ForeignKey(SubFamilia)
	costo = models.DecimalField(max_digits=10, decimal_places=3)
	utilidad = models.DecimalField(max_digits=10, decimal_places=3)
	precio = models.DecimalField(max_digits=10, decimal_places=3)
	observaciones = models.TextField()


	def __unicode__(self):
		return self.nombre
		


class ImagenArticulo(models.Model):
	imagen = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
	producto = models.ForeignKey(Articulo)


