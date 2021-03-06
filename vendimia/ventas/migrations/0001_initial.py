# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 07:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plazo', models.CharField(max_length=13)),
                ('abono', models.CharField(max_length=13)),
                ('ahorro', models.CharField(max_length=13)),
                ('cantidad', models.CharField(max_length=133)),
                ('total_a_pagar', models.CharField(max_length=13)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.DateTimeField(blank=True, null=True)),
                ('origin', models.IntegerField(blank=True, null=True)),
                ('articulo', models.ManyToManyField(to='articulos.Articulos')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Clientes')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Ventas',
                'verbose_name_plural': 'Ventas',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
    ]
