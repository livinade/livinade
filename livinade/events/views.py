from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import EventForm
from .models import Event
from django.contrib import messages


# Create your views here.
@login_required
def event_create(request):
	form = EventForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.host = request.user
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"event_form": form,
	}
	return render(request, "events/event_form.html",context)

def event_list(request):
	queryset_list = Event.objects.all()
	paginator = Paginator(queryset_list, 25)

	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		'events' : queryset,
		'Title' : 'events'
	}

	return render(request, 'events/event_list.html', context)

def event_detail(request, slug=None):
	instance = get_object_or_404(Event, slug=slug)
	context = {
		'event': instance,
		'title': instance.title,
	}

	return render(request,'events/event_detail.html', context)
@login_required
def event_update(request, slug=None):
	instance = get_object_or_404(Event, slug=slug)
	if request.user != instance.host:
		raise Http404

	form = EventForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Saved")
		return HttpResponseRedirect(instance.get_absolute_url)

	context = {
		"title": instance.title,
		"instance": instance,
		"event_form": form,
	}
	return render(request, "events/event_form.html", context)

@login_required
def event_delete(request, slug=None):
	instance = get_object_or_404(Event, slug=slug)
	if request.user != instance.host:
		raise Http404

	instance.delete()
	messages.success(request,"Successfully Deleted")
	return redirect("events:list")