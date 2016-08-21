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
	tmp_id=0
	for o in aboutus_data.objects.all():
		tmp_id=o.id
	tmp_row=aboutus_data.objects.get(id=tmp_id)
	json_data={"image":request.scheme+'://'+request.get_host()+'/'+str(tmp_row.image),
	"description":str(tmp_row.description),

	}
	print(str(json_data))
	return (HttpResponse(str(json_data)))