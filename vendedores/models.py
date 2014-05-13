from django.db import models
from django.utils.translation import ugettext as _
from clientes.models import Cliente
from articulos.models import Articulo
# Create your models here.
class Vendedor(models.Model):

	#numero = models.AutoField(primary_key=True)
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=150)
	password = models.CharField(max_length=50)
	ventxdia = models.BooleanField(default=True)
	class Meta:
	    verbose_name = _('Vendedor')
	    verbose_name_plural = _('Vendedores')

	def __unicode__(self):
	    return _("%s") % (self.nombre)

class VendedorCliente(models.Model):
	vendedor = models.ForeignKey(Vendedor)
	clientes = models.ManyToManyField(Cliente)

		
class PedidoNoEnviado(models.Model):
	vendedor = models.ForeignKey(Vendedor)
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Articulo)
	cant_pedido = models.DecimalField(max_digits=13, decimal_places=3)
	cant_enviado = models.DecimalField(max_digits=13, decimal_places=3)
	visto = models.BooleanField(default=False)