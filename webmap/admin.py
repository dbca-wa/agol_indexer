from django.contrib import admin
from webmap.forms import Webmap_AdminForm, Webmap_App_AdminForm
from webmap.models import Webmap, Webmap_App,  Webmap_Contact


class Webmap_Admin(admin.ModelAdmin):
    list_display = ('name', 'purpose', 'url', 'contact', 'collector', 'collector_offline')
    search_fields = ('name',)
    form = Webmap_AdminForm


class Webmap_App_Admin(admin.ModelAdmin):
    list_display = ('name', 'purpose', 'url', 'contact', 'webmap')
    search_fields = ('name',)
    form = Webmap_App_AdminForm


admin.site.register(Webmap, Webmap_Admin)
admin.site.register(Webmap_App, Webmap_App_Admin)
admin.site.register(Webmap_Contact)
