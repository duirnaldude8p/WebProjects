# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-07 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_remove_userprofileinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='usrnm',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]