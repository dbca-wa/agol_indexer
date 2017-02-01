from __future__ import unicode_literals
from django.db import models

#--GROUPS TABLE
class Groups(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(max_length=255)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)