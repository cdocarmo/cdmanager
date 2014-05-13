# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from vendedores.models import Vendedor, PedidoNoEnviado
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
import string

def cargo_vendedores(request):
    vendedores = Vendedor.objects.all().order_by("nombre")
    data = serializers.serialize("json", vendedores)
    return HttpResponse(data, mimetype="application/json; charset=uft8")



def diferenacia_pedido(request, xVend):
	xDif = PedidoNoEnviado.objects.filter(vendedor__codigo=xVend, visto=False)
	data = serializers.serialize("json", xDif)
	return HttpResponse(data, mimetype="application/json; charset=uft8")
