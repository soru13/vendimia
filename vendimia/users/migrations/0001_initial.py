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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=13)),
                ('apellido_paterno', models.CharField(max_length=13)),
                ('apellido_materno', models.CharField(max_length=13)),
                ('rfc', models.CharField(blank=True, max_length=13)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.DateTimeField(blank=True, null=True)),
                ('origin', models.IntegerField(blank=True, null=True)),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Clientes',
                'verbose_name_plural': 'Clientes',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='AvatarUser')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.DateTimeField(blank=True, null=True)),
                ('origin', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
    ]
