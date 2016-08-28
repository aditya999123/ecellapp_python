# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=1200, null=True)),
                ('date', models.CharField(blank=True, max_length=120, null=True)),
                ('owner', models.CharField(blank=True, max_length=120, null=True)),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contacts_data',
        ),
    ]