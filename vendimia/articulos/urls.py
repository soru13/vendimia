from django.conf.urls import url

from .views import (
    ArticulosList,
    configuracion,
    ArticulosCreation,
    ArticuloDelete,
    ArticuloUpdate,
#     EmpresaCreation,
#     EmpresaUpdate,
#     EmpresaDelete,
#     agregar_empresa_perfil_user
)

urlpatterns = [

    url(r'^$', ArticulosList.as_view(), name='list'),
    url(r'^configuracion$', configuracion, name='configuracion'),    
    url(r'^nuevo$', ArticulosCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ArticuloUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ArticuloDelete.as_view(), name='delete'),
]