# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditlocal',
            name='junta',
        ),
    ]