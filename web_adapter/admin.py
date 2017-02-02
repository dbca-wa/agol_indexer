from django.contrib import admin
from web_adapter.models import Web_Adapter

class Web_Adapter_Admin(admin.ModelAdmin):
    list_display = ('machine_name', 'enviroment', 'alias', 'description')
    search_fields = ('machine_name',)

admin.site.register(Web_Adapter, Web_Adapter_Admin)