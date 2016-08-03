from __future__ import unicode_literals

from django.db import models

# Create your models here.
class timer_table(models.Model):
    time=models.SmallIntegerField(default=0)