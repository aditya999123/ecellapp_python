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
	data="{'blogs':["
	for o in blogs_data.objects.all():
		data+="{"+"'blogId':'"+str(o.id)+"',"
		data+="'blogTitle':'"+str(o.title)+"',"
		data+="'blogDate':'"+str(o.date)+"',"
		data+="'blogOwner':'"+str(o.owner)+"',"
		data+="'blogCategory':'"+str(o.category)+"',"
		data+="'blogImage':'"+request.scheme+'://'+request.get_host()+'/'+str(o.image)+'"'
		data+="'blogBody':'"+str(o.body)+"',"
		data+="'image':'"+str(o.image)+"',"
		data+="'blogTime':'"+str(o.time)+"',"
		data+="},"
	if (blogs_data.objects.count())>0:
		json_data=data[:-1]
	else:
		json_data=data
	json_data+="]}"
	return (HttpResponse(json_data))