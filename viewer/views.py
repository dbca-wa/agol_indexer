from django.shortcuts import render
from django.http import HttpResponse, Http404
from layer_source.models import Layer_Source

def viewer_home(request):
	return render(request, 'viewer_index.html')

def viewer_agol(request):
	location = ['ArcGIS Online Item']
	return render(request, 'viewer_list.html', {'location': location})

def viewer_groups(request):
	location = ['Groups']
	return render(request, 'viewer_list.html', {'location': location})

def viewer_layer_source(request):
	location = ['Layer Source']
	layer_source = Layer_Source.objects.all()
	return render(request, 'viewer_list.html', {'location': location, 'items': layer_source})

def viewer_mxd(request):
	location = ['MXD']
	return render(request, 'viewer_list.html', {'location': location})

def viewer_web_adapter(request):
	location = ['Web Adapter']
	return render(request, 'viewer_list.html', {'location': location})

def viewer_web_service(request):
	location = ['Web Service']
	return render(request, 'viewer_list.html', {'location': location})

def viewer_webmap(request):
	location = ['Webmap']
	return render(request, 'viewer_list.html', {'location': location})

def viewer_webmap_app(request):
	location = ['Webmap App']
	return render(request, 'viewer_list.html', {'location': location})