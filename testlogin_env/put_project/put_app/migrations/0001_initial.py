# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-18 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
        ),
    ]