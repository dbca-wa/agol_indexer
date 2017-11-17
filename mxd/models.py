from __future__ import unicode_literals
from django.db import models
from layer_source.models import Layer_Source


class MxdManager(models.Manager):
    def create_mxd(self, name, created_on, client_id, created_by_id, path, description):
        mxd = self.create(name=name, created_on=created_on, client_id=client_id, created_by_id=created_by_id, path=path, description=description)
        return mxd


class MXD_Client(models.Model):
    client = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'MXD Client'
        ordering = ['client']

    def __str__(self):
        return self.client


class MXD_Creator(models.Model):
    creator = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'MXD Creator'
        ordering = ['creator']

    def __str__(self):
        return self.creator


class MXD(models.Model):
    name = models.CharField(max_length=60)
    path = models.CharField(max_length=500)
    description = models.TextField(max_length=255, blank=True)
    client = models.ForeignKey(MXD_Client)
    created_by = models.ForeignKey(MXD_Creator)
    created_on = models.DateTimeField()
    layer_source = models.ManyToManyField(Layer_Source)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = MxdManager()

    dependencies = ['layer_source']
    reverse_dependencies = ['agol_item_set', 'web_service_set']

    class Meta:
        verbose_name = 'MXD'
        ordering = ['name']

    def __str__(self):
        return "%s - %s" % (self.name, self.created_by)