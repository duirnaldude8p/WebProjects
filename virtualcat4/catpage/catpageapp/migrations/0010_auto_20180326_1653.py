# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-26 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catpageapp', '0009_auto_20180326_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='breed',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='cat_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='cat_pic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='story',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
