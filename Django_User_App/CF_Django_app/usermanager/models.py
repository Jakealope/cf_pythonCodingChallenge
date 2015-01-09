from django.db import models

class UserManager(models.Model):

    class Meta:
        verbose_name_plural = "User Details"

    firstname = models.CharField('First Name', max_length=100)
    lastname = models.CharField('Last Name', max_length=100, blank=True)
    email = models.EmailField('Email')
    

    def __unicode__(self):
        return self.firstname
        return self.lastname
        return self.email