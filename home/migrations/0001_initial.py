# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-20 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('number', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
