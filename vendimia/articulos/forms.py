from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets
from .models import Configuracion,Articulos

class configuracionForm(forms.ModelForm):
    """ """
    class Meta:
        model = Configuracion
        fields = ['tasa_financiamiento','porcentaje_enganche','placo_maximo','usuario_registro']
        exclude = ['is_active']
        labels = {
            'tasa_financiamiento': _('Tasa Financiamiento'),
            'porcentaje_enganche': _('Porcentaje Enganche'),
            'placo_maximo': _('Plazo Maximo')
        }
        widgets = {
        'tasa_financiamiento': widgets.TextInput(attrs={"type":"number","placeholder" : 'Tasa Financiamiento', "maxlength" : '40' ,'title':'Tasa Financiamiento','step':'.1','required':True}),
        'porcentaje_enganche': widgets.TextInput(attrs={"type":"number","placeholder" : 'Porcentaje Enganche', "maxlength" : '40' ,'title':'Porcentaje enganche','required':True}),
        'placo_maximo': widgets.TextInput(attrs={"type":"number","placeholder" : 'Plazo Maximo', "maxlength" : '40' ,'title':'plazo maximo','required':True}),
        'usuario_registro': widgets.TextInput(attrs={"type":"hidden"}),
        }

class ArticulosForm(forms.ModelForm):
    """ """
    class Meta:
        model = Articulos
        fields = ['descripcion','modelo','precio','existencia','usuario_registro','configuracion']
        widgets = {
        'descripcion': widgets.TextInput(attrs={"type":"text","placeholder" : 'Descripcion',"maxlength" : '40','title':'Descripcion','required':True}),
        'modelo': widgets.TextInput(attrs={"type":"text","placeholder" : 'Modelo', "maxlength" : '40' ,'title':'Modelo','required':True}),
        'precio': widgets.TextInput(attrs={"type":"number","placeholder" : 'Precio', "maxlength" : '40' ,'title':'Precio','required':True}),
        'existencia': widgets.TextInput(attrs={"type":"number","placeholder" : 'Existencia', "maxlength" : '40' ,"min" : '0' ,'title':'Existencia','required':True}),
        'usuario_registro': widgets.TextInput(attrs={"type":"hidden"}),
        'configuracion': widgets.TextInput(attrs={"type":"hidden"}),
        }
        
