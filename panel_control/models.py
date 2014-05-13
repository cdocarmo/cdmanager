from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class PanelControl(models.Model):

	tiene_ruta = models.BooleanField(default=True)

	class Meta:
	    verbose_name = _('PanelControl')
	    verbose_name_plural = _('PanelControl')

