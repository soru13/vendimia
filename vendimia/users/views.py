# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from mixins.mixins import LoginRequired
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from .forms import FormRegistroUsuario,ClientesForm
from .models import Perfil,Clientes
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import requests ,random
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView




class PerfilDelete(LoginRequired,DeleteView):
    model = Perfil
    success_url = reverse_lazy('usuarios:list')
    def get_context_data(self, **kwargs):
        context = super(PerfilDelete, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
        # And so on for more models
        return context

class ClienteDelete(LoginRequired,DeleteView):
    model = Clientes
    success_url = reverse_lazy('usuarios:list')
    def get_context_data(self, **kwargs):
        context = super(ClienteDelete, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
        # And so on for more models
        return context

class ClienteList(LoginRequired,ListView):
    model = Clientes
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(ClienteList, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
            
        # And so on for more models
        return context

class Home(LoginRequired,TemplateView):
    template_name = "home/inicio.html"
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
        # And so on for more models
        return context  

# Create your views here.
def NuevoUsuario(request):
    if request.user.is_authenticated():
        loginn=request.user
        if request.method == 'POST':
            print 'entramos a guardar usuario en post'
            formulario = ClientesForm(request.POST)
            if formulario.is_valid():
                print 'formulario validado pasamos a guardar'
                formulario.save()
                # user = User.objects.get(username=request.POST['username'])
                # estado = Estado.objects.get(id=1)
                # municipio = Municipio.objects.get(id=1)
                # print 'Guardamos fotografia y creamos el perfil'
                # p=Candidato(user=user,avatar='AvatarUser/icon_ios_user.png',candidato = True,nombre=user.username,estado=estado,municipio=municipio)
                # p.save();
                # exito = True
                return redirect('/clientes')
        else:
            formulario = ClientesForm()
            perfil = Perfil.objects.get(user__username=request.user.username)

            clientes = 0
            if Clientes.objects.count() != 0:
                clientes = Clientes.objects.latest('id').id +1
            else:
                clientes =1
            return  render(request, 'users/users_form.html', {'form':formulario,'Perfil':perfil,'clientes':clientes })
    else:
        if request.method == 'POST':
            formulario = FormRegistroUsuario(request.POST)
            if formulario.is_valid():
                formulario.save()
                user = User.objects.get(username=request.POST['username'])
                nombre_apellido =  request.POST['nombre_apellido']
                array_name = nombre_apellido.split(" ")
                print array_name
                if len(array_name)==1:
                    user.first_name= array_name[0]
                elif len(array_name)==2:
                    user.first_name= array_name[0]
                    user.last_name= array_name[1]
                else:
                    user.first_name= array_name[0]
                user.is_active = True
                user.save()
                p=Perfil(user=user,avatar='AvatarUser/icon_ios_user.png')
                p.save();
                usuario = request.POST['username']
                clave = request.POST['password1']
                auth_user = login_user(request,usuario,clave)     
                if auth_user is not None:
                    user = User.objects.get(username=request.POST['username'])
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    send_simple_message(str(user.email),user,uid,token)
                    return redirect('/bienvenido')
                else:
                    raise ValueError("Invalid username and password")
            else:
                errores = formulario.errors
                print errores
                return  render(request, 'users/Signup.html', {'form':formulario,'error':errores})
        else:
            formulario = FormRegistroUsuario()
            return  render(request, 'users/Signup.html', {'form':formulario})


def login_user(request, username, password):
    from django.contrib import auth
    print '------------------------'
    print username
    print '------------------------'
    print password
    print '------------------------'
    if not username and password:
        raise ValueError("Invalid username and password")
    auth_user = auth.authenticate(username=username, password=password)
    if auth_user is None:
        raise ValueError("Invalid username and password al authenticar")

    auth.login(request, auth_user)
    return auth_user

class Bienvenido(LoginRequired,TemplateView):
    template_name = "users/bienvenido.html"
    def get_context_data(self, **kwargs):
        context = super(Bienvenido, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)

        # And so on for more models
        return context  

@login_required(login_url = '/login')   
def confirmacion(request,uidb64,token):
    if uidb64 is not None and token is not None:
        from django.utils.http import urlsafe_base64_decode
        uid = urlsafe_base64_decode(uidb64)
        try:
            from django.contrib.auth import get_user_model
            from django.contrib.auth.tokens import default_token_generator
            user_model = get_user_model()
            user = user_model.objects.get(pk=uid)
            print user
            print user.is_staff
            print token
            if default_token_generator.check_token(user,token) and user.is_staff == 0:
                user.is_staff = True
                user.save()
                print 'es activo'
                print user.is_staff
                return redirect('/bienvenido')
        except:
            return redirect('/ayuda')

def send_simple_message(email,user,uid,token):
    print '------------------------email '+email
    print '------------------------user '+user.username
    print '------------------------uid '+uid
    print '------------------------token '+token
    return requests.post(
        "https://api.mailgun.net/v3/midler.co/messages",
        auth=("api", "key-97ff37f1f573adbe141a60c00625d0b0"),
        data={"from": "Confirmacion midler.co<no-reply@midler.co>",
              "to": "<"+email+">",
              "subject": "Hello "+user.username+"",
              "html": """
              <h3 style="margin:0px">Bienvenido Sr/a: %s </h3><p>Para confirmar su registro en el sitio Midler le solicitamos haga click en el siguiente 
        <a href='http://midler.co/validate/%s/%s/'>enlace de confirmacion</a><br><p><b>Gracias por formar parte de Midler.</b></p>
        <small>Este es un mensaje enviado automaticamente. Por favor no responda a esta direccion de mail.</small>"""%(user, uid,token)

              })

def send_simple_message_forgot_Password(email,uid,token,user):
    return requests.post(
        "https://api.mailgun.net/v3/empleocondesarrollo.com/messages",
        auth=("api", "key-06e964d121fa064ed3a96dddd4e9dbfa"),
        data={"from": "Confirmacion empleocondesarrollo.com<no-reply@empleocondesarrollo.com>",
              "to": "<"+email+">",
              "subject": "Cambiar Password",
              "html": """
              <h3 style="margin:0px">Peticion de cambio de Password %s </h3><p>Para recuperar su password da click en el siguiente enlace 
        <a href='http://empleocondesarrollo.com/email/validate/%s/%s/%s'>enlace de recuperacio
        on de password</a><br><p><b>Gracias por formar parte de Empleocondesarrollo.</b></p>
        <small>Este es un mensaje enviado automaticamente. Por favor no responda a esta direccion de mail.</small>"""%(email, uid,token,user)

              })

class ClienteUpdate(LoginRequired,UpdateView):
    form_class = ClientesForm
    model = Clientes
    success_url = '/clientes'
    def get_context_data(self, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
        # And so on for more models
        return context

class PerfilUpdate(LoginRequired,UpdateView):
    model = Perfil
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super(PerfilUpdate, self).get_context_data(**kwargs)
        if self.request.user:
            context['Perfil'] = Perfil.objects.get(user__username=self.request.user.username)
        # And so on for more models
        return context