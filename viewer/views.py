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
from webmap.models import Webmap, Webmap_App, Webmap_Item

def viewer_home(request):
	return render(request, 'viewer_index.html')

def viewer_agol(request):
	location = ['ArcGIS Online Item']
	agol_all = AGOL_Item.objects.all()
	agol = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			agol = agol_all
		else:
			agol = AGOL_Item.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			agol = agol_all
		else:
			agol = AGOL_Item.objects.filter(name__icontains=name)
			showing_all = False
			search_field = name
	else:
		agol = agol_all
	
	location.append(agol.count)
	search_data = AGOL_Item.objects.all().values_list('name', flat=True).distinct()
	group_links = Group.objects.all()
	webmap_item_links = Webmap_Item.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': agol,
		'group_links': group_links,
		'webmap_item_links': webmap_item_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_groups(request):
	location = ['Group']
	groups_all = Group.objects.all()
	groups = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			groups = groups_all
		else:
			groups = Group.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			groups = groups_all
		else:
			groups = Group.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
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
		'showing_all': showing_all,
	})

def viewer_layer_source(request):
	location = ['Layer Source']
	layer_source_all = Layer_Source.objects.all()
	layer_source = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			layer_source = layer_source_all
		else:
			layer_source = Layer_Source.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			layer_source = layer_source_all
		else:
			layer_source = Layer_Source.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		layer_source = layer_source_all
	
	location.append(layer_source.count)
	mxd_links = MXD.objects.all()
	search_data = Layer_Source.objects.all().values_list('name', flat=True).distinct()

	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': layer_source,
		'mxd_links': mxd_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_mxd(request):
	location = ['MXD']
	mxd_all = MXD.objects.all()
	mxd = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			mxd = mxd_all
		else:
			mxd = MXD.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			mxd = mxd_all
		else:
			mxd = MXD.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		mxd = mxd_all

	location.append(mxd.count)
	search_data = MXD.objects.all().values_list('name', flat=True).distinct()
	web_service_links = Web_Service.objects.all()
	agol_links = AGOL_Item.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': mxd,
		'web_service_links': web_service_links,
		'agol_links': agol_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_web_adapter(request):
	location = ['Web Adapter']
	web_adapter_all = Web_Adapter.objects.all()
	web_adapter = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			web_adapter = web_adapter_all
		else:
			web_adapter = Web_Adapter.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			web_adapter = web_adapter_all
		else:
			web_adapter = Web_Adapter.objects.filter(machine_name__icontains=name)
			search_field = name
			showing_all = False
	else:
		web_adapter = web_adapter_all

	location.append(web_adapter.count)
	search_data = Web_Adapter.objects.all().values_list('machine_name', flat=True).distinct()
	web_service_links = Web_Service.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': web_adapter,
		'web_service_links': web_service_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_web_service(request):
	location = ['Web Service']
	web_service_all = Web_Service.objects.all()
	web_service = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			web_service = web_service_all
		else:
			web_service = Web_Service.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			web_service = web_service_all
		else:
			web_service = Web_Service.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		web_service = web_service_all

	location.append(web_service.count)
	search_data = Web_Service.objects.all().values_list('name', flat=True).distinct()
	agol_links = AGOL_Item.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': web_service,
		'agol_links': agol_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_webmap(request):
	location = ['Webmap']
	webmap_all = Webmap.objects.all()
	webmap = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			webmap = webmap_all
		else:
			webmap = Webmap.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			webmap = webmap_all
		else:
			webmap = Webmap.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		webmap = webmap_all

	location.append(webmap.count)
	search_data = Webmap.objects.all().values_list('name', flat=True).distinct()
	webmap_app_links = Webmap_App.objects.all()
	webmap_item_links = Webmap_Item.objects.all()
	group_links = Group.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': webmap,
		'webmap_app_links': webmap_app_links,
		'webmap_item_links': webmap_item_links,
		'group_links': group_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_webmap_app(request):
	location = ['Webmap App']
	webmap_app_all = Webmap_App.objects.all()
	webmap_app = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			webmap_app = webmap_app_all
		else:
			webmap_app = Webmap_App.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			webmap = webmap_app_all
		else:
			webmap_app = Webmap_App.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		webmap_app = webmap_app_all

	location.append(webmap_app.count)
	search_data = Webmap_App.objects.all().values_list('name', flat=True).distinct()
	group_links = Group.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': webmap_app,
		'group_links': group_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_webmap_item(request):
	location = ['Webmap Item']
	webmap_item_all = Webmap_Item.objects.all()
	webmap_item = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			webmap_item = webmap_app_all
		else:
			webmap_item = Webmap_Item.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			webmap_item = webmap_app_all
		else:
			webmap_item = Webmap_Item.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		webmap_item = webmap_item_all

	location.append(webmap_item.count)
	search_data = Webmap_Item.objects.all().values_list('name', flat=True).distinct()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': webmap_item,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})

def viewer_user(request):
	location = ['User']
	user_all = User.objects.all()
	user = None
	showing_all = True
	search_field = ''

	if 'id' in request.GET:
		i = request.GET['id']
		if not i:
			user = user_all
		else:
			user = User.objects.filter(id=i)
			showing_all = False

	elif 'name' in request.GET:
		name = request.GET['name']
		if not name:
			user = user_all
		else:
			user = User.objects.filter(name__icontains=name)
			search_field = name
			showing_all = False
	else:
		user = user_all

	location.append(user.count)
	search_data = User.objects.all().values_list('name', flat=True).distinct()
	agol_links = AGOL_Item.objects.all()
	return render(request, 'viewer_list.html',
	{
		'location': location,
		'items': user,
		'agol_links': agol_links,
		'search_data': search_data,
		'search_field': search_field,
		'showing_all': showing_all,
	})