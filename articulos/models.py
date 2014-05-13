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
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=200)
	familia = models.ForeignKey(Familia)

	def __unicode__(self):
		return self.nombre

class Articulo(models.Model):
	codigo = models.AutoField(primary_key=True, blank=True)
	nombre = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	familia = models.ForeignKey(Familia)
	subfamilia = models.ForeignKey(SubFamilia)
	costo = models.DecimalField(max_digits=10, decimal_places=3)
	utilidad = models.DecimalField(max_digits=10, decimal_places=3)
	precio = models.DecimalField(max_digits=10, decimal_places=3)
	stock = models.DecimalField(max_digits=10, decimal_places=3)
	observaciones = models.TextField()
	new_cod = models.IntegerField()
	es_combo = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre
		
class Combo(models.Model):
	producto = models.ForeignKey(Articulo)
	cantidad = models.DecimalField(max_digits=12, decimal_places=3)

	def __unicode__(self):
		return self.producto.nombre

class ComboProducto(models.Model):
	combo = models.ForeignKey(Combo)
	producto = models.ManyToManyField(Articulo)

	def __unicode__(self):
		return self.combo.producto.nombre


    


class ImagenArticulo(models.Model):
	imagen = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
	producto = models.ForeignKey(Articulo)


