from django.conf.urls import patterns, url
urlpatterns = patterns('',
	url(r'^$', 'locacion.views.view', name='view'),
	url(r'^guardo_locacion/$', 'locacion.views.guardo_locacion', name='guardo_locacion'),
	url(r'^locacion-vendedor/$', 'locacion.views.cargo_locacion_vendedor', name='cargo-locacion-vendedor'),

)
