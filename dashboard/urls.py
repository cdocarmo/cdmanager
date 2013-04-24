from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dashboard.views',
    url(r'^$', 'index'),
    #url(r'^contacto/$', 'contacto'),
	#url(r'^principal/$', 'principal'),
)
