from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from webmap.models import Webmap, Webmap_App
from mxd.models import MXD, MXD_Client, MXD_Creator
from layer_source.models import Layer_Source
from groups.models import Group
from agol.models import AGOL_Item
from joins.forms import CreateGroupForm, CreateWebmapItemsForm, CreateMxdForm
from datetime import datetime


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


def joins_MXD(request):
    if 'mxd_id' in request.GET:
        mxd_id = request.GET['mxd_id']
        if mxd_id:
            return HttpResponseRedirect(reverse_lazy('joins_mxds', args=(mxd_id)))
    else:
        mxd_list = MXD.objects.values('id', 'name').order_by('name')
        client_list = MXD_Client.objects.values('id', 'client').order_by('client')
        creator_list = MXD_Creator.objects.values('id', 'creator').order_by('creator')

        return render(request, 'joins_index.html', {
            'type': 'MXD',
            'selected_item': None,
            'item_list': mxd_list,
            'client_list': client_list,
            'creator_list': creator_list,
        })


def joins_getMXD(request, mxd_id):
    if 'layersource_add_id' in request.GET:
        layersource_id = request.GET['layersource_add_id']
        if layersource_id:
            return mxd_layersource_add(request, mxd_id, layersource_id)

    else:
        mxd = get_object_or_404(MXD, id=mxd_id)

        layersource_list = Layer_Source.objects.all().exclude(id__in=mxd.layer_source.all())

        mxd_list = MXD.objects.values('id', 'name').order_by('name')

        return render(request, 'joins_index.html', {
            'type': 'MXD',
            'selected_item': mxd,
            'item_list': mxd_list,
            'layersource_list': layersource_list,
        })


#######
# ADD #
#######


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


def mxd_layersource_add(request, id_a, id_b):
    mxd = get_object_or_404(MXD, id=id_a)
    layer_source = get_object_or_404(Layer_Source, id=id_b)

    mxd.layer_source.add(layer_source)

    return HttpResponseRedirect(reverse_lazy('joins_mxds', args=(id_a)))


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


##########
# REMOVE #
##########


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


def mxd_layersource_delete(request, id_a, id_b):
    mxd = get_object_or_404(MXD, id=id_a)
    layer_source = get_object_or_404(Layer_Source, id=id_b)

    mxd.layer_source.remove(layer_source)

    return HttpResponseRedirect(reverse_lazy('joins_mxds', args=(id_a)))


#########
# JOINS #
#########


def group_create(request):
    if request.method == "POST":
        groupForm = CreateGroupForm(request.POST)

        if groupForm.is_valid():
            data = groupForm.cleaned_data
            name = data['name']
            description = data['description']

            group = Group.objects.create_group(name, description)

            return HttpResponseRedirect(reverse_lazy('joins_groups', args=(group.id,)))


def mxd_create(request):
    if request.method == "POST":
        mxdForm = CreateMxdForm(request.POST)

        if mxdForm.is_valid():
            data = mxdForm.cleaned_data
            name = data['name']
            path = data['path']
            description = data['description']
            created_on = data['created_on']
            created_by_id = data['created_by']
            client_id = data['client']
            created_on_formatted = datetime.strptime(created_on, '%d/%m/%Y %H:%M')

            mxd = MXD.objects.create_mxd(name, created_on_formatted, client_id, created_by_id, path, description)

            return HttpResponseRedirect(reverse_lazy('joins_mxds', args=(mxd.id,)))
