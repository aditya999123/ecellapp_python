# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-21 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_auto_20160820_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus_data',
            name='image',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
