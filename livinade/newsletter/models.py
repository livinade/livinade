from __future__ import unicode_literals
from django.db import models

# Create your models here.

class NLSignUp(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length=120,blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.email
from django.db import models

# Create your models here.
