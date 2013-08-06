from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.
class Vendedor(models.Model):

	#numero = models.AutoField(primary_key=True)
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=150)
	password = models.CharField(max_length=50)
	class Meta:
	    verbose_name = _('Vendedor')
	    verbose_name_plural = _('Vendedors')

	def __unicode__(self):
	    return _("%s") % (self.nombre)
