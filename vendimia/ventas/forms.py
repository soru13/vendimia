from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets
from .models import Ventas

class VentasForm(forms.ModelForm):
    """ """
    class Meta:
        model = Ventas
        fields = ['articulo','cliente','plazo','abono','ahorro','total_a_pagar','usuario_registro']
        widgets = {
        # 'articulo': widgets.TextInput(attrs={"type":"hidden"}),
        'cliente': widgets.TextInput(attrs={"type":"hidden"}),
        'plazo': widgets.TextInput(attrs={"type":"hidden"}),
        'abono': widgets.TextInput(attrs={"type":"hidden"}),
        'ahorro': widgets.TextInput(attrs={"type":"hidden"}),
        'total_a_pagar': widgets.TextInput(attrs={"type":"hidden"}),
        'usuario_registro': widgets.TextInput(attrs={"type":"hidden"}),
        }
        
