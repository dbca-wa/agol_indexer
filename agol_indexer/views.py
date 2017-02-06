from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import Q
from agol.models import AGOL_Item
from groups.models import Group
from layer_source.models import Layer_Source
from mxd.models import MXD
from users.models import User
from web_adapter.models import Web_Adapter
from web_service.models import Web_Service
from webmap.models import Webmap, Webmap_App

def index_home(request):
	agol = None
	groups = None
	layer_source = None
	mxd = None
	web_adapter = None
	web_service = None
	webmap = None
	webmap_app = None
	search_field = ''

	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			errors = ('Enter a search term.')
		else:
			agol = AGOL_Item.objects.filter(Q(name__icontains=name) | Q(external_layer_url__icontains=name) | Q(mxd__name__icontains=name) | Q(owner__name__icontains=name)).distinct()
			groups = Group.objects.filter(Q(name__icontains=name) | Q(webmap__name__icontains=name) | Q(webmap_app__name__icontains=name)).distinct()
			layer_source = Layer_Source.objects.filter(name__icontains=name).distinct()
			mxd = MXD.objects.filter(Q(name__icontains=name) | Q(client__client__icontains=name) | Q(created_by__creator__icontains=name)).distinct()
			web_adapter = None
			web_service = None
			webmap = None
			webmap_app = None

			search_field = name

	return render(request, 'home_search.html',
	{
		'agols': agol,
		'groups': groups,
		'layer_sources': layer_source,
		'mxds': mxd,
		'web_adapters': web_adapter,
		'web_services': web_service,
		'webmaps': webmap,
		'webmap_apps': webmap_app,
		'search_field': search_field,
	})