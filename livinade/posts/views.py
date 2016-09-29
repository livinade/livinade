from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_list(request):
	queryset_list = Post.objects.all() #.order_by("-timestamp")
	paginator = Paginator(queryset_list, 6) # Show 25 contacts per page
	
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page) 
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		'object_list': queryset,
		'title': 'Blog',
	}

	return render(request,'blog/post_list.html', context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	context = {
		'obj': instance,
		'title': instance.title,
	}

	return render(request,'blog/post_detail.html', context)