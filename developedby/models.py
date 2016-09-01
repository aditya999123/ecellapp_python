from __future__ import unicode_literals

from django.db import models

# Create your models here.
class developer_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    image=models.CharField(max_length=120,blank=True,null=True)
    name=models.CharField(max_length=120,blank=True,null=True)
    email=models.CharField(max_length=120,blank=True,null=True)
    