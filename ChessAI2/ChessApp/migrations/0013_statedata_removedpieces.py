# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-10 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessApp', '0012_auto_20180410_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='statedata',
            name='RemovedPieces',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]