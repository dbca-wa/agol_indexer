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
from webmap.models import Webmap, Webmap_App, Webmap_Item
import datetime

def index_home(request):
	errors = []
	s = None
	search_history = None
	agol = None
	groups = None
	layer_source = None
	mxd = None
	web_adapter = None
	web_service = None
	webmap = None
	webmap_app = None
	webmap_item = None
	search_field = ''
	result_amount = None
	mxd_links = None

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
			webmap_item = Webmap_Item.objects.filter(Q(name__icontains=s) | Q(agol_item__name__icontains=s) | Q(webmap__name__icontains=s)).distinct()

			mxd_links = MXD.objects.all()
			result_amount = len(agol) + len(groups) + len(layer_source) + len(mxd) + len(web_adapter) + len(web_service) + len(webmap) + len(webmap_app) + len(webmap_item)
			search_field = s

	if 'search_history' in request.COOKIES:
		search_history = getSearchHistory(request)
	print search_history

	response = render(request, 'home_search.html',
	{
		'agols': agol,
		'groups': groups,
		'layer_sources': layer_source,
		'mxds': mxd,
		'web_adapters': web_adapter,
		'web_services': web_service,
		'webmaps': webmap,
		'webmap_apps': webmap_app,
		'webmap_items': webmap_item,
		'errors': errors,
		'search_field': search_field,
		'result_amount': result_amount,
		'search_history': search_history,
		'mxd_links': mxd_links,
	})
	if s:
		expireTime = datetime.datetime.now() + datetime.timedelta(days=30)
		response.set_cookie('search_history', setSearchHistory(request, s, search_history), expires=expireTime)
	return response

def setSearchHistory(request, s, search_history_str):
	search_history_arr = []
	if search_history_str == None:
		return s
	else:
		search_history_str = ','.join(map(str, search_history_str))
		if ',' in search_history_str:
			search_history_arr = search_history_str.split(',')
		else:
			search_history_arr.append(search_history_str)
		
		if s.lower() not in search_history_arr:
			search_history_arr.append(s.lower())
		else:
			search_history_arr.remove(s.lower())
			search_history_arr.append(s.lower())

		if len(search_history_arr) > 5:
			search_history_arr.pop(0)

		search_history_str = ','.join(map(str, search_history_arr))
		return search_history_str

def getSearchHistory(request):
	search_history_str = request.COOKIES['search_history']
	search_history_arr = search_history_str.split(',')
	return search_history_arr