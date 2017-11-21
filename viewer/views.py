from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.core import serializers
from agol.models import AGOL_Item
from groups.models import Group
from layer_source.models import Layer_Source
from mxd.models import MXD
from agol_users.models import AGOL_User
from web_adapter.models import Web_Adapter
from web_service.models import Web_Service
from webmap.models import Webmap, Webmap_App, Webmap_Item


def viewer_home(request):
    return render(request, 'viewer_index.html')


def viewer_agol(request):
    location = ['ArcGIS Online Item']
    agol = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            agol = AGOL_Item.objects.all().order_by('name')
        else:
            agol = AGOL_Item.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            agol = AGOL_Item.objects.all().order_by('name')
        else:
            agol = AGOL_Item.objects.filter(name__icontains=name).order_by('name')
            showing_all = False
            search_field = name
    else:
        agol = AGOL_Item.objects.all().order_by('name')
    
    agol = paginator(request, agol)

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
    groups = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            groups = Group.objects.all().order_by('name')
        else:
            groups = Group.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            groups = Group.objects.all().order_by('name')
        else:
            groups = Group.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        groups = Group.objects.all().order_by('name')
    
    groups = paginator(request, groups)

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
    layer_source = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            layer_source = Layer_Source.objects.all().order_by('name')
        else:
            layer_source = Layer_Source.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            layer_source = Layer_Source.objects.all().order_by('name')
        else:
            layer_source = Layer_Source.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        layer_source = Layer_Source.objects.all().order_by('name')
    
    layer_source = paginator(request, layer_source)

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
    mxd = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            mxd = MXD.objects.all().order_by('name')
        else:
            mxd = MXD.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            mxd = MXD.objects.all().order_by('name')
        else:
            mxd = MXD.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        mxd = MXD.objects.all().order_by('name')

    mxd = paginator(request, mxd)

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
    web_adapter = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            web_adapter = Web_Adapter.objects.all().order_by('machine_name')
        else:
            web_adapter = Web_Adapter.objects.filter(id=i).order_by('machine_name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            web_adapter = Web_Adapter.objects.all().order_by('machine_name')
        else:
            web_adapter = Web_Adapter.objects.filter(machine_name__icontains=name).order_by('machine_name')
            search_field = name
            showing_all = False
    else:
        web_adapter = Web_Adapter.objects.all().order_by('machine_name')

    web_adapter = paginator(request, web_adapter)

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
    web_service = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            web_service = Web_Service.objects.all().order_by('name')
        else:
            web_service = Web_Service.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            web_service = Web_Service.objects.all().order_by('name')
        else:
            web_service = Web_Service.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        web_service = Web_Service.objects.all().order_by('name')

    web_service = paginator(request, web_service)

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
    webmap = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            webmap = Webmap.objects.all().order_by('name')
        else:
            webmap = Webmap.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            webmap = Webmap.objects.all().order_by('name')
        else:
            webmap = Webmap.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        webmap = Webmap.objects.all().order_by('name')

    webmap = paginator(request, webmap)

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
    webmap_app = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            webmap_app = Webmap_App.objects.all().order_by('name')
        else:
            webmap_app = Webmap_App.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            webmap = Webmap_App.objects.all().order_by('name')
        else:
            webmap_app = Webmap_App.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        webmap_app = Webmap_App.objects.all().order_by('name')

    webmap_app = paginator(request, webmap_app)

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
    webmap_item = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            webmap_item = Webmap_Item.objects.all().order_by("name")
        else:
            webmap_item = Webmap_Item.objects.filter(id=i).order_by("name")
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            webmap_item = Webmap_Item.objects.all().order_by('name')
        else:
            webmap_item = Webmap_Item.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        webmap_item = Webmap_Item.objects.all().order_by('name')

    webmap_item = paginator(request, webmap_item)

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
    user = None
    showing_all = True
    search_field = ''

    if 'id' in request.GET:
        i = request.GET['id']
        if not i:
            user = AGOL_User.objects.all().order_by('name')
        else:
            user = AGOL_User.objects.filter(id=i).order_by('name')
            showing_all = False

    elif 'name' in request.GET:
        name = request.GET['name']
        if not name:
            user = AGOL_User.objects.all().order_by('name')
        else:
            user = AGOL_User.objects.filter(name__icontains=name).order_by('name')
            search_field = name
            showing_all = False
    else:
        user = AGOL_User.objects.all().order_by('name')
    
    user = paginator(request, user)

    location.append(user.count)
    search_data = AGOL_User.objects.all().values_list('name', flat=True).distinct()
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


# pagination
def paginator(request, items):
    # 14 results per page
    result_amount = request.GET.get('showing')
    if result_amount is None:
        result_amount = 14
    paginator = Paginator(items, result_amount)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return items