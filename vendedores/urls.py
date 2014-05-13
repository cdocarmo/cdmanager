from django.conf.urls import patterns, url
urlpatterns = patterns('',
	url(r'^cargo-vendedores/$', 'vendedores.views.cargo_vendedores', name='cargo-vendedores'),
	url(r'^cargo-diferencia-pedido/([a-zA-Z0-9]+)/$', 'vendedores.views.diferenacia_pedido', name='diferenacia-pedido'),
)
