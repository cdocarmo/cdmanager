from django.conf.urls import patterns, url


urlpatterns = patterns('',
	url(r'^dispo/$', 'articulos.views.disponible', name='disponible'),
	url(r'^guardo-productos/$', 'articulos.views.guardo_producto', name='guardo-productos'),
	url(r'^cargo-productos/$', 'articulos.views.cargo_productos', name='cargo-productos'),
	url(r'^cargo-combos/$', 'articulos.views.cargo_combos', name='cargo_combos'),
    url(r'^$', 'articulos.views.view', name='view-articulo'),
    url(r'^search/$', 'articulos.views.result_search', name = 'new-search'),
    url(r'^(?P<articulo_slug>[\w-]+)/$', \
        'articulos.views.articulo_detalle', name='articulo-detalle'),
    url(r'^([-\w]+)/modificar/$', 'articulos.views.modificar_articulo', name="modificar-articulo"),
	
	url(r'^stock/([a-zA-Z0-9]+)/$', 'articulos.views.stock_disponible', name='stock-disponible'),
	
)
