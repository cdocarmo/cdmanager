from django.db import models
from django.utils.translation import ugettext as _
import datetime
from django.contrib.auth.models import User
from clientes.models import Cliente
from vendedores.models import Vendedor
from articulos.models import Articulo
from decimal import Decimal

class Movimiento(models.Model):
	fecha = models.DateField(auto_now_add=True, verbose_name=u'fecha de creaci\xf3n')
	fecha_hora = models.DateTimeField(auto_now_add=True)
	cliente = models.ForeignKey(Cliente)
	vendedor = models.ForeignKey(Vendedor)
	tipo = models.CharField(max_length=3)
	observa = models.CharField(max_length=250)
	fin = models.BooleanField()
	es_pedido = models.BooleanField(default=True)
	echo = models.BooleanField(default=False)
	id_pedido = models.IntegerField()
	mal_estado = models.BooleanField(default=False)
	vence = models.DateField()

	def __unicode__(self):
		return _("%s") % ("")

	def totalGral(self):
		xT = Decimal(0)
		for xL in self.mis_lineas.all():
			xT += xL.totalValor() - ((xL.totalValor() * Decimal(xL.dto)) / Decimal(100))
		return "%01.2f" % xT

class Lineas(models.Model):
	movto = models.ForeignKey(Movimiento, related_name="mis_lineas")
	producto = models.ForeignKey(Articulo)
	cantidad = models.DecimalField(max_digits=13, decimal_places=3)
	precio = models.DecimalField(max_digits=13, decimal_places=3)
	dto = models.DecimalField(max_digits=13, decimal_places=3)
	combo = models.IntegerField(default=0)
	def __unicode__(self):
		return _("%s,  %s") % ("","")

	def total(self):
		xTotal = self.cantidad * (self.precio - ((self.precio * self.dto) / 100))
		return "%01.2f" % xTotal

	def totalValor(self):
		xTotal = self.cantidad * (self.precio - ((self.precio * self.dto) / 100))
		return Decimal(xTotal)

class Documentos(models.Model):
	fecha = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha de creaci\xf3n')
	cliente = models.ForeignKey(Cliente)
	vendedor = models.ForeignKey(Vendedor)
	tipo = models.CharField(max_length=3)
	observa = models.CharField(max_length=250)
	fin = models.BooleanField()
	es_pedido = models.BooleanField(default=True)
	echo = models.BooleanField(default=False)
	id_pedido = models.IntegerField()
	mal_estado = models.BooleanField(default=False)
	vence = models.DateTimeField(auto_now_add=True, verbose_name=u'fecha de creaci\xf3n')
	total = models.DecimalField(max_digits=13, decimal_places=3)
	saldo = models.DecimalField(max_digits=13, decimal_places=3)
	numero = models.IntegerField()
	serie = models.CharField(max_length=1)
	
	def __unicode__(self):
		return _("%s") % ("")



class DetalleDocu(models.Model):
	movto = models.ForeignKey(Documentos, related_name="mis_lineas")
	producto = models.ForeignKey(Articulo)
	cantidad = models.DecimalField(max_digits=13, decimal_places=3)
	precio = models.DecimalField(max_digits=13, decimal_places=3)
	dto = models.DecimalField(max_digits=13, decimal_places=3)
	combo = models.IntegerField(default=0)
	def __unicode__(self):
		return _("%s,  %s") % ("","")

	def total(self):
		xTotal = self.cantidad * (self.precio - ((self.precio * self.dto) / 100))
		return "%01.2f" % xTotal
