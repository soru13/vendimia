# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from users.models import Perfil
from mixins.mixins import LoginRequired
from mixins.multipleForms import MultiFormsView
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from users.models import Clientes
from articulos.models import Articulos
from django.http import HttpResponse
from .models import Ventas
from .forms import VentasForm
import math
try: import simplejson as json
except ImportError: import json
# from save_the_change.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.

class VentasList(LoginRequired,ListView):
    model = Ventas
    def get_context_data(self, **kwargs):
        context = super(VentasList, self).get_context_data(**kwargs)
        if self.request.user:
            perfil = Perfil.objects.get(user__username=self.request.user.username)
            context['Perfil'] = perfil
        # And so on for more models
        return context

@login_required(login_url = '/login')  
def VentasNew(request):
    perfil = Perfil.objects.get(user__username=request.user.username)
    ventas = Ventas.objects.filter()
    return  render(request, 'ventas/ventas.html', {'forms':VentasForm(),'Perfil':perfil, 'ventas':ventas.count()+1  })

class AutoCompleteView(FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        username = data.get("term")
        results = []
        print '----------------' +username
        if username:
            users = Clientes.objects.filter(nombre__icontains = username)
        else:
            users = Clientes.objects.all()
            results = []
        for user in users:
            print '----------------' +user.nombre
            user_json = {}
            user_json['id'] = user.id
            user_json['value'] = user.rfc
            user_json['label'] = "%s %s %s" % (user.nombre,user.apellido_paterno,user.apellido_materno)

            results.append(user_json)
            data = json.dumps(results)
        return HttpResponse(data, 'application/json')

class AutoCompleteArticulosView(FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        username = data.get("term")
        results = []
        if username:
            arti = Articulos.objects.filter(descripcion__icontains = username)
        else:
            arti = Articulos.objects.all()
            results = []
        for articulo in arti:
            user_json = {}
            user_json['id'] = articulo.id
            user_json['value'] = articulo.descripcion
            user_json['descripcion'] = articulo.modelo
            user_json['existencia'] = articulo.existencia
            user_json['porcentaje_enganche'] = articulo.configuracion.porcentaje_enganche
            user_json['plazo'] = articulo.configuracion.placo_maximo
            tasa = float(articulo.configuracion.tasa_financiamiento)*12/100
            user_json['tasa'] = tasa
            user_json['tasa_financiamiento'] = float(articulo.configuracion.tasa_financiamiento)
            tiempo = float(articulo.configuracion.placo_maximo)/12
            precio =  float(articulo.precio)*(1+(tasa*tiempo))
            user_json['precio'] = round(precio, 2)
            results.append(user_json)
            data = json.dumps(results)
        return HttpResponse(data, 'application/json')


class VentasCreation(LoginRequired,CreateView):
    form_class = VentasForm
    model = Ventas
    success_url = reverse_lazy('ventas:list')
    def get_context_data(self, **kwargs):
        context = super(VentasCreation, self).get_context_data(**kwargs)
        if self.request.user:
            perfil = Perfil.objects.get(user__username=self.request.user.username)
            context['Perfil'] = perfil
            context['ventas'] = Ventas.objects.filter().count()+1
        # And so on for more models
        return context
# class VentasUpdate(LoginRequired,UpdateView):
#     model = Ventas
#     success_url = reverse_lazy('ventas:list')
# #     fields = ['nombre','imagen','url','giro','actividad','telefono','rfc','razonSocial','numeroInterior','numeroEXterior','calle','codigoPostal','ciudad','municipio','estado','pais',
# # 'correo']
#     def get_context_data(self, **kwargs):
#         context = super(VentasUpdate, self).get_context_data(**kwargs)
#         if self.request.user:
#             context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
#         # And so on for more models
#         return context

class VentasDelete(LoginRequired,DeleteView):
    model = Ventas
    success_url = reverse_lazy('ventas:list')
    def get_context_data(self, **kwargs):
        context = super(VentasDelete, self).get_context_data(**kwargs)
        if self.request.user:
            perfil = Perfil.objects.get(user__username=self.request.user.username)
            context['Perfil'] = perfil
        # And so on for more models
        return context