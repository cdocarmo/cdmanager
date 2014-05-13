from django.conf.urls import patterns, url
urlpatterns = patterns('',
	url(r'^ruta_dia/([a-zA-Z0-9]+)/(\d{1})/(\d{1})/$', 'rutas.views.ruta_dia', name='ruta-dia'),
	url(r'^ruta_clientes/([a-zA-Z0-9]+)/$', 'rutas.views.ruta_clientes', name='ruta-clientes'),

)
