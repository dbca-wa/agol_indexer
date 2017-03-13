from django.contrib import admin
from groups.forms import Group_AdminForm
from groups.models import Group

class Group_Admin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ('name',)
	form = Group_AdminForm

admin.site.register(Group, Group_Admin)