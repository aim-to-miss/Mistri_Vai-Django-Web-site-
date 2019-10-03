from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from viewstat.models import homestat, comments, mistri




def home(request):
	qs = homestat.objects.all()
	obj2 = comments.objects.all()
	if qs.count()!=1:
		raise Http404
	else:
		obj = qs.first()
	context = {"object": obj,
				"object_list":obj2
	}
	return render(request,"index.html",context)

def about(request):
	return render(request,"about.html")

def mistril(request):
	qs = mistri.objects.all()
	if qs.count() < 1:
		raise Http404
	else:
		context = {"mistriList":qs}
	return render(request,"mistri.html",context)