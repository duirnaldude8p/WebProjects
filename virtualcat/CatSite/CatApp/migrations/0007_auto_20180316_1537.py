# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-16 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatApp', '0006_auto_20180315_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='cat_comments',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='cats',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='comments',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='accounts',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='cat_comments',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='cats',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='comments',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='Cat_Comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]