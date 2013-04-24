from django import forms
from articulos.models import Articulo

class ArticuloForm(forms.ModelForm):
    
    search = forms.CharField(
    			widget=forms.TextInput(
    				attrs={'id':'text-art',
    				'class':'input-text'}))
    class Meta:
        model = Articulo
        fields = ('search',)