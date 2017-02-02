from django.contrib import admin
from webmap.models import Webmap, Webmap_App, Webmap_Item, Webmap_Contact

class Webmap_Admin(admin.ModelAdmin):
	list_display = ('name', 'purpose', 'contact', 'collector', 'collector_offline')
	search_fields = ('name',)

class Webmap_App_Admin(admin.ModelAdmin):
	list_display = ('name', 'purpose', 'url', 'contact', 'webmap')
	search_fields = ('name',)

class Webmap_Item_Admin(admin.ModelAdmin):
	list_display = ('name', 'map_description')
	search_fields = ('name',)

admin.site.register(Webmap, Webmap_Admin)
admin.site.register(Webmap_App, Webmap_App_Admin)
admin.site.register(Webmap_Item, Webmap_Item_Admin)
admin.site.register(Webmap_Contact)