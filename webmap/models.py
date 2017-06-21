from __future__ import unicode_literals
from django.db import models
from agol.models import AGOL_Item

class Webmap_Contact(models.Model):
	contact_name = models.CharField(max_length=120)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Webmap Contact'
		ordering = ['contact_name']

	def __str__(self):
		return self.contact_name

#--WEBMAP TABLE
class Webmap(models.Model):
	name = models.CharField(max_length=60)
	purpose = models.CharField(max_length=255)
	url = models.URLField(help_text="URL of the web map")
	contact = models.ForeignKey(Webmap_Contact)
	collector = models.BooleanField()
	collector_offline = models.BooleanField()
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

#--WEBMAP APP TABLE
class Webmap_App(models.Model):
	name = models.CharField(max_length=60)
	purpose = models.CharField(max_length=255)
	url = models.URLField(help_text="URL of the web mapping application")
	contact = models.ForeignKey(Webmap_Contact)
	webmap = models.ForeignKey(Webmap)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Webmap App'
		ordering = ['name']

	def __str__(self):
		return self.name

#Manager
class Webmap_Item_Manager(models.Manager):
	def create_webmap_item(self, name, description):
		webmap_item = self.create(name=name, description=description)
		return webmap_item

#--AGO_WEBMAP Many2Many
class Webmap_Item(models.Model):
	name = models.CharField(max_length=120, blank=True)
	webmap = models.ManyToManyField(Webmap)
	agol = models.ManyToManyField(AGOL_Item)
	description = models.TextField(blank=True, verbose_name='Map description')
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	objects = Webmap_Item_Manager()

	class Meta:
		verbose_name = 'Webmap Item'
		ordering = ['name']

	def __str__(self):
		return self.name
