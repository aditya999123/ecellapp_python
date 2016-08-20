from django.shortcuts import render
#import random
#import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import render_to_response, render
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def feed(request):
	data="{'aboutus':["
	for o in aboutus_data.objects.all():
		data+="{"+"'id':'"+str(o.id)+"',"
		data+="'image':'"+str(o.image)+"',"
		data+="'description':'"+str(o.description)+"',"
		data+="},"
	if (aboutus_data.objects.count())>0:
		json_data=data[:-1]
	else:
		json_data=data
	json_data+="]}"
	return (HttpResponse(json_data))