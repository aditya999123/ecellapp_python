# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendOtp', '0010_fcm__not_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
