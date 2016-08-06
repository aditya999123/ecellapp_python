# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20160803_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=120, null=True)),
                ('question_type', models.SmallIntegerField(default=-10)),
                ('duration', models.SmallIntegerField(default=120)),
                ('option1', models.CharField(blank=True, max_length=120, null=True)),
                ('option2', models.CharField(blank=True, max_length=120, null=True)),
                ('option3', models.CharField(blank=True, max_length=120, null=True)),
                ('option4', models.CharField(blank=True, max_length=120, null=True)),
                ('image_url', models.CharField(blank=True, max_length=120, null=True)),
                ('ans', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]