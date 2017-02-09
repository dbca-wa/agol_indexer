from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from webmap.models import Webmap_Item, Webmap, Webmap_App
from groups.models import Group
from agol.models import AGOL_Item


# Create your views here.
def joins_group(request):
	group = None
	agol_list = None
	webmap_list = None
	webmap_app_list = None

	if 'group_id' in request.GET:
		group_id = request.GET['group_id']
		if group_id:
			group = Group.objects.get(id=group_id)

			agol_list = AGOL_Item.objects.all().exclude(id__in=group.agol.all())
			webmap_list = Webmap.objects.all().exclude(id__in=group.webmap.all())
			webmap_app_list = Webmap_App.objects.all().exclude(id__in=group.webmap_app.all())
		
	groups_list = Group.objects.values('id', 'name').order_by('name')

	return render(request, 'joins_index.html', {
		'type': 'Group',
		'selected_item': group,
		'item_list': groups_list,
		'agol_list': agol_list,
		'webmap_list': webmap_list,
		'webmap_app_list': webmap_app_list,
	})

def joins_webmapitems(request):
	wmi = None
	agol_list = None
	webmap_list = None

	if 'wmi_id' in request.GET:
		wmi_id = request.GET['wmi_id']
		if wmi_id:
			wmi = Webmap_Item.objects.get(id=wmi_id)

			agol_list = AGOL_Item.objects.all().exclude(id__in=wmi.agol.all())
			webmap_list = Webmap.objects.all().exclude(id__in=wmi.webmap.all())
		
	wmi_list = Webmap_Item.objects.values('id', 'name').order_by('name')

	return render(request, 'joins_index.html', {
		'type': 'Webmap Item',
		'selected_item': wmi,
		'item_list': wmi_list,
		'agol_list': agol_list,
		'webmap_list': webmap_list,
	})

def group_agol_delete(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	agol = get_object_or_404(AGOL_Item, id=id_b)

	group.agol.remove(agol)

	return HttpResponseRedirect(reverse('joins_groups'))

def group_webmap_delete(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	webmap = get_object_or_404(Webmap, id=id_b)

	group.webmap.remove(webmap)

	return HttpResponseRedirect(reverse('joins_groups'))

def group_webmap_app_delete(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	webmap_app = get_object_or_404(Webmap_App, id=id_b)

	group.webmap_app.remove(webmap_app)

	return HttpResponseRedirect(reverse('joins_groups'))

def webmapitem_agol_delete(request, id_a, id_b):
	webmap_item = get_object_or_404(Group, id=id_a)
	agol = get_object_or_404(AGOL_Item, id=id_b)

	webmap_item.agol.remove(agol)

	return HttpResponseRedirect(reverse('joins_groups'))

def webmapitem_webmap_delete(request, id_a, id_b):
	webmap_item = get_object_or_404(Group, id=id_a)
	webmap = get_object_or_404(Webmap, id=id_b)

	webmap_item.webmap.remove(webmap)

	return HttpResponseRedirect(reverse('joins_groups'))