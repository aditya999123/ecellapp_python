# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendOtp', '0002_otp_data_verify'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=120, null=True)),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('access_token', models.CharField(blank=True, max_length=120, null=True)),
                ('college', models.CharField(blank=True, max_length=120, null=True)),
                ('branch', models.CharField(blank=True, max_length=120, null=True)),
                ('sem', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
