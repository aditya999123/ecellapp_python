# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendOtp', '0007_auto_20160801_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_token_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm', models.CharField(blank=True, max_length=400, null=True)),
                ('access_token', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='fcm_data',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='fcm',
        ),
    ]