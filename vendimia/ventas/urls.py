from django.conf.urls import url
from .views import (
    VentasList,AutoCompleteView,AutoCompleteArticulosView,VentasNew,VentasDelete,VentasCreation,VentasEdit
)

urlpatterns = [

    url(r'^$', VentasList.as_view(), name='list'),
    url(r'^new$', VentasNew, name='new'),
    url(r'^autocomplete/$',AutoCompleteView.as_view(), name='autocomplete'),
    url(r'^autocompletearticulo/$',AutoCompleteArticulosView.as_view(), name='autocompleteArticulos'),
    url(r'^nuevo$', VentasCreation.as_view(), name='nuevo'),
    url(r'^borrar/(?P<pk>\d+)$', VentasDelete.as_view(), name='delete'),
    url(r'^editar/(?P<pk>\d+)$', VentasEdit, name='edit'),



]