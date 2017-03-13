from __future__ import unicode_literals
from django.db import models
from web_adapter.models import Web_Adapter
from mxd.models import MXD

class Web_Service_Level(models.Model):
	level = models.CharField(max_length=50)
	created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

	class Meta:
		verbose_name = 'Web Service Level'
		ordering = ['level']

	def __str__(self):
		return self.level

#--WEB SERVICE TABLE
class Web_Service(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	actual_url = models.CharField(max_length=150, help_text="Full URL of layer / web service that includes the actual machine name and port of host machine that ArcGIS Server (which creates/contains the web services) resides.  Note that if only one layer is defined in the web service then put the full URL including the index number of that layer.  Else, include no index numbers Eg. https://kens-arcgis-001-prod:6443/arcgis/rest/services/PVS/Long_Trails_Structures_WSE/MapServer/0")
	alias_url = models.URLField(help_text="Full URL of layer / web service that includes the alias to the actual machine name of host machine that ArcGIS Server (which creates/contains the web services) resides.  Note that if only one layer is defined in the web service then put the full URL including the index number of that layer.  Else, include no index numbers Eg. https://arcgis.dpaw.wa.gov.au/arcgis/rest/services/PVS/Long_Trails_Structures_WSE/MapServer/0")
	level = models.ForeignKey(Web_Service_Level)
	mxd = models.ForeignKey(MXD)
	web_adapter = models.ForeignKey(Web_Adapter)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Web Service'
		ordering = ['name']

	def __str__(self):
		return self.alias_url