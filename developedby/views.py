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
	data='{"spons":['
	for o in spons_data.objects.all():
		data+='{'+'"id":"'+str(o.id)+'",'
		data+='"image":"'+request.scheme+'://'+request.get_host()+'/'+str(o.image1)+'",'
		data+='"name":"'+str(o.name)+'",'
		data+='"email":"'+str(o.image1)+'"'
		data+='},'
	if (developer_data.objects.count())>0:
		json_data=data[:-1]
	else:
		json_data=data
	json_data+="]}"
	return (HttpResponse(json_data))