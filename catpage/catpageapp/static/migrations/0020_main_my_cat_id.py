# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-31 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catpageapp', '0019_auto_20180331_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='my_cat_id',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
