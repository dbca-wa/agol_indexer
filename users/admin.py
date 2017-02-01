from django.contrib import admin
from users.models import Role, User

class User_Admin(admin.ModelAdmin):
	list_display = ('name', 'role')
	search_fields = ('name',)

admin.site.register(Role)
admin.site.register(User, User_Admin)