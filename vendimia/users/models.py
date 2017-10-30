# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from save_the_change.mixins import SaveTheChange
from django.contrib.auth.models import User
from users.midlerdamanager import MidlerManager,BorradoLogico
from django.db import models


class Perfil(SaveTheChange, models.Model):
    user = models.OneToOneField(User) # Solo tener 1 perfil
    avatar = models.ImageField(upload_to='AvatarUser', blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    is_active = models.DateTimeField(blank=True, null=True)
    origin = models.IntegerField(blank=True, null=True)
    objects = MidlerManager()
    
    def delete(self):
        BorradoLogico(self)
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    def __unicode__(self):
        return '%s' % (self.user)

class Clientes(SaveTheChange, models.Model):
    nombre = models.CharField(max_length=13, blank=False, null=False)
    apellido_paterno = models.CharField(max_length=13, blank=False, null=False)
    apellido_materno = models.CharField(max_length=13, blank=False, null=False)
    rfc = models.CharField(max_length=13, blank=True, null=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    is_active = models.DateTimeField(blank=True, null=True)
    origin = models.IntegerField(blank=True, null=True)
    objects = MidlerManager()
    usuario_registro = models.ForeignKey(User)
    def delete(self):
        BorradoLogico(self)
    class Meta:
        ordering = ["-id"]
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
    def __unicode__(self):
        return '%s' % (self.nombre)