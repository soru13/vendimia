# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

from django.forms import widgets
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'rfc','usuario_registro')
        widgets = {
        'nombre': widgets.TextInput(attrs={"type":"text","pattern":"[a-zA-Z0]+", "placeholder" : 'nombre',"maxlength" : '40','title':'Descripcion','required':True}),
        'apellido_paterno': widgets.TextInput(attrs={"type":"text","pattern":"[a-zA-Z0]+","placeholder" : 'Apellido Paterno', "maxlength" : '40' ,'title':'Modelo','required':True}),
        'apellido_materno': widgets.TextInput(attrs={"type":"text","pattern":"[a-zA-Z0]+","placeholder" : 'Apellido Materno', "maxlength" : '40' ,'title':'Precio','required':True}),
        'rfc': widgets.TextInput(attrs={"type":"text","placeholder" : 'RFC', "maxlength" : '40' ,"min" : '0' ,'title':'Existencia','required':True}),
        'usuario_registro': widgets.TextInput(attrs={"type":"hidden"}),
        }

class FormRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email', 'password1', 'password2','is_active','is_staff','is_superuser','groups')
        exclude = ['groups']
        labels = {
            'is_staff': _('Supervisor'),
            'is_active': _('Usuario Estandar'),
            'is_superuser': _('Administrador General'),
            'first_name': _('Nombres')
        }
        help_texts = {
            'username':_('Solo letras y numeros'),
            'password2':_('Introduzca la misma contrasena que antes, para su verificacion.'),
            'is_active': _('Tendra permiso solo de consulta general y para promover y dar seguimiento a una vacante.'),
            'is_staff': _('Los mismo permiso que el Usuario Estandar, ademas de: Agregar Candidato, Publicar una vacante, Agregar Empresa')
        }
        widgets = {
        'username': widgets.TextInput(attrs={"autofocus":True,"class" : 'radius', "maxlength" : '40' ,'title':'Usuario','required':True}),
        'first_name': widgets.TextInput(attrs={"placeholder" : 'Nombre','title':'Nombre','required':True}),
        'last_name': widgets.TextInput(attrs={'title':'Apellido',"placeholder" : 'Apellido','required':True}),
        'email': widgets.EmailInput(attrs={'title':'Email',"placeholder" : 'Correo Electronico',"class" : 'radius','required':True}),
        'is_active': widgets.CheckboxInput(attrs={'title':'active'}),
        'is_staff': widgets.CheckboxInput(attrs={'title':'staff'}),
        'is_superuser': widgets.CheckboxInput(attrs={'title':'superadmin'}),
        }
    def save(self, commit = True):
        user = super(FormRegistroUsuario, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
