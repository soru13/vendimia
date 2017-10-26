# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from save_the_change.mixins import SaveTheChange
from django.db import models
from users.midlerdamanager import MidlerManager,BorradoLogico
from articulos.models import Articulos
from users.models import Clientes
from django.contrib.auth.models import User

# Create your models here.



class Ventas(SaveTheChange, models.Model):
    articulo = models.ManyToManyField(Articulos)
    cliente = models.ForeignKey(Clientes)
    plazo = models.CharField(max_length=13, blank=False, null=False)
    abono = models.CharField(max_length=13, blank=False, null=False)
    ahorro = models.CharField(max_length=13, blank=False, null=False)
    total_a_pagar = models.CharField(max_length=13, blank=False, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    is_active = models.DateTimeField(blank=True, null=True)
    origin = models.IntegerField(blank=True, null=True)
    objects = MidlerManager()
    usuario_registro = models.ForeignKey(User)
    
    def delete(self):
        BorradoLogico(self)
    class Meta:
        verbose_name = 'Ventas'
        verbose_name_plural = 'Ventas'
    def __unicode__(self):
        return '%s' % (self.cliente.nombre)