from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.text import slugify


# Create your models here.tz
def flyer_upload_location(instance, filename):
	return "events/%s/%s" %(instance.id, filename)

class Event(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	host = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="host", default=1)
	flyer = models.ImageField(upload_to=flyer_upload_location,
		blank=True,
		width_field="width_field",
		height_field="height_field")
	youtube_id = models.CharField(max_length=120, blank=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	details = models.TextField()
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("events:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Event.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_event_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_event_receiver, sender=Event)
