from django.contrib import admin
from usermanager.models import UserManager 


class UserAdmin(admin.ModelAdmin):
	list_display = ('firstName', 'lastName', 'email')
	fields = ['firstName', 'lastName', 'email']


admin.site.register(UserManager, UserAdmin)