from django.contrib import admin
from agol.forms import AGOL_AdminForm
from agol.models import AGOL_Item_Type, AGOL_Item

class AGOL_Item_Admin(admin.ModelAdmin):
	list_display = ('name', 'url', 'type', 'mxd', 'owner')
	search_fields = ('name',)
	form = AGOL_AdminForm

admin.site.register(AGOL_Item, AGOL_Item_Admin)
admin.site.register(AGOL_Item_Type)