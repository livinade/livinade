from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Event

# Create your views here.

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
