from django.db import models
from django.utils import timezone
from cacheops import invalidate_obj, invalidate_model
class MidlerQuerySet(models.query.QuerySet):
	def delete(self):
		self.update(is_active=timezone.now())
	def active(self):
		return self.filter(is_active=None)
	def desactive(self):
		return self.exclude(is_active=None)

class MidlerManager(models.Manager):
	def get_query_set(self):
		return MidlerQuerySet(self.model, using=self._db)
	def get_queryset(self):
		return self.get_query_set().active()
	def all(self):
		return self.get_queryset().active()
	def alls(self):
		return self.get_query_set()

def BorradoLogico(self):
	#to_delete, access = get_related_objects(self)
	#for i in range(0, len(access)):
	#	for obj in to_delete[i]:
	#		obj.delete()invalidate_obj
	self.is_active = timezone.now()
	super(type(self), self).save((), {})
	# invalidate_obj(self)