from django.contrib import admin
from userapp.models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
	# fieldsets = [
	# 	(None,               {'fields': ['f_name', 'l_name', 'email']}),
	# 	('Date information', {'fields': ['create_date'], 'classes': ['collapse']}),
	# 	]
	fields = ['f_name', 'l_name', 'email'] 	
	list_display = ('id', 'f_name', 'l_name', 'create_date', 'was_created_recently')
	list_filter = ['create_date']

admin.site.register(UserInfo, UserInfoAdmin)
