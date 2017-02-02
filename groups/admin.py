from django.contrib import admin
from groups.models import Group

class Group_Admin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ('name',)

admin.site.register(Group, Group_Admin)