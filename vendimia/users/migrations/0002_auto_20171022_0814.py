# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='is_active',
            field=models.DateTimeField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rfc',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
