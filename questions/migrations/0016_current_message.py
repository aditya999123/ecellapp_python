# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-27 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_auto_20160825_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='message',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]