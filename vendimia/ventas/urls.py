from django.conf.urls import url
from .views import (
    VentasList,AutoCompleteView,AutoCompleteArticulosView,VentasNew,VentasDelete,VentasCreation
)

urlpatterns = [

    url(r'^$', VentasList.as_view(), name='list'),
    url(r'^new$', VentasNew, name='new'),
    url(r'^autocomplete/$',AutoCompleteView.as_view(), name='autocomplete'),
    url(r'^autocompletearticulo/$',AutoCompleteArticulosView.as_view(), name='autocompleteArticulos'),
    url(r'^nuevo$', VentasCreation.as_view(), name='nuevo'),
    url(r'^borrar/(?P<pk>\d+)$', VentasDelete.as_view(), name='delete'),


    # // La empresa del perfil 
    # url(r'^agregar/$', agregar_empresa_perfil_user, name ='agregar_empresa' ),
    # url(r'^(editar|eliminar)/([0-9]+)/?([0-9]+)$', agregar_empresa_perfil_user,name ='editar_empresa'),
]