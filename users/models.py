from __future__ import unicode_literals
from django.db import models

#--Users - Roles
class Role(models.Model):
	level = models.CharField(max_length=10)
	description = models.TextField(max_length=255)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.level

#--Users - Main
class User(models.Model):
	name = models.CharField(max_length=20)
	comments = models.TextField(max_length=255)
	role = models.ForeignKey(Role)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name