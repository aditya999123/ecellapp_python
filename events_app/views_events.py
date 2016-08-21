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
	data='{"events":['
	for o in events_data.objects.all():
		data+='{'+'"id":"'+str(o.id)+'",'
		data+='"name":"'+str(o.event_name)+'",'
		data+='"description":"'+str(o.description)+'",'
		data+='"rules":"'+str(o.rules)+'",'
		data+='"date":"'+str(o.date)+'",'
		data+='"venue":"'+str(o.venue)+'",'
		data+='"image":"'+request.scheme+'://'+request.get_host()+'/'+str(o.image)+'"'
		data+='},'
	if (events_data.objects.count())>0:
		json_data=data[:-1]
	else:
		json_data=data
	json_data+="]}"
	return (HttpResponse(json_data))