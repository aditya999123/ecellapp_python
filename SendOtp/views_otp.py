from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def get_otp(request,name,number):
	url='https://control.msg91.com/api/sendhttp.php?authkey=120246AC7mrK6PUjd5794d29c&mobiles='
	
	#phno_data = np.loadtxt('phno.csv', delimiter=' ',dtype='str')
	#n = random.random()
	#for o in phno_data:
	#	url+= str(o)+',
	n=random.random()#'
	url+=str(number)
	url+='&message='+'hello '+str(name)+' your otp for ecell app  is '+str(int(n*10000))
	url+='&sender=AdiCse&route=4'
	result_json = requests.request('GET', url)
	return HttpResponse("{'success':1}")

def initial(requests):
	return HttpResponse("under construction")