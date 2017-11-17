from __future__ import unicode_literals
from django.db import models
from webmap.models import Webmap, Webmap_App
from agol.models import AGOL_Item


class GroupManager(models.Manager):
    def create_group(self, name, description):
        group = self.create(name=name, description=description)
        return group


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255, blank=True)
    webmap = models.ManyToManyField(Webmap)
    webmap_app = models.ManyToManyField(Webmap_App)
    agol = models.ManyToManyField(AGOL_Item)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = GroupManager()

    dependencies = ['agol', 'webmap', 'webmap_app']
    reverse_dependencies = []

    class Meta:
        verbose_name = 'AGOL Group'
        ordering = ['name']

    def __str__(self):
        return self.name
