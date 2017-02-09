"""agol_indexer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.joins_group, name="joins"),
	url(r'^groups/$', views.joins_group, name="joins_groups"),
	url(r'^webmapitems/$', views.joins_webmapitems, name="joins_webmapitems"),

	url(r'^groups/(?P<id_a>(\d+))/agol/(?P<id_b>(\d+))/delete$', views.group_agol_delete, name="joins_groups_agol_delete"),
	url(r'^groups/(?P<id_a>(\d+))/webmap/(?P<id_b>(\d+))/delete$', views.group_webmap_delete, name="joins_groups_webmap_delete"),
	url(r'^groups/(?P<id_a>(\d+))/webmapapp/(?P<id_b>(\d+))/delete$', views.group_webmap_app_delete, name="joins_groups_webmapapp_delete"),

	url(r'^webmapitems/(?P<id_a>(\d+))/agol/(?P<id_b>(\d+))/delete$', views.webmapitem_agol_delete, name="joins_webmapitems_agol_delete"),
	url(r'^webmapitems/(?P<id_a>(\d+))/webmap/(?P<id_b>(\d+))/delete$', views.webmapitem_webmap_delete, name="joins_webmapitems_webmap_delete"),
]