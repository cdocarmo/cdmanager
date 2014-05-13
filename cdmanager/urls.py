from django.conf.urls import patterns, url, include
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('dashboard.urls'),),
	url(r'^articulos/', include('articulos.urls'),),
    url(r'^clientes/', include('clientes.urls'),),
    url(r'^vendedores/', include('vendedores.urls'),),
    url(r'^visitas/', include('rutas.urls'),),
    url(r'^movtos/', include('movimientos.urls'),),
    url(r'^locacion/', include('locacion.urls'),),
    url(r'^login/$','dashboard.views.ingresar', name='ingresar'),
    url(r'^logout/$', 'dashboard.views.cerrar', name='cerrar'),    
    url(
            r'^account/', 
            include('django.contrib.auth.urls')
        ),
        
        #this is the accounts app main url
        url(
            r'^usuarios/', 
            include('usuarios.urls', namespace="accounts")
        ),
    # Examples:
    # url(r'^$', 'cdmanager.views.home', name='home'),
    # url(r'^cdmanager/', include('cdmanager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
