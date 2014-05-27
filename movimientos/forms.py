from django.forms import ModelForm
from django import forms
#from models import Pedido
from vendedores.models import Vendedor
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime

class VentasxVededorForm(forms.Form):

    vendedor = forms.ModelChoiceField(queryset=Vendedor.objects.none(),
        widget=forms.Select(attrs={'id':"vendedor-venta", 'name':"vendedor"}))

    


    def __init__(self, *args, **kwargs):
        super(VentasxVededorForm, self).__init__(*args, **kwargs)
        self.fields['vendedor'].queryset = Vendedor.objects.all().order_by('nombre')
