# Generated by Django 2.1.4 on 2018-12-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='password',
            field=models.CharField(blank=True, default='dude', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='username',
            field=models.CharField(blank=True, default='dude', max_length=15, null=True),
        ),
    ]
