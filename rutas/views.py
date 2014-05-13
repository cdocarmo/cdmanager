# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from rutas.models import Visita, VisitaCliente
from clientes.models import Cliente
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
import string
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def ruta_clientes(request, xvendedor=0):
	visita = Cliente.objects.filter(visitacliente__ruta__vendedor__codigo=xvendedor)
	if visita == None:
	    return HttpResponse(return_msg('Rura no encontrada', False))

	data = serializers.serialize("json", visita)
	return HttpResponse(data, mimetype="application/json; charset=uft8")

@csrf_exempt
def ruta_dia(request, xvendedor=0, xdia=0, xhora=0):
	if int(xhora) != int(0):
		xruta = Visita.objects.filter(dia=xdia, hora=xhora, vendedor__codigo=xvendedor)
		visita = Cliente.objects.filter(visitacliente__ruta=xruta)
	else:
		#xruta = Visita.objects.filter(vendedor__codigo=xvendedor)
		visita = Cliente.objects.filter(visitacliente__ruta__vendedor__codigo=xvendedor)
	if visita == None:
		return HttpResponse(return_msg('Rura no encontrada', False))

	data = serializers.serialize("json", visita)
	return HttpResponse(data, mimetype="application/json; charset=uft8")
