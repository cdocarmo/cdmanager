from django.conf.urls import patterns, url
urlpatterns = patterns('',
	url(r'^$', 'movimientos.views.view', name='view'),
	url(r'^guardo_pedido/$', 'movimientos.views.guardo_pedido', name='guardo_pedido'),
	url(r'^cargo-movtos/$', 'movimientos.views.cargo_movtos', name='cargo-movtos'),
)
