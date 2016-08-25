from __future__ import unicode_literals

from django.db import models

# Create your models here.
class home_data(models.Model):
    id=models.SmallIntegerField(default=0,primary_key=True)
    image=models.CharField(max_length=120,blank=True,null=True)
    description=models.CharField(max_length=1200,blank=True,null=True)
    date=models.CharField(max_length=120,blank=True,null=True)
    data_type=models.SmallIntegerField(default=0)
    owner=models.CharField(max_length=120,blank=True,null=True)
    title=models.CharField(max_length=120,blank=True,null=True)
'''
private int type;
   private List<String> viewPagerImageList;
   private String title;
   private String discription;
   private String image;
   private String url;
   private String timestamp;
   private String owner;
'''