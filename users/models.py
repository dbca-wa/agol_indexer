from __future__ import unicode_literals
from django.db import models

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