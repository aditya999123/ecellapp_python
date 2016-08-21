from __future__ import unicode_literals

from django.db import models

# Create your models here.
class events_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    image=models.CharField(max_length=120,blank=True,null=True)
    description=models.CharField(max_length=1200,blank=True,null=True)
    event_name=models.CharField(max_length=120,blank=True,null=True)
    rules=models.CharField(max_length=120,blank=True,null=True)
    date=models.CharField(max_length=120,blank=True,null=True)
    venue=models.CharField(max_length=120,blank=True,null=True)