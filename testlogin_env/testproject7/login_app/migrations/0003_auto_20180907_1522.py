# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-07 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_userprofileinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
