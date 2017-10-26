# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.midlerdamanager import MidlerManager
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Configuracion(models.Model):
    """ """
    tasa_financiamiento = models.CharField('% tasa', max_length=150)
    porcentaje_enganche = models.CharField(max_length=3)
    placo_maximo = models.IntegerField()
    is_active = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    objects = MidlerManager()
    usuario_registro = models.ForeignKey(User)

    class Meta:
        ordering = ["-id"]
    def __unicode__(self):
        return u'%s' % (self.tasa_financiamiento)

class Articulos(models.Model):
    """ """
    descripcion = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=30, decimal_places=2)
    existencia = models.IntegerField()
    is_active = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    objects = MidlerManager()
    usuario_registro = models.ForeignKey(User)
    configuracion = models.ForeignKey(Configuracion)

    class Meta:
        ordering = ["-id"]
    def __unicode__(self):
        return u'%s' % (self.descripcion)