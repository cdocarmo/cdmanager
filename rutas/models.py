from django.db import models
from vendedores.models import *
from clientes.models import *
from django.utils.translation import ugettext as _
# Create your models here.
class Visita(models.Model):

	AM = 1
	PM = 2
	NCH = 3
	HORA = (
		(AM, _('AM')),
		(PM, _('PM')),
		(NCH, _('NOCHE')),)

	LUNES = 1
	MARTES = 2
	MIERCOLES = 3
	JUEVES = 4
	VIERNES = 5
	SABADO = 6
	DIA = (
		(LUNES, _('LUNES')),
		(MARTES, _('MARTES')),
		(MIERCOLES, _('MIERCOLES')),
		(JUEVES, _('JUEVES')),
		(VIERNES, _('VIERNES')),
		(SABADO, _('SABADO')),)


	#ruta = models.AutoField(primary_key=True)
	dia = models.IntegerField(choices=DIA, default=1)
	hora = models.IntegerField(choices=HORA, default=1)
	vendedor = models.ForeignKey(Vendedor)

	class Meta:
	    verbose_name = _('Visita')
	    verbose_name_plural = _('Visitas')


	def __unicode__(self):
	    return _("%s, %s") % (self.dia, self.hora)

class VisitaCliente(models.Model):

	#codigo = models.AutoField(primary_key=True)
	ruta = models.ForeignKey(Visita)
	cliente = models.ForeignKey(Cliente)
	orden = models.IntegerField()

	class Meta:
	    verbose_name = _('VisitaCliente')
	    verbose_name_plural = _('VisitaClientes')

	def __unicode__(self):
	    return _("%s, %s") % (self.ruta, self.cliente)

