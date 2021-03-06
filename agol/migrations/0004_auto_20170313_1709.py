# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agol', '0003_auto_20170313_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agol_item',
            name='mxd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxd.MXD', verbose_name='MXD'),
        ),
        migrations.AlterField(
            model_name='agol_item',
            name='url',
            field=models.ForeignKey(help_text='Select  the layers web service aliased URL from the list', on_delete=django.db.models.deletion.CASCADE, to='web_service.Web_Service', verbose_name='Web Service URL'),
        ),
    ]
