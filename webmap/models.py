from __future__ import unicode_literals
from django.db import models
from agol.models import AGOL_Item

#--WEBMAP TABLE
class Webmap(models.Model):
	name = models.CharField(max_length=20)
	purpose = models.CharField(max_length=50)
	contact = models.CharField(max_length=20)
	collector = models.BooleanField()
	collector_offline = models.BooleanField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

#--WEBMAP APP TABLE
class Webmap_App(models.Model):
	name = models.CharField(max_length=20)
	purpose = models.CharField(max_length=50)
	url = models.URLField()
	contact = models.CharField(max_length=20)
	webmap = models.ForeignKey(Webmap)

	class Meta:
		verbose_name = 'Webmap App'

	def __str__(self):
		return self.name

#--AGO_WEBMAP Many2Many
class Webmap_Item(models.Model):
	webmap = models.ManyToManyField(Webmap)
	agol_item = models.ManyToManyField(AGOL_Item)
	map_comments = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Webmap Item'