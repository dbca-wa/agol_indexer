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
	url(r'^$', views.viewer_home, name="viewer"),
	url(r'^agol/$', views.viewer_agol, name='viewer_agol'),
	url(r'^group/$', views.viewer_groups, name='viewer_group'),
	url(r'^layersource/$', views.viewer_layer_source, name='viewer_layer_source'),
	url(r'^mxd/$', views.viewer_mxd, name='viewer_mxd'),
	url(r'^webmap/$', views.viewer_webmap, name='viewer_webmap'),
	url(r'^webmapapp/$', views.viewer_webmap_app, name='viewer_webmap_app'),
	url(r'^webmapitem/$', views.viewer_webmap_item, name='viewer_webmap_item'),
	url(r'^webadapter/$', views.viewer_web_adapter, name='viewer_web_adapter'),
	url(r'^webservice/$', views.viewer_web_service, name='viewer_web_service'),
	url(r'^user/$', views.viewer_user, name='viewer_user'),
]