from django.contrib import admin
from web_service.models import Web_Service

class Web_Service_Admin(admin.ModelAdmin):
	list_display = ('location', 'level', 'actual_url', 'alias_url', 'mxd', 'web_adapter')
	search_fields = ('name',)

admin.site.register(Web_Service, Web_Service_Admin)