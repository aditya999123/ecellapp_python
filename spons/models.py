from __future__ import unicode_literals

from django.db import models

# Create your models here.
class spons_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    image1=models.CharField(max_length=120,blank=True,null=True)
    image2=models.CharField(max_length=120,blank=True,null=True)