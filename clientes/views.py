# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from clientes.models import Cliente
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core import serializers
import string

def view(request):
    template = 'articulos/view-articulos.html'
    data = {}
    return render_to_response( template, data, 
                               context_instance = RequestContext( request ), )

def cargo_clientes(request):
    clientes = Cliente.objects.filter().order_by("nombre")
    """
    q = request.GET.get( 'Id' )
    q = q.replace("-", " ")
    if q is not None:  
        articulos = articulos.filter(
                                  Q( nombre__contains = q )
                                  ).order_by( 'nombre' )
    """
    data = serializers.serialize("json", clientes)
    return HttpResponse(data, mimetype="application/json; charset=uft8")




def guardo_cliente(request):

    coll = request.POST
    #q = request.GET.get('fields')
    print coll
    """
    art = Articulo(
    slug = formulario.cleaned_data['fecha'],
    nombre = formulario.cleaned_data['nombre'],
    familia = formulario.cleaned_data['detalle'],
    subfamilia = formulario.cleaned_data['aquien'],
    precio = request.user.get_profile())
    art.save()    
    """
def result_search(request):
    articulos = Articulo.objects.all().order_by('nombre')
    if request.is_ajax():
        q = request.GET.get( 'q' )
        q = q.replace("-", " ")
        if q is not None:  
            results = articulos.filter(
                                      Q( nombre__contains = q )
                                      ).order_by( 'nombre' )
        paginator = Paginator(results, 25) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            results = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            results = paginator.page(paginator.num_pages)
        template = 'articulos/resultado.html'
        data = {
            'articulos': results,
            'page_obj': results, 
            'paginator': results,
        }
        return render_to_response( template, data, 
                                 context_instance = RequestContext( request ) )

def cliente_detalle(request, articulo_slug):
       
    articulo = get_object_or_404(Articulo, slug = articulo_slug)
    return render_to_response('articulos/ver_articulo.html', locals(), 
                              context_instance=RequestContext(request))
  
#@login_required
def modificar_cliente(request, slug_Cliente):
    empresa = get_object_or_404(Empresa, slug = slug_Empresa)
    servicio = EmpresaServicio.objects.get(empresa=empresa, slug=slug_Servicio) 
    if request.user.is_authenticated() and request.method == "POST":
        form = Modificar_ServicioForm(request.POST)       
        #return HttpResponse(str(form))
        if form.is_valid():
            post = request.POST.copy()
            servicio.descripcion = post['descripcion']
            servicio.nombre =  post['nombre']
            servicio.tags = post['tags']
            servicio.save()
            return HttpResponseRedirect(empresa.get_absolute_url())
    else:
        form = Modificar_ServicioForm()
    context = {
        'form': form,
    }    
    return render_to_response(
        "empresa/modificar-servicio.html", {'servicio_form': form,
                                            'nombre': servicio.nombre, 'descripcion': servicio.descripcion,
                                            'tags': servicio.tags, 'empresa': empresa},
        context_instance=RequestContext(request),
    )


