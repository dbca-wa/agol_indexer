from __future__ import unicode_literals
from django.db import models

class Layer_Source(models.Model):
	name = models.CharField(max_length=20)
	location = models.CharField(max_length=50)
	#format = models.ForeignKey(#) FK TODO
	#feature_type = models.ForeignKey(#) FK TODO
	created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)