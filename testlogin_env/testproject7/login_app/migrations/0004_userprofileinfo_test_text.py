# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-07 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20180907_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='test_text',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
