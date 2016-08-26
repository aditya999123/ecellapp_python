from __future__ import unicode_literals

from django.db import models

# Create your models here.
class questions(models.Model):
	question_id=models.SmallIntegerField(default=-10)
	quiz_id=models.SmallIntegerField(default=0)
	question=models.CharField(max_length=1000,blank=True,null=True)
	question_type=models.SmallIntegerField(default=-10)
	duration=models.SmallIntegerField(default=120)
	option1=models.CharField(max_length=120,blank=True,null=True)
	option2=models.CharField(max_length=120,blank=True,null=True)
	option3=models.CharField(max_length=120,blank=True,null=True)
	option4=models.CharField(max_length=120,blank=True,null=True)
	image_url=models.CharField(max_length=120,blank=True,null=True)
	points=models.CharField(max_length=120,blank=True,null=True)
	ans=models.CharField(max_length=120,blank=True,null=True)

class user_response(models.Model):
    response_id= models.AutoField(primary_key=True)
    question_id=models.PositiveSmallIntegerField()
    user_id=models.PositiveSmallIntegerField()
    quiz_id=models.PositiveSmallIntegerField()
    response=models.CharField(max_length=120,blank=True,null=True)
class rules(models.Model):
    question_id=models.PositiveSmallIntegerField()
    rules=models.CharField(max_length=120,blank=True,null=True)
class current(models.Model):
	message=models.CharField(max_length=120,blank=True,null=True)
	value=models.SmallIntegerField(default=0)
	tag=models.CharField(max_length=120,blank=True,null=True)