# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-16 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatApp', '0009_auto_20180316_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='user',
        ),
    ]