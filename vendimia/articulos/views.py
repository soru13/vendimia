# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from users.models import Perfil
from mixins.mixins import LoginRequired
from .models import Articulos,Configuracion
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .forms import ArticulosForm,configuracionForm
from django.shortcuts import redirect,render
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

class ArticuloDelete(LoginRequired,DeleteView):
    model = Articulos
    success_url = reverse_lazy('articulos:list')
    def get_context_data(self, **kwargs):
        context = super(ArticuloDelete, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
        # And so on for more models
        return context

class ArticuloUpdate(LoginRequired,UpdateView):
	form_class = ArticulosForm
	model = Articulos
	success_url = reverse_lazy('articulos:list')
	def get_context_data(self, **kwargs):
		context = super(ArticuloUpdate, self).get_context_data(**kwargs)
		if self.request.user:
			context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
		# And so on for more models
		return context

# Create your views here.
class ArticulosList(LoginRequired,ListView):
	model = Articulos
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super(ArticulosList, self).get_context_data(**kwargs)
		if self.request.user:
			context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
		# And so on for more models
		return context

@login_required(login_url = '/login')
def configuracion(request,peticion=None,id_objeto=0):
	confs = Configuracion.objects.filter()
	if request.method == 'POST':
		if confs.count() > 0:
			objeto = Configuracion.objects.get(id = confs[0].id)
			form = configuracionForm(request.POST or None, instance = objeto)
			if form.is_valid():
				form.save()
				return redirect('/')
		else:
			formulario = configuracionForm(request.POST)
			if formulario.is_valid():
				print 'formulario validado pasamos a guardar'
				formulario.save()
				return redirect('/')
	else:
		perfil = Perfil.objects.get(user__username=request.user.username)
		if confs.count() > 0:
			objeto = Configuracion.objects.get(id = confs[0].id)
			formulario = configuracionForm(instance  = objeto)
		else:
		    formulario = configuracionForm()
		return  render(request, 'articulos/configuracion.html', {'form':formulario,'Perfil':perfil})
	

	

	

class ArticulosCreation(LoginRequired,CreateView):
	form_class = ArticulosForm
	model = Articulos
	success_url = reverse_lazy('articulos:list')

	def get_context_data(self, **kwargs):
		context = super(ArticulosCreation, self).get_context_data(**kwargs)
		if self.request.user:
			perfil = Perfil.objects.get(user__username=self.request.user.username)
			context['Perfil'] = perfil
			if Articulos.objects.count() != 0:
				context['articulos'] = Articulos.objects.latest('id').id +1
			else:
				context['articulos'] =1
			
			if Configuracion.objects.filter().count() == 1:
				context['configuracion'] = Configuracion.objects.filter()[0]
		# And so on for more models
		return context

