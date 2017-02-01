from __future__ import unicode_literals
from django.db import models

#ARCGIS ONLINE Item - Type
class AGOL_Item_Type(models.Model):
    type = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#ARCGIS ONLINE Item - Owner
class AGOL_Item_Owner(models.Model):
    owner = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#--ARCGIS ONLINE TABLE - Main
class AGOL_Item(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    type = models.ForeignKey(AGOL_Item_Type)
    creator = models.CharField(max_length=20)
    owner = models.ForeignKey(AGOL_Item_Owner)
    comments = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)