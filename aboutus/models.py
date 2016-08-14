from __future__ import unicode_literals
from django.db import models

class user_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    image=models.CharField(max_length=120,blank=True,null=True)
    description=models.CharField(max_length=120,blank=True,null=True)
    last_name=models.CharField(max_length=120,blank=True,null=True)
    email=models.CharField(max_length=120,blank=True,null=True)
    college=models.CharField(max_length=120,blank=True,null=True)
    branch=models.CharField(max_length=120,blank=True,null=True)
    sem=models.CharField(max_length=120,blank=True,null=True)

# Create your models here.
