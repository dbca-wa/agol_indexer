from __future__ import unicode_literals
from django.db import models
from users.models import User

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
    name = models.CharField(max_length=30)
    url = models.URLField()
    type = models.ForeignKey(AGOL_Item_Type)
    creator = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    comments = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ArcGIS Online Item'

    def __str__(self):
        return self.name