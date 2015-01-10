import datetime

from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
	f_name = models.CharField('First Name', max_length=100)
	l_name = models.CharField('Last Name', max_length=200)
	email = models.EmailField('Email')
	create_date = models.DateTimeField('Date Created')
	def __unicode__(self):
		return "%s, %s" % (self.f_name, self.l_name)


	def was_created_recently(self):
		return self.create_date >= timezone.now() - datetime.timedelta(days=1)
		was_created_recently.admin_order_field = 'create_date'
    	was_created_recently.boolean = True
    	was_created_recently.short_description = 'Created Recently?'

