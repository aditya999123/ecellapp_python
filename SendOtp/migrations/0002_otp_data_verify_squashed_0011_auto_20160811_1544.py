# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'SendOtp', '0002_otp_data_verify'), (b'SendOtp', '0003_user_data'), (b'SendOtp', '0004_gcm_data'), (b'SendOtp', '0005_user_data_gcm'), (b'SendOtp', '0006_auto_20160801_1719'), (b'SendOtp', '0007_auto_20160801_1721'), (b'SendOtp', '0008_auto_20160806_1405'), (b'SendOtp', '0009_auto_20160806_1422'), (b'SendOtp', '0010_fcm__not_registered'), (b'SendOtp', '0011_auto_20160811_1544')]

    dependencies = [
        ('SendOtp', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp_data',
            name='verify',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(blank=True, max_length=120, null=True)),
                ('first_name', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('college', models.CharField(blank=True, max_length=120, null=True)),
                ('branch', models.CharField(blank=True, max_length=120, null=True)),
                ('sem', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_token_data',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key='True', serialize=False)),
                ('fcm', models.CharField(blank=True, max_length=400, null=True)),
                ('access_token', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fcm__not_registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
