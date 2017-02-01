from django.contrib import admin
from webmap.models import Webmap, Webmap_App, Webmap_App_Group, Webmap_Group, Webmap_Item

class Webmap_Admin(admin.ModelAdmin):
	list_display = ('name', 'purpose', 'contact', 'collector', 'collector_offline')
	search_fields = ('name',)

class Webmap_App_Admin(admin.ModelAdmin):
	list_display = ('name', 'purpose', 'url', 'contact', 'webmap')
	search_fields = ('name',)

admin.site.register(Webmap, Webmap_Admin)
admin.site.register(Webmap_App, Webmap_App_Admin)
admin.site.register(Webmap_Item)
admin.site.register(Webmap_Group)
admin.site.register(Webmap_App_Group)