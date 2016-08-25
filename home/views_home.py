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
	data="{"
	data+='"success":'+str(True)+','
	
	data+='"homeDetailsList":['
	for o in home_data.objects.all():
		data+='{'+'"title":"'+str(o.title)+'",'
		data+='"discription":"'+str(o.description)+'",'
		data+='"type":'+str(o.data_type)+","
		data+='"timestamp":"'+str(o.date)+'",'
		data+='"owner":"'+str(o.owner)+'",'
		data+='"image":"'+request.scheme+"://"+request.get_host()+"/"+str(o.image)+'"'
		data+='},'
	if (home_data.objects.count())>0:
		json_data=data[:-1]
	else:
		json_data=data
	json_data+="]}"
	return (HttpResponse(json_data))
