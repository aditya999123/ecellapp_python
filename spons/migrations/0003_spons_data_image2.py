# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-30 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spons', '0002_remove_spons_data_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='spons_data',
            name='image2',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
