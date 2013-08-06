from django.db import models
from localidades.models  import Localidad
from django.utils.translation import ugettext as _
# Create your models here.
class Cliente(models.Model):
	"""docstring for Cliente"""

	numero = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=150)
	razon = models.CharField(max_length=150)
	direccion = models.CharField(max_length=250)
	telefono = models.CharField(max_length=50)
	celular = models.CharField(max_length=50)
	mail = models.EmailField()
	rut = models.CharField(max_length=50)
	cedula = models.CharField(max_length=50)
	localidad = models.ForeignKey(Localidad)

	def __unicode__(self):
	    return _("%s") % (self.razon)