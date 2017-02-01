from __future__ import unicode_literals
from django.db import models

#WEB ADAPTER TABLE
class Web_Adapter(models.Model):
	machine_name = models.CharField(max_length=20)
	enviroment = models.CharField(max_length=4)
	alias = models.CharField(max_length=20)
	description = models.TextField(max_length=255)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Web Adapter'

	def __str__(self):
		return self.machine_name