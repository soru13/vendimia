# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AuditLocal(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    id_obj = models.IntegerField(db_index=True)
    accion = models.CharField(max_length=1, db_index=True)
    fecha = models.DateTimeField(db_index=True)
    changed_fields = models.TextField(null=True)
    junta = models.IntegerField(db_index=True)
    class Meta:
        ordering = ['id']
    def __unicode__(self):
        return 'Audit'