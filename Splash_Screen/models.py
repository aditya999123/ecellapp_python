from __future__ import unicode_literals

from django.db import models
#from django_mysql import models
class version_control(models.Model):
	app_version=models.PositiveSmallIntegerField()
	compulsary_update=models.PositiveSmallIntegerField()
	#def __str__(self):
	#	return self.app_version
# Create your models here.
