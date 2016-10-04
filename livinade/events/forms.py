from django import forms
from .models import Event

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [
			"title",
			"flyer",
			"youtube_id",
			"details"
		]