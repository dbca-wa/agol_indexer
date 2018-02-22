from __future__ import unicode_literals
from django.db import models
from agol.models import AGOL_Item


class Webmap_Contact(models.Model):
    contact_name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Webmap Contact'
        ordering = ['contact_name']

    def __str__(self):
        return self.contact_name


class Webmap(models.Model):
    name = models.CharField(max_length=60)
    purpose = models.CharField(max_length=255)
    url = models.URLField(help_text="URL of the web map")
    contact = models.ForeignKey(Webmap_Contact)
    collector = models.BooleanField()
    collector_offline = models.BooleanField()
    agols = models.ManyToManyField(AGOL_Item, related_name='webmaps', related_query_name='agol')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    dependencies = ['agols']
    reverse_dependencies = ['webmap_app_set']

    class Meta:
        verbose_name = 'Webmap'
        ordering = ['name']

    def __str__(self):
        return self.name


class Webmap_App(models.Model):
    name = models.CharField(max_length=60)
    purpose = models.CharField(max_length=255)
    url = models.URLField(help_text="URL of the web mapping application")
    contact = models.ForeignKey(Webmap_Contact)
    webmap = models.ForeignKey(Webmap)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    dependencies = ['webmap']
    reverse_dependencies = ['group_set']

    class Meta:
        verbose_name = 'Webmap App'
        ordering = ['name']

    def __str__(self):
        return self.name
