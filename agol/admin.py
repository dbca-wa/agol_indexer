from django.contrib import admin
from agol.models import AGOL_Item_Type, AGOL_Group, AGOL_Item

class AGOL_Item_Admin(admin.ModelAdmin):
	list_display = ('name', 'url', 'type', 'creator', 'owner')
	search_fields = ('name',)

admin.site.register(AGOL_Item, AGOL_Item_Admin)
admin.site.register(AGOL_Item_Type)
admin.site.register(AGOL_Group)