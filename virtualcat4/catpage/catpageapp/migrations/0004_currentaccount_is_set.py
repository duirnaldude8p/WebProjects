# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-25 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catpageapp', '0003_auto_20180325_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentaccount',
            name='is_set',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
