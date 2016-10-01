from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

# Create your views here.

def user_profiles(request, username=None):
	instance = get_object_or_404(User, username=username)
	context = {
		'obj': instance,
		'title': instance.username,
	}

	return render(request,'account/user_profiles.html', context)

def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect("/account/")
	else:

		if request.method == 'POST':
			user_form = UserRegistrationForm(request.POST)

			if user_form.is_valid():
				# Create a new user object but avoid saving it yet
				new_user = user_form.save(commit=False)
				# Set the chosen password
				new_user.set_password(user_form.cleaned_data['password'])
				# Save the User object
				new_user.save()
				# Create the user Profile
				profile = Profile.objects.create(user=new_user)
				user = authenticate(username=user_form.cleaned_data['username'], 
									password=user_form.cleaned_data['password'])
				if user is not None:
					if user.is_active:
						login(request, user)
				return HttpResponseRedirect("/account/edit/")

		else:
			user_form = UserRegistrationForm()

	context = {'user_form': user_form}
	return render(request, 'account/register.html', context)

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, "Profile updated successfully")
		else:
			messages.error(request, "Error updating your profile")
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	context = { 
		'user_form': user_form,
		'profile_form': profile_form
	}
	return render(request, 'account/edit.html', context)

@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})

