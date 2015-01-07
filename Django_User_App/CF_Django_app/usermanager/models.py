from django.db import models


class UserManager(models.Model):
		firstName = models.CharField(max_length=200, blank=False)
		lastName = models.CharField(max_length=200, blank = True)
		email = models.EmailField()
		def __unicode__(self):
			return self.firstName
			return self.lastName
