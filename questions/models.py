from __future__ import unicode_literals

from django.db import models

# Create your models here.
class timer_table(models.Model):
    time=models.SmallIntegerField(default=0)
    
class question(models.Model):
	question_id=models.SmallIntegerField(default=-10)
	
	question=models.CharField(max_length=120,blank=True,null=True)
	question_type=models.SmallIntegerField(default=-10)
	duration=models.SmallIntegerField(default=120)
	option1=models.CharField(max_length=120,blank=True,null=True)
	option2=models.CharField(max_length=120,blank=True,null=True)
	option3=models.CharField(max_length=120,blank=True,null=True)
	option4=models.CharField(max_length=120,blank=True,null=True)
	image_url=models.CharField(max_length=120,blank=True,null=True)
	ans=models.CharField(max_length=120,blank=True,null=True)