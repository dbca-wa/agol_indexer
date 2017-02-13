from __future__ import unicode_literals
from django.db import models
from layer_source.models import Layer_Source

class MXD_Client(models.Model):
	client = models.CharField(max_length=120)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'MXD Client'

	def __str__(self):
		return self.client

class MXD_Creator(models.Model):
	creator = models.CharField(max_length=120)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'MXD Creator'

	def __str__(self):
		return self.creator

class MXD(models.Model):
	name = models.CharField(max_length=60)
	path = models.CharField(max_length=500)
	description = models.TextField(max_length=255, blank=True)
	client = models.ForeignKey(MXD_Client)
	created_by = models.ForeignKey(MXD_Creator)
	created_on = models.DateTimeField()
	layer_source = models.ForeignKey(Layer_Source)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'MXD'

	def __str__(self):
		return "%s - %s" % (self.name, self.created_by)