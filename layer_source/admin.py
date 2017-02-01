from django.contrib import admin
from layer_source.models import Layer_Source_Format, Layer_Source_Format_Type, Layer_Source

admin.site.register(Layer_Source)
admin.site.register(Layer_Source_Format)
admin.site.register(Layer_Source_Format_Type)