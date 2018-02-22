from django.db.models.base import Model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from agol.models import AGOL_Item
from groups.models import Group
from layer_source.models import Layer_Source
from mxd.models import MXD
from web_service.models import Web_Service
from webmap.models import Webmap
from webmap.models import Webmap_App


def dependencies_layer_source(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(Layer_Source, id=i)

    return dependencies_generic(request, subject)


def dependencies_mxd(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(MXD, id=i)

    return dependencies_generic(request, subject)


def dependencies_web_service(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(Web_Service, id=i)

    return dependencies_generic(request, subject)


def dependencies_agol(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(AGOL_Item, id=i)

    return dependencies_generic(request, subject)


def dependencies_webmap(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(Webmap, id=i)

    return dependencies_generic(request, subject)


def dependencies_webmap_app(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(Webmap_App, id=i)

    return dependencies_generic(request, subject)


def dependencies_group(request):
    if 'id' not in request.GET:
        raise Http404()

    i = request.GET['id']
    subject = get_object_or_404(Group, id=i)

    return dependencies_generic(request, subject)


def dependencies_generic(request, subject):

    items_by_table = {
        "layer_source": [],
        'mxd': [],
        'web_service': [],
        'agol_item': [],
        'webmap': [],
        'webmap_app': [],
        'group': [],
    }

    dependencies = _bidirectional_dependencies(subject)
    for item in dependencies:
        items_by_table[item._meta.model_name].append(item)

    layer_sources = ListWrapper(items_by_table['layer_source'])
    mxds = ListWrapper(items_by_table['mxd'])
    web_services = ListWrapper(items_by_table['web_service'])
    agols = ListWrapper(items_by_table['agol_item'])
    webmaps = ListWrapper(items_by_table['webmap'])
    webmap_apps = ListWrapper(items_by_table['webmap_app'])
    groups = ListWrapper(items_by_table['group'])

    return render(
        request,
        'home_search.html',
        {
            'title': "Dependencies for {}: {}".format(subject._meta.verbose_name, subject.name),
            'hide_search': True,

            'layer_sources': layer_sources,
            'mxds': mxds,
            'web_services': web_services,
            'agols': agols,
            'webmaps': webmaps,
            'webmap_apps': webmap_apps,
            'groups': groups,
        }
    )


def _bidirectional_dependencies(subject):
    dependencies = _deep_dependencies(subject, "dependencies")
    reverse_dependencies = _deep_dependencies(subject, "reverse_dependencies")

    results = dependencies | reverse_dependencies
    results.add(subject)
    return results


def _deep_dependencies(subject, dependencies_list_name):
    checked = set()
    unchecked = set()
    unchecked.add(subject)
    while len(unchecked) > 0:
        current = unchecked.pop()
        unchecked |= _direct_dependencies(current, dependencies_list_name)
        checked.add(current)
    checked.remove(subject)
    return checked


def _direct_dependencies(subject, dependencies_list_name):
    dependencies = set()
    if not hasattr(subject, dependencies_list_name):
        return dependencies
    dependencies_list = getattr(subject, dependencies_list_name)
    for field_name in dependencies_list:
        field = getattr(subject, field_name)
        if field is None:
            continue
        if issubclass(type(field), Model):
            dependencies.add(field)
            continue
        if type(field) is list:
            for item in field:
                dependencies.add(item)
            continue
        for rd_item in field.select_related().all():
            dependencies.add(rd_item)
    return dependencies


class ListWrapper(object):
    """ This is a quick hack to allow us to pass a list to templates that
        expect a django QuerySet object.  Currently only a small subset of the
        QuerySet interface is required """

    def __init__(self, lst):
        self.list = lst

    # will be used to support for loops
    def __iter__(self):
        return self.list.__iter__()

    # will be used for boolean / empty checks
    def __len__(self):
        return len(self.list)

    # will be used for pluralisation
    def count(self):
        return len(self.list)
