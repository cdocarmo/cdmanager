# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from articulos.models import Articulo
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view(request):
    template = 'articulos/view-articulos.html'
    data = {}
    return render_to_response( template, data, 
                               context_instance = RequestContext( request ), )


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

def articulo_detalle(request, articulo_slug):
       
    articulo = get_object_or_404(Articulo, slug = articulo_slug)
    return render_to_response('articulos/ver_articulo.html', locals(), 
                              context_instance=RequestContext(request))
  
#@login_required
def modificar_articulo(request, slug_Articulo):
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


