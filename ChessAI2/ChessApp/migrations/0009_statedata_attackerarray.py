# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-09 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessApp', '0008_auto_20180309_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='statedata',
            name='AttackerArray',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
