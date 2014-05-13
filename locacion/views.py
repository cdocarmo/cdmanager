from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
import string
from django.views.decorators.csrf import csrf_exempt
from vendedores.models import Vendedor
from locacion.models import Locacion
from decimal import Decimal
#from datetime import datetime
from locacion.forms import *
from datetime import date, timedelta
import datetime
from django.utils.dateparse import parse_datetime
#import pytz
from clientes.models import Cliente
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def view(request):
    fromLocacion = LocacionForm()
    template = 'locacion/locacion.html'
    data = {'fromLoc':fromLocacion,}


    return render_to_response( template, data, 
                               context_instance = RequestContext( request ), )

def cargo_locacion_vendedor(request):
    xCol = []
    if request.POST:
        xVend = request.POST['vendedor'] 
        xDia = request.POST['fecha']
        xHora = request.POST['hora']
        xHoraIni = " 14:30:00"
        xHoraFin = " 04:59:00"

        if str(xHora) == "AM":
            xHoraIni = " 05:00:00"
            xHoraFin = " 14:31:00"


        xProxDia = datetime.datetime(int(xDia[6:10]), int(xDia[3:5]), int(xDia[0:2]))

        xProxDia += datetime.timedelta(days=1)


        xIni = str(xDia[6:10]) + "-" + str(xDia[3:5]) + "-" + str(xDia[0:2]) + xHoraIni
        xFin = str(xDia[6:10]) + "-" + str(xDia[3:5]) + "-" + str(xDia[0:2]) + xHoraFin
        if str(xHora) == "PM":
            xFin = str(xProxDia.year) + "-" + str(xProxDia.month) + "-" + str(xProxDia.day) + xHoraFin

        #la = pytz.timezone('America/Montevideo')
        n1 = parse_datetime(xIni) # naive object
        n2 = parse_datetime(xFin)
        aware_start_time = str(n1)+"-03:00" #la.localize(n1) # aware object
        aware_end_time = str(n2)+"-03:00" #la.localize(n2)
        xLugar =  Locacion.objects.filter(vendedor=int(xVend), 
            fecha__range=(aware_start_time, aware_end_time)).order_by('fecha')

           #xLugar =  Locacion.objects.filter(vendedor=int(xVend), 
           # fecha__range=(aware_start_time, aware_end_time),
            #  diferencia de 200 presicion__lte=200).order_by('fecha')

        #data = serializers.serialize("json", xLugar, 
        #    fields=('id','fecha','logitud','latitud','presicion', 'cliente'))
        #print data

        
        for xL in xLugar:
            xCol.append({ 'id': xL.id, 
                'logitud': xL.logitud,
                'latitud': xL.latitud,
                'presicion': xL.presicion, 'cliente': xL.cliente.razon,
                'hora': str(xL.fecha.hour-3) + ":" + str(xL.fecha.minute),
                'presicion': xL.presicion, 'dire': xL.cliente.direccion})

    return HttpResponse(
    json.dumps({ 'xCol': xCol }),
    content_type="application/json; charset=uft8"
    ) 


    return HttpResponse(data, mimetype="application/javascript")

@csrf_exempt
def guardo_locacion(request):
    #return HttpResponse("Hola" + str(request.POST))

    data = str(request.POST['json'])
    xMovto = json.loads(data)


    xLoc = Locacion(
        vendedor = Vendedor.objects.get(codigo=xMovto['vendedor']),
        logitud = xMovto['latitud'],
        latitud = xMovto['longitud'],
        presicion = xMovto['precision'],
        cliente = Cliente.objects.get(numero=xMovto['cliente']))
    xLoc.save()
        
    return HttpResponse(return_msg('ok', True))

def return_msg(mensagem='', success=True):
    resultado = json.dumps( {'erro': mensagem , 'success': str(success)})
    return resultado;