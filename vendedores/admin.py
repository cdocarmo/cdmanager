from django.contrib import admin
from models import *

class VendedorAdmin(admin.ModelAdmin):
	#prepopulated_fields = {"slug": ("nombre", )}
	fieldsets = (
			(None, {
					'fields': ('codigo', 'nombre', 'password')
				}),
		)
	list_display = ['codigo', 'nombre']
	search_fields = ('nombre',)
	ordering = ('nombre', )

admin.site.register(Vendedor, VendedorAdmin)

