from __future__ import unicode_literals
from django.db import models
from web_adapter import models as wa
from mxd import models as m

#--WEB SERVICE TABLE
class Web_Service(models.Model):
	location = models.CharField(max_length=50)
	level = models.CharField(max_length=50)
	actual_url = models.URLField()
	alias_url = models.URLField()
	mxd_id = models.ForeignKey(m.MXD)
	web_adapter_id = models.ForeignKey(wa.Web_Adapter)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.alias_url