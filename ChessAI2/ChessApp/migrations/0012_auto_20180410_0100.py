# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-10 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessApp', '0011_auto_20180408_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='statedata',
            name='CompMadeRemove',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='statedata',
            name='CompRemoves',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
