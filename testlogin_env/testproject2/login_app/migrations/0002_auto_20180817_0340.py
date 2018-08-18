# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-17 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import login_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=login_app.models.profile_image_path),
        ),
    ]
