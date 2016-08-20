from django.shortcuts import render
#import random
#import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import render_to_response, render
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib.sites.models import Site
# Create your views here.
def feed(request):
	data='{"contacts":['
	for o in contactus_data.objects.all():
		data+='{'+'"id":"'+str(o.id)+'",'
		data+='"name":"'+str(o.name)+'",'
		data+='"designation":"'+str(o.designation)+'",'
		data+='"email":"'+str(o.email)+'",'
		data+='"phone":"'+str(o.phone)+'",'
		data+='"image":"'+request.scheme+'://'+request.get_host()+'/'+str(o.image)+'"'
		data+='},'
	if (contactus_data.objects.count())>0:
		json_data=data[:-1]
	else:
		json_data=data
	json_data+="]}"
	#json_data+=request.build_absolute_uri()
	#json_data+="\n\n"+request.scheme+"://"+request.get_host()+"/"
	return (HttpResponse(json_data))