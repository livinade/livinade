from django.contrib import admin
# Register your models here.
from .forms import NLSignUpForm
from .models import NLSignUp

class NLSignUpAdmin(admin.ModelAdmin):
	list_display = ("__unicode__","timestamp", "updated")
	form = NLSignUpForm

admin.site.register(NLSignUp, NLSignUpAdmin)