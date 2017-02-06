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
	errors = []
	agol = None
	groups = None
	layer_source = None
	mxd = None
	web_adapter = None
	web_service = None
	webmap = None
	webmap_app = None
	search_field = ''

	if 'search' in request.GET:
		s = request.GET['search']
		if not s:
			errors.append('Please enter a search term.')
		else:
			agol = AGOL_Item.objects.filter(Q(name__icontains=s) | Q(url__name__icontains=s) | Q(external_layer_url__icontains=s) | Q(mxd__name__icontains=s) | Q(owner__name__icontains=s)).distinct()
			groups = Group.objects.filter(Q(name__icontains=s) | Q(webmap__name__icontains=s) | Q(webmap_app__name__icontains=s)).distinct()
			layer_source = Layer_Source.objects.filter(name__icontains=s).distinct()
			mxd = MXD.objects.filter(Q(name__icontains=s) | Q(client__client__icontains=s) | Q(created_by__creator__icontains=s)).distinct()
			web_adapter = Web_Adapter.objects.filter(Q(machine_name__icontains=s) | Q(alias__icontains=s)).distinct()
			web_service = Web_Service.objects.filter(Q(name__icontains=s)| Q(actual_url__icontains=s) | Q(alias_url__icontains=s) | Q(mxd__name__icontains=s) | Q(web_adapter__machine_name__icontains=s)).distinct()
			webmap = Webmap.objects.filter(Q(name__icontains=s) | Q(contact__contact_name__icontains=s)).distinct()
			webmap_app = Webmap_App.objects.filter(Q(name__icontains=s) | Q(url__icontains=s) | Q(contact__contact_name__icontains=s) | Q(webmap__name__icontains=s)).distinct()

			result_amount = len(agol) + len(groups) + len(layer_source) + len(mxd) + len(web_adapter) + len(web_service) + len(webmap) + len(webmap_app)
			search_field = s

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
		'errors': errors,
		'search_field': search_field,
		'result_amount': result_amount,
	})