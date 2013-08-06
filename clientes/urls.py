from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^guardo-cliente/$', 'clientes.views.guardo_cliente', name='guardo-cliente'),
	url(r'^cargo-clientes/$', 'clientes.views.cargo_clientes', name='cargo-clientes'),
    url(r'^$', 'clientes.views.view', name='view-clientes'),
    url(r'^search/$', 'clientes.views.result_search', name = 'new-search'),
    url(r'^(?P<cliente_slug>[\w-]+)/$', \
        'clientes.views.cliente_detalle', name='cliente-detalle'),
    url(r'^([-\w]+)/modificar/$', 'clientes.views.modificar_cliente', name="modificar-cliente"),

)
