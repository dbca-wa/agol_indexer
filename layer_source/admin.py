from django.contrib import admin
from layer_source.models import Layer_Source_Format, Layer_Source_Format_Type, Layer_Source

class Layer_Source_Admin(admin.ModelAdmin):
	list_display = ('name', 'location', 'formats', 'owner', 'feature_type')
	search_fields = ('name',)

admin.site.register(Layer_Source, Layer_Source_Admin)
admin.site.register(Layer_Source_Format)
admin.site.register(Layer_Source_Format_Type)