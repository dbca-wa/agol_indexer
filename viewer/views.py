from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core import serializers
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
	layer_source_all = Layer_Source.objects.all()
	layer_source = None

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			layer_source = layer_source_all
		else:
			layer_source = Layer_Source.objects.filter(name__icontains=name)
	else:
		layer_source = layer_source_all
	print layer_source
	search_data = serializers.serialize("json", layer_source_all)
	return render(request, 'viewer_list.html', {'location': location, 'items': layer_source, 'search_data': search_data})

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