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
from movimientos.forms import *
from datetime import date, timedelta
import datetime
from django.utils.dateparse import parse_datetime

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

@login_required(login_url='/login')
def ventas_vendedor(request):
    fromVentasVend = VentasxVededorForm()
    template = 'movtos/ventas_vendedor.html'
    data = {'fromVV':fromVentasVend,}


    return render_to_response( template, data, 
                               context_instance = RequestContext( request ), )




def cargo_ventasvendedor(request):
    xCol = []
    if request.POST:
        xVend = request.POST['vendedor'] 
        xDia = request.POST['fecha']
        xHasta = request.POST['hasta']
        xProxDia = datetime.datetime(int(xDia[6:10]), int(xDia[3:5]), int(xDia[0:2]))

        xIni = str(xDia[6:10]) + "-" + str(xDia[3:5]) + "-" + str(xDia[0:2]) + " 00:00:00"
        xFin = str(xHasta[6:10]) + "-" + str(xHasta[3:5]) + "-" + str(xHasta[0:2]) + " 23:59:00"

        #la = pytz.timezone('America/Montevideo')
        n1 = parse_datetime(xIni) # naive object
        n2 = parse_datetime(xFin)
        aware_start_time = str(n1)+"-03:00" #la.localize(n1) # aware object
        aware_end_time = str(n2)+"-03:00" #la.localize(n2)


        xVentas =  Movimiento.objects.filter(vendedor=int(xVend), 
            fecha__range=(aware_start_time, aware_end_time)).order_by('fecha')

        xTotal = Decimal(0)
        for xM in xVentas:
            xCol.append({ 'id': xM.id, 
                'cliente': str(xM.cliente),
                'tipo': xM.tipo,
                'fecha': str(xM.fecha.strftime("%d/%m/%Y")),
                'total': str(xM.totalGral()),})
            xTotal += Decimal(xM.totalGral())
        xCol.append({ 'id': "", 
            'cliente': str(""),
            'fecha': "",
            'tipo': "Total...",
            'total': str(xTotal),})            
    return HttpResponse(
    json.dumps({ 'xCol': xCol }),
    content_type="application/json; charset=uft8"
    ) 


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
