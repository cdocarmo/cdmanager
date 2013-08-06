from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('dashboard.urls'),),
	url(r'^articulos/', include('articulos.urls'),),
    url(r'^clientes/', include('clientes.urls'),),
    url(r'^vendedores/', include('vendedores.urls'),),
    url(r'^visitas/', include('rutas.urls'),),
	
    # Examples:
    # url(r'^$', 'cdmanager.views.home', name='home'),
    # url(r'^cdmanager/', include('cdmanager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
