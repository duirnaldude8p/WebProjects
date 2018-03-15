# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-14 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CatApp', '0002_auto_20180312_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='accounts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CatApp.Account'),
        ),
        migrations.AddField(
            model_name='main',
            name='cat_comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CatApp.Cat_Comment'),
        ),
        migrations.AddField(
            model_name='main',
            name='cats',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CatApp.Cat'),
        ),
    ]
