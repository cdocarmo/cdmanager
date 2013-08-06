from django.contrib import admin
from models import *

class ClienteAdmin(admin.ModelAdmin):
	#prepopulated_fields = {"slug": ("nombre", )}
	fieldsets = (
			(None, {
					'fields': ('numero', ('nombre', 'razon'),
						'direccion', ('telefono', 'celular', 'mail'), 
						('rut', 'cedula'), 'localidad')
				}),
		)
	list_display = ['numero', 'nombre', 'razon', 'direccion', 'rut', 'telefono', 'celular', 'mail']
	list_filter = ['localidad']
	search_fields = ('nombre', 'razon')
	ordering = ('nombre', )

admin.site.register(Cliente, ClienteAdmin)
