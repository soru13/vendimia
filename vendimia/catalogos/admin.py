# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db.models import Model as Modelo
import models, inspect
# Register your models here.
for x in dir(models):
	item = getattr(models, x)
	if inspect.isclass(item) and issubclass(item, Modelo) and x != 'User' and not admin.site.is_registered(item):
		admin.site.register(item)