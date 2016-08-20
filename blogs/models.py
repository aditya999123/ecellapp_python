from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blogs_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    image=models.CharField(max_length=120,blank=True,null=True)
    body=models.CharField(max_length=120,blank=True,null=True)
    title=models.CharField(max_length=120,blank=True,null=True)
    category=models.CharField(max_length=120,blank=True,null=True)
    date=models.CharField(max_length=120,blank=True,null=True)
    owner=models.CharField(max_length=120,blank=True,null=True)
    time=models.CharField(max_length=120,blank=True,null=True)