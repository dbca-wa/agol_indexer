from __future__ import unicode_literals
from django.db import models
from users import models as u
from groups import models as g

#--ARCGIS ONLINE Item - Type
class AGOL_Item_Type(models.Model):
    type = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

#--ARCGIS ONLINE TABLE - Main
class AGOL_Item(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    type = models.ForeignKey(AGOL_Item_Type)
    creator = models.CharField(max_length=20)
    owner = models.ForeignKey(u.User)
    comments = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AGOL_Group(models.Model):
    agol_item = models.ManyToManyField(AGOL_Item)
    group = models.ManyToManyField(g.Group)
    comments = models.TextField(blank=True)