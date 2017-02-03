from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core import serializers
from agol.models import AGOL_Item
from groups.models import Group
from layer_source.models import Layer_Source
from mxd.models import MXD
from users.models import User
from web_adapter.models import Web_Adapter
from web_service.models import Web_Service
from webmap.models import Webmap, Webmap_App

def viewer_home(request):
	return render(request, 'viewer_index.html')

def viewer_agol(request):
	location = ['ArcGIS Online Item']
	agol_all = AGOL_Item.objects.all()
	agol = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			agol = agol_all
		else:
			agol = AGOL_Item.objects.filter(name__icontains=name)
			search_field = name
	else:
		agol = agol_all
	
	location.append(agol.count)
	search_data = AGOL_Item.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': agol,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_groups(request):
	location = ['Groups']
	groups_all = Group.objects.all()
	groups = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			groups = groups_all
		else:
			groups = Group.objects.filter(name__icontains=name)
			search_field = name
	else:
		groups = groups_all
	
	location.append(groups.count)
	search_data = Group.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': groups,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_layer_source(request):
	location = ['Layer Source']
	layer_source_all = Layer_Source.objects.all()
	layer_source = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			layer_source = layer_source_all
		else:
			layer_source = Layer_Source.objects.filter(name__icontains=name)
			search_field = name
	else:
		layer_source = layer_source_all
	
	location.append(layer_source.count)
	search_data = Layer_Source.objects.all().values_list('name', flat=True).distinct()
	print 'search_data %s' % search_data
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': layer_source,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_mxd(request):
	location = ['MXD']
	mxd_all = MXD.objects.all()
	mxd = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			mxd = mxd_all
		else:
			mxd = MXD.objects.filter(name__icontains=name)
			search_field = name
	else:
		mxd = mxd_all

	location.append(mxd.count)
	search_data = MXD.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': mxd,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_web_adapter(request):
	location = ['Web Adapter']
	web_adapter_all = Web_Adapter.objects.all()
	web_adapter = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			web_adapter = web_adapter_all
		else:
			web_adapter = Web_Adapter.objects.filter(machine_name__icontains=name)
			search_field = name
	else:
		web_adapter = web_adapter_all

	location.append(web_adapter.count)
	search_data = Web_Adapter.objects.all().values_list('machine_name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': web_adapter,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_web_service(request):
	location = ['Web Service']
	web_service_all = Web_Service.objects.all()
	web_service = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			web_service = web_service_all
		else:
			web_service = Web_Service.objects.filter(name__icontains=name)
			search_field = name
	else:
		web_service = web_service_all

	location.append(web_service.count)
	search_data = Web_Service.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': web_service,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_webmap(request):
	location = ['Webmap']
	webmap_all = Webmap.objects.all()
	webmap = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			webmap = webmap_all
		else:
			webmap = Webmap.objects.filter(name__icontains=name)
			search_field = name
	else:
		webmap = webmap_all

	location.append(webmap.count)
	search_data = Webmap.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': webmap,
		'search_data': search_data,
		'search_field': search_field,
	})

def viewer_webmap_app(request):
	location = ['Webmap App']
	webmap_app_all = Webmap_App.objects.all()
	webmap_app = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			webmap = webmap_app_all
		else:
			webmap_app = Webmap_App.objects.filter(name__icontains=name)
			search_field = name
	else:
		webmap_app = webmap_app_all

	location.append(webmap_app.count)
	search_data = Webmap_App.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': webmap_app,
		'search_data': search_data,
		'search_field': search_field,
	})