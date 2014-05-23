# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
import string
from django.views.decorators.csrf import csrf_exempt
from clientes.models import Cliente
from localidades.models import Localidad
from movimientos.models import Movimiento, Lineas, Documentos
from vendedores.models import Vendedor
from articulos.models import Articulo
from decimal import Decimal
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def view(request):
    template = 'movtos/ver_movtos.html'
    data = {}
    return render_to_response( template, data, 
                               context_instance = RequestContext( request ), )

@login_required(login_url='/login')
def cargo_movtos(request):
    mov = Movimiento.objects.filter(es_pedido=True).order_by("fecha")
    return render_to_response('movtos/movimientos.html',
                            {'movtos':mov}, 
                            context_instance=RequestContext(request))

def cargo_movtos1(request):
    articulos = Articulo.objects.exclude(stock = 0).order_by("nombre")
    """
    q = request.GET.get( 'Id' )
    q = q.replace("-", " ")
    if q is not None:  
        articulos = articulos.filter(
                                  Q( nombre__contains = q )
                                  ).order_by( 'nombre' )
    """
    data = serializers.serialize("json", articulos)
    return HttpResponse(data, mimetype="application/json; charset=uft8")



@csrf_exempt
def guardo_pedido(request):
    #return HttpResponse("Hola" + str(request.POST))
    xFecha = datetime.now()
    data = str(request.POST['json'])
    xMovto = json.loads(data)
    xLineas = xMovto['lineas']


    xM = Movimiento.objects.filter(
        vendedor=Vendedor.objects.get(codigo=xMovto['vendedor']), 
        cliente=Cliente.objects.get(numero=xMovto['cliente']), 
        id_pedido=int(xMovto['Id']), fin=True, 
        fecha__year=xFecha.year, fecha__month=xFecha.month, fecha__day=xFecha.day)
    #print xMovto['vence']
    if not xM:
        xMov = Movimiento(
            cliente = Cliente.objects.get(numero=xMovto['cliente']),
            vendedor = Vendedor.objects.get(codigo=xMovto['vendedor']),
            tipo = xMovto['tipo'],
            observa = xMovto['detalle'],
            fin=False,
            es_pedido=True,
            id_pedido=xMovto['Id'],
            echo=False,
            mal_estado=xMovto['malestado'],
            vence=xMovto['vence'])
        xMov.save()
        
        for xL in xLineas:
            xArt = Articulo.objects.get(codigo=xL['producto'])
            xLin = Lineas(
                movto = xMov,
                producto = xArt,
                cantidad = float(xL['cantidad']),
                precio = float(xL['precio']),
                dto = float(xL['dto']),
                combo = int(xL['combo']))
            xLin.save()
            xArt.stock = xArt.stock - Decimal(xL['cantidad'])
            xArt.save()

        xMov.fin = True
        xMov.save()
    return HttpResponse(return_msg('ok', True))

def return_msg(mensagem='', success=True):
    resultado = json.dumps( {'erro': mensagem , 'success': str(success)})
    return resultado;

@csrf_exempt
def cargo_estcta(request):
    xD = json.loads(str(request.POST['json']))
    xMov = Documentos.objects.filter(cliente=xD['Cli'], \
        vendedor=Vendedor.objects.get(codigo=xD['Ven'])).order_by("fecha")

    data = serializers.serialize("json", xMov) #.encode('zlib').encode('base64')

    #print json.loads(data.decode('base64').decode('zlib'))
    return HttpResponse(data, mimetype="application/json; charset=uft8")
