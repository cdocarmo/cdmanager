from django.conf.urls import patterns, url
urlpatterns = patterns('',
	url(r'^$', 'movimientos.views.view', name='view'),
	url(r'^guardo_pedido/$', 'movimientos.views.guardo_pedido', name='guardo_pedido'),
	url(r'^cargo-movtos/$', 'movimientos.views.cargo_movtos', name='cargo-movtos'),
	url(r'^cargo_estcta/$', 'movimientos.views.cargo_estcta', name='cargo-estcta'),
	url(r'^ventas_vendedor/$', 'movimientos.views.ventas_vendedor', name='ventas-vendedor'),
	url(r'^ventas_vendedor/cargo_ventasvendedor/$', 'movimientos.views.cargo_ventasvendedor', name='cargo-ventasvendedor'),
	
)
