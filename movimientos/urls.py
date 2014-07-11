from django.conf.urls import patterns, url
urlpatterns = patterns('',
	url(r'^$', 'movimientos.views.view', name='view'),
	url(r'^guardo_pedido/$', 'movimientos.views.guardo_pedido', name='guardo_pedido'),
	url(r'^cargo-movtos/$', 'movimientos.views.cargo_movtos', name='cargo-movtos'),
	url(r'^cargo_estcta/$', 'movimientos.views.cargo_estcta', name='cargo-estcta'),
	url(r'^pedidos_vendedor/$', 'movimientos.views.ventas_vendedor', name='ventas-vendedor'),
	url(r'^pedidos_vendedor/cargo_pedidovendedor/$', 'movimientos.views.cargo_pedidovendedor', name='cargo-pedidovendedor'),
	url(r'^ver_pedido/([a-zA-Z0-9]+)/$', 'movimientos.views.ver_pedido', name='ver-pedido'),
)
