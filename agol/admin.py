from django.contrib import admin
from agol.models import AGOL_Item_Type, AGOL_Group, AGOL_Item

admin.site.register(AGOL_Item)
admin.site.register(AGOL_Item_Type)
admin.site.register(AGOL_Group)
