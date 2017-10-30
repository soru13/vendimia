# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100)),
                ('id_obj', models.IntegerField(db_index=True)),
                ('accion', models.CharField(db_index=True, max_length=1)),
                ('fecha', models.DateTimeField(db_index=True)),
                ('changed_fields', models.TextField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'audit_local',
                'managed': False,
            },
        ),
    ]
