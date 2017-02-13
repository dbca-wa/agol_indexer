from __future__ import unicode_literals
from django.db import models
from agol_users.models import AGOL_User
from web_service.models import Web_Service
from mxd.models import MXD

#--ARCGIS ONLINE Item - Type
class AGOL_Item_Type(models.Model):
    type = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ArcGIS Online Item Type'

    def __str__(self):
        return self.type

#--ARCGIS ONLINE TABLE - Main
class AGOL_Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(AGOL_Item_Type)
    url = models.ForeignKey(Web_Service, verbose_name='External url')
    mxd = models.ForeignKey(MXD, verbose_name='External MXD')
    external_layer_url = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(AGOL_User)
    comments = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ArcGIS Online Item'

    def __str__(self):
        return self.name