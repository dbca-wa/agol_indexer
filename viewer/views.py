from django.shortcuts import render
from django.http import HttpResponse, Http404

def viewer_home(request):
	return render(request, 'viewer_index.html')

def viewer_agol(request):
	return render(request, 'viewer_agol-item.html')

def viewer_groups(request):
	return render(request, 'viewer_groups.html')

def viewer_layer_source(request):
	return render(request, 'viewer_layer-source.html')

def viewer_mxd(request):
	return render(request, 'viewer_mxd.html')

def viewer_web_adapter(request):
	return render(request, 'viewer_web-adapter.html')

def viewer_web_service(request):
	return render(request, 'viewer_web-service.html')

def viewer_webmap(request):
	return render(request, 'viewer_webmap.html')

def viewer_webmap_app(request):
	return render(request, 'viewer_webmap-app.html')