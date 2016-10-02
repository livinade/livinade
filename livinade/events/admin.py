from django.contrib import admin
from .models import Event
# Register your models here.

class EventModelAdmin(admin.ModelAdmin):
	list_display = ("title", "updated", "timestamp")
	list_display_links = ["updated"]
	list_filter = ("updated", "timestamp")
	search_fields = ("title", "details")
	prepopulated_fields = {'slug':("title",)}

	class Meta:
		model = Event

admin.site.register(Event, EventModelAdmin)