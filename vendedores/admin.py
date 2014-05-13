from django.contrib import admin
from models import *

class VendedorAdmin(admin.ModelAdmin):
	#prepopulated_fields = {"slug": ("nombre", )}
	fieldsets = (
			(None, {
					'fields': ('codigo', 'nombre', 'password', 'ventxdia')
				}),
		)
	list_display = ['codigo', 'nombre']
	search_fields = ('nombre',)
	ordering = ('nombre', )


class VendedorClienteAdmin(admin.ModelAdmin):
	#prepopulated_fields = {"slug": ("nombre", )}

	pass


admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(VendedorCliente, VendedorClienteAdmin)
