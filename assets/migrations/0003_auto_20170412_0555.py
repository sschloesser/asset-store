# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 05:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20170412_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z][0-9a-zA-Z_-]{3,63}$', message='4-64 chars; only alphanumeric ascii, underscore and dash allowed; must start with alphanumeric.')]),
        ),
    ]
