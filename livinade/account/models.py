from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.
def avatar_upload_location(instance, filename):
	return "users/%s/avatar/%s" %(instance.user.username, filename)

def header_upload_location(instance, filename):
	return "users/%s/header/%s" %(instance.user.username, filename)

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	avatar = models.ImageField(upload_to=avatar_upload_location, blank=True)
	header_image = models.ImageField(upload_to=header_upload_location, blank=True)

	def __unicode__(self):
		return 'Profile for user {}'.format(self.user.username)