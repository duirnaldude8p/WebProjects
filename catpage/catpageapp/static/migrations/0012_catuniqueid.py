# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-27 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catpageapp', '0011_auto_20180326_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatUniqueId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
