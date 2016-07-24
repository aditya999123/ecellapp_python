from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def get_version(request):
	json='{"sucess":true}'
	return HttpResponse(json)