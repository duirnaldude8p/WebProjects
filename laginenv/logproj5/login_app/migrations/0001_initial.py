# Generated by Django 2.1.4 on 2018-12-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='dude', max_length=15, null=True)),
                ('password', models.CharField(blank=True, default='dude', max_length=15, null=True)),
            ],
        ),
    ]