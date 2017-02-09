from django.shortcuts import render
from webmap.models import Webmap_Item
from groups.models import Group

# Create your views here.
def joins_group(request):
	group = None

	if 'group_id' in request.GET:
		group_id = request.GET['group_id']
		if group_id:
			group = Group.objects.get(id=group_id)
		
	groups_list = Group.objects.values('id', 'name')

	return render(request, 'joins_index.html', {
		'type': 'Group',
		'selected_item': group,
		'item_list': groups_list
	})

def joins_webmapitems(request):
	wmi = None

	if 'wmi_id' in request.GET:
		wmi_id = request.GET['wmi_id']
		if wmi_id:
			wmi = Webmap_Item.objects.get(id=wmi_id)
		
	wmi_list = Webmap_Item.objects.values('id', 'name')

	return render(request, 'joins_index.html', {
		'type': 'Webmap Item',
		'selected_item': wmi,
		'item_list': wmi_list
	})