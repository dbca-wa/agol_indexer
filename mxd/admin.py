from django.contrib import admin
from mxd.models import MXD, MXD_Client, MXD_Creator

class MXD_Admin(admin.ModelAdmin):
	list_display = ('name', 'path', 'client', 'created_by', 'created_on', 'layer_source')
	search_fields = ('name',)

admin.site.register(MXD, MXD_Admin)
admin.site.register(MXD_Client)
admin.site.register(MXD_Creator)
