# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-16 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatApp', '0007_auto_20180316_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='section',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='section',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='section',
            field=models.CharField(max_length=20, null=True),
        ),
    ]