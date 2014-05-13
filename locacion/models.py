from django.db import models
from django.utils.translation import ugettext as _
import datetime
from django.contrib.auth.models import User
from vendedores.models import Vendedor
from clientes.models import Cliente
class Locacion(models.Model):
	vendedor = models.ForeignKey(Vendedor)
	logitud = models.FloatField()
	latitud = models.FloatField()
	presicion = models.FloatField()
	fecha = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha de creaci\xf3n')
	cliente = models.ForeignKey(Cliente)
