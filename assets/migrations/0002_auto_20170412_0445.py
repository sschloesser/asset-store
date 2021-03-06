# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_class',
            field=models.CharField(choices=[('dove', 'Dove (satellite class)'), ('rapideye', 'Rapideye (satellite class)'), ('dish', 'Dish (antenna class)'), ('yagi', 'Yagi (antenna class)')], max_length=8),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('satellite', 'Satellite Asset Type'), ('antenna', 'Antenna Asset Type')], max_length=9),
        ),
        migrations.AlterField(
            model_name='assetdetail',
            name='val_type',
            field=models.CharField(choices=[('F', 'float'), ('B', 'boolean'), ('I', 'integer'), ('S', 'string')], max_length=1),
        ),
    ]
