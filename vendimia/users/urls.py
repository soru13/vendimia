from django.conf.urls import url
from . import views
from .views import Bienvenido,PerfilUpdate,Home,ClienteList,PerfilDelete,ClienteUpdate,ClienteDelete
urlpatterns = [
	url(r'^nuevo', views.NuevoUsuario, name='new'),

	url(r'^$', Home.as_view(), name='home'),
	url(r'^editar/(?P<pk>\d+)$', PerfilUpdate.as_view(), name='perfil'),

	url(r'^edit/(?P<pk>\d+)$', ClienteUpdate.as_view(), name='edit'),
	url(r'^borrar/(?P<pk>\d+)$', PerfilDelete.as_view(), name='delete'),
	url(r'^delete/(?P<pk>\d+)$', ClienteDelete.as_view(), name='deletCliente'),


	url(r'^bienvenido/$', Bienvenido.as_view(), name='bienvenido'),
	url(r'^clientes$', ClienteList.as_view(), name='list'),
	url(r'^validate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.confirmacion, name='user-activation-link'),
]