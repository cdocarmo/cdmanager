from django.contrib import admin
from models import *


class Visitas(admin.TabularInline):
	model = VisitaCliente
	extra = 0


class VisitaAdmin(admin.ModelAdmin):
	inlines = [Visitas]
	#prepopulated_fields = {"slug": ("nombre", )}
	fieldsets = (
			(None, {
					'fields': (('dia', 'hora'),
						'vendedor')
				}),
		)
	list_display = ['vendedor', 'dia', 'hora']
	list_filter = ['vendedor']
	ordering = ('dia', 'hora' )

class VisitaClienteAdmin(admin.ModelAdmin):
	#prepopulated_fields = {"slug": ("nombre", )}
	fieldsets = (
			(None, {
					'fields': ('ruta', 'cliente',
						'orden')
				}),
		)
	list_display = ['cliente', 'ruta', 'orden']
	list_filter = ['cliente']
	ordering = ('ruta', 'orden' )


admin.site.register(Visita, VisitaAdmin)
admin.site.register(VisitaCliente, VisitaClienteAdmin)
