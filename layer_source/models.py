from __future__ import unicode_literals
from django.db import models

class Layer_Source_Format(models.Model):
	formats = models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Layer Source Format'

	def __str__(self):
		return self.formats

class Layer_Source_Format_Type(models.Model):
	format_type = models.CharField(max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Layer Source Format Type'

	def __str__(self):
		return self.format_type

class Layer_Source(models.Model):
	name = models.CharField(max_length=30)
	location = models.CharField(max_length=50, verbose_name='Location or Database')
	formats = models.ForeignKey(Layer_Source_Format, verbose_name='format')
	feature_type = models.ForeignKey(Layer_Source_Format_Type)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Layer Source'

	def __str__(self):
		return self.name