from django.contrib import admin
from webmap.models import Webmap, Webmap_App, Webmap_App_Group, Webmap_Group, Webmap_Item

admin.site.register(Webmap)
admin.site.register(Webmap_App)
admin.site.register(Webmap_Item)
admin.site.register(Webmap_Group)
admin.site.register(Webmap_App_Group)