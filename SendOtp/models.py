from __future__ import unicode_literals

from django.db import models

class otp_data(models.Model):
    number=models.DecimalField(max_digits=10,decimal_places=0)
    otp=models.PositiveSmallIntegerField(default=0)
    verify=models.PositiveSmallIntegerField(default=0)

class user_data(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    number=models.CharField(max_length=120,blank=True,null=True)
    first_name=models.CharField(max_length=120,blank=True,null=True)
    last_name=models.CharField(max_length=120,blank=True,null=True)
    email=models.CharField(max_length=120,blank=True,null=True)
    college=models.CharField(max_length=120,blank=True,null=True)
    branch=models.CharField(max_length=120,blank=True,null=True)
    sem=models.CharField(max_length=120,blank=True,null=True)

class user_token_data(models.Model):
    id=models.PositiveSmallIntegerField(primary_key='True')
    fcm=models.CharField(max_length=400,blank=True,null=True)
    access_token=models.CharField(max_length=120,blank=True,null=True)

class fcm__not_registered(models.Model):
    fcm=models.CharField(max_length=400,blank=True,null=True)
