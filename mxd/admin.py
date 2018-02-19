from django.contrib import admin
from mxd.forms import MXD_AdminForm
from mxd.models import MXD, MXD_Client, MXD_Creator


class MXD_Admin(admin.ModelAdmin):
    list_display = ('name', 'path', 'client', 'created_by', 'created_on')
    search_fields = ('name',)
    form = MXD_AdminForm
    filter_horizontal = (
        'layer_source',
    )


admin.site.register(MXD, MXD_Admin)
admin.site.register(MXD_Client)
admin.site.register(MXD_Creator)
