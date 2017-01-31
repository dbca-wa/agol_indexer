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

#--WEBMAP TABLE
class Webmap(models.Model):
    name = models.CharField(max_length=20)
    purpose = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    collector = models.BooleanField()
    collector_offline = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#--GROUPS TABLE
class Groups(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#--WEB SERVICE TABLE
class Web_Service(models.Model):
    #name = models.CharField() FK? MXD
    #machine_name = models.CharField() FK? WEB_ADAPTER
    location = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    actual_url = models.URLField()
    alias_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Web_Adapter(models.Model):
    machine_name = models.CharField(max_length=20)
    enviroment = models.CharField(max_length=4)
    alias = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#--USERS TABLE
#--Users - Roles
class Users_Roles(models.Model):
    level = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
#--Users - Main
class Users(models.Model):
    name = models.CharField(max_length=20)
    comments = models.CharField(max_length=255)
    role = models.ForeignKey(Users_Roles)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

