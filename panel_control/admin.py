from django.contrib import admin
from models import *

class PanelAdmin(admin.ModelAdmin):
	#prepopulated_fields = {"slug": ("nombre", )}
	pass
	
admin.site.register(PanelControl, PanelAdmin)
