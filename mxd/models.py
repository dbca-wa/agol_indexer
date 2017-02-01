from __future__ import unicode_literals
from django.db import models
from layer_source.models import Layer_Source

class MXD(models.Model):
	name = models.CharField(max_length=60)
	path = models.CharField(max_length=255)
	description = models.TextField(max_length=255, blank=True)
	client = models.CharField(max_length=10)
	created_by = models.CharField(max_length=20)
	created_on = models.DateTimeField()
	layer_source = models.ForeignKey(Layer_Source)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'MXD'

	def __str__(self):
		return self.name