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
    url(r'^layersources/$', views.dependencies_layer_source, name='dependencies_layer_source'),
    url(r'^mxds/$', views.dependencies_mxd, name='dependencies_mxd'),
    url(r'^webservices/$', views.dependencies_web_service, name='dependencies_web_service'),
    url(r'^agols/$', views.dependencies_agol, name='dependencies_agol'),
    url(r'^webmaps/$', views.dependencies_webmap, name='dependencies_webmap'),
    url(r'^webmapapps/$', views.dependencies_webmap_app, name='dependencies_webmap_app'),
    url(r'^groups/$', views.dependencies_group, name='dependencies_group'),
]
