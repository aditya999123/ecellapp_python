from __future__ import unicode_literals
from django.db import models

class aboutus_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    image=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=1000,blank=True,null=True)