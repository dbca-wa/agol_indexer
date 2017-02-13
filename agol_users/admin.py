from django.contrib import admin
from agol_users.models import Role, AGOL_User

class AGOL_User_Admin(admin.ModelAdmin):
	list_display = ('name', 'role')
	search_fields = ('name',)

admin.site.register(Role)
admin.site.register(AGOL_User, AGOL_User_Admin)