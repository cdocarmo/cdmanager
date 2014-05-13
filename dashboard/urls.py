from django.conf.urls import patterns, url
urlpatterns = patterns('dashboard.views',
    url(r'^$', 'index'),
    #url(r'^contacto/$', 'contacto'),
	#url(r'^principal/$', 'principal'),
)
