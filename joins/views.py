from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from webmap.models import Webmap_Item, Webmap, Webmap_App
from groups.models import Group
from agol.models import AGOL_Item
from joins.forms import CreateGroupForm, CreateWebmapItemsForm


# Create your views here.
def joins_group(request):
	if 'group_id' in request.GET:
		group_id = request.GET['group_id']
		if group_id:
			return HttpResponseRedirect(reverse_lazy('joins_groups', args=(group_id)))
	else:
		groups_list = Group.objects.values('id', 'name').order_by('name')

		return render(request, 'joins_index.html', {
			'type': 'Group',
			'selected_item': None,
			'item_list': groups_list,
		})

def joins_getGroup(request, group_id):
	if 'agol_add_id' in request.GET:
		agol_id = request.GET['agol_add_id']
		if agol_id:
			return group_agol_add(request, group_id, agol_id)
	
	elif 'webmap_add_id' in request.GET:
		webmap_id = request.GET['webmap_add_id']
		if webmap_id:
			return group_webmap_add(request, group_id, webmap_id)

	elif 'webmap_app_add_id' in request.GET:
		webmap_app_id = request.GET['webmap_app_add_id']
		if webmap_app_id:
			return group_webmap_app_add(request, group_id, webmap_app_id)

	else:
		group = get_object_or_404(Group, id=group_id)

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
	if 'wmi_id' in request.GET:
		wmi_id = request.GET['wmi_id']
		if wmi_id:	
			return HttpResponseRedirect(reverse_lazy('joins_webmapitems', args=(wmi_id)))
	else:
		wmi_list = Webmap_Item.objects.values('id', 'name').order_by('name')

		return render(request, 'joins_index.html', {
			'type': 'Webmap Item',
			'selected_item': None,
			'item_list': wmi_list,
		})

def joins_getWebmapitems(request, wmi_id):
	if 'agol_add_id' in request.GET:
		agol_id = request.GET['agol_add_id']
		if agol_id:
			return webmapitem_agol_add(request, wmi_id, agol_id)
	
	elif 'webmap_add_id' in request.GET:
		webmap_id = request.GET['webmap_add_id']
		if webmap_id:
			return webmapitem_webmap_add(request, wmi_id, webmap_id)
	else:
		wmi = get_object_or_404(Webmap_Item, id=wmi_id)

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

########
#ADD#
########
def group_agol_add(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	agol = get_object_or_404(AGOL_Item, id=id_b)

	group.agol.add(agol)

	return HttpResponseRedirect(reverse_lazy('joins_groups', args=(id_a)))

def group_webmap_add(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	webmap = get_object_or_404(Webmap, id=id_b)

	group.webmap.add(webmap)

	return HttpResponseRedirect(reverse_lazy('joins_groups', args=(id_a)))

def group_webmap_app_add(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	webmap_app = get_object_or_404(Webmap_App, id=id_b)

	group.webmap_app.add(webmap_app)

	return HttpResponseRedirect(reverse_lazy('joins_groups', args=(id_a)))

def webmapitem_agol_add(request, id_a, id_b):
	webmap_item = get_object_or_404(Webmap_Item, id=id_a)
	agol = get_object_or_404(AGOL_Item, id=id_b)

	webmap_item.agol.add(agol)

	return HttpResponseRedirect(reverse_lazy('joins_webmapitems', args=(id_a)))

def webmapitem_webmap_add(request, id_a, id_b):
	webmap_item = get_object_or_404(Webmap_Item, id=id_a)
	webmap = get_object_or_404(Webmap, id=id_b)

	webmap_item.webmap.add(webmap)

	return HttpResponseRedirect(reverse_lazy('joins_webmapitems', args=(id_a)))

########
#REMOVE#
########
def group_agol_delete(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	agol = get_object_or_404(AGOL_Item, id=id_b)

	group.agol.remove(agol)

	return HttpResponseRedirect(reverse_lazy('joins_groups', args=(id_a)))

def group_webmap_delete(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	webmap = get_object_or_404(Webmap, id=id_b)

	group.webmap.remove(webmap)

	return HttpResponseRedirect(reverse_lazy('joins_groups', args=(id_a)))

def group_webmap_app_delete(request, id_a, id_b):
	group = get_object_or_404(Group, id=id_a)
	webmap_app = get_object_or_404(Webmap_App, id=id_b)

	group.webmap_app.remove(webmap_app)

	return HttpResponseRedirect(reverse_lazy('joins_groups', args=(id_a)))

def webmapitem_agol_delete(request, id_a, id_b):
	webmap_item = get_object_or_404(Webmap_Item, id=id_a)
	agol = get_object_or_404(AGOL_Item, id=id_b)

	webmap_item.agol.remove(agol)

	return HttpResponseRedirect(reverse_lazy('joins_webmapitems', args=(id_a)))

def webmapitem_webmap_delete(request, id_a, id_b):
	webmap_item = get_object_or_404(Webmap_Item, id=id_a)
	webmap = get_object_or_404(Webmap, id=id_b)

	webmap_item.webmap.remove(webmap)

	return HttpResponseRedirect(reverse_lazy('joins_webmapitems', args=(id_a)))

#######
#JOINS#
#######

def group_create(request):
	if request.method == "POST":
		groupForm = CreateGroupForm(request.POST)

		if groupForm.is_valid():
			print groupForm

			data = groupForm.cleaned_data
			name = data['name']
			description = data['description']

			group = Group.objects.create_group(name, description)

			return HttpResponseRedirect(reverse_lazy('joins_webmapitems', args=(group.id)))

def webmapitems_create(request):
	if request.method == "POST":
		webmapItemForm = CreateWebmapItemsForm(request.POST)

		if webmapItemForm.is_valid():
			name = CreateWebmapItemsForm.cleaned_data['name']
			description = CreateWebmapItemsForm.cleaned_data['description']