from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
# Create your views here.
def get_otp(request,name,number):
	url='http://api.msg91.com/api/sendhttp.php?authkey=120246AC7mrK6PUjd5794d29c&mobiles='
	
	#phno_data = np.loadtxt('phno.csv', delimiter=' ',dtype='str')
	#n = random.random()
	#for o in phno_data:
	#	url+= str(o)+',
	n=random.randint(1000,9999)
	url+=str(number)
	otp=str(n)

	url+='&message='+'hello '+str(name)+' your otp for ecell app  is '+otp
	url+='&sender=mECell&route=4'
	try:
		result = requests.request('GET', url)

		try:
			otp_list=otp_data.objects.get(number=number)
			setattr(otp_list,'otp',int(otp))
			otp_list.save()
		except:
			otp_data.objects.create(number=number,otp=int(otp))
	# for o in otp_queries:
	# 	print o.number
	# 	if(number == o.number):
	# 		otp_queries.otp=int(otp)
	# 		otp_data.objects.create(number=number,otp=int(otp))
	#
		return HttpResponse('{"success":"1"}')
	except:
		return HttpResponse('{"success":"0"}')
def ver_otp(request,firstname,lastname,email,college,branch,sem,number,otp,fcm):
	try:
		otp_list=otp_data.objects.get(number=number)
		if otp_list.otp==int(otp):
			setattr(otp_list,'verify',int(1))
			otp_list.save()
			try:
				user_list=user_data.objects.get(number=number)
				setattr(user_list,'first_name',firstname)
				setattr(user_list,'last_name',lastname)
				setattr(user_list,'email',email)
				setattr(user_list,'college',college)
				setattr(user_list,'branch',branch)
				setattr(user_list,'sem',sem)
				setattr(user_list,'number',number)
				
				setattr(user_list,'fcm',fcm)
				#setattr(user_list,'access_token',access_token)
				user_list.save()
			except:
				user_data.objects.create(
					first_name=firstname,
					last_name=lastname,
					email=email,
					number=number,
					college=college,
					branch=branch,
					sem=sem,
					#access_token=access_token,
					fcm=fcm
					)
			return HttpResponse('{"status":"verified"}')
		else:
			return HttpResponse('{"status":"not_verified"}')
	except:
		return HttpResponse('{"status":"error"}')

def send_fcm(request,fcm):
	try:
		fcm_list=gcm_data.objects.get(fcm=fcm)
	except:
		fcm_data.create(fcm=fcm)

def send_notification(request,data):
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	'Content-Type':'application/json',
	"Authorization":"key=AIzaSyCmRDiB2zoKvbeiMTgVQXVs-o86tJ3AH04"
	}
	json={"to" : "fxkdtNoFIT8:APA91bFwBy4plm32o8gOp9TvSMRdBSpDFl7DIiqnVBMh2DWOSteCw_hqHKymRzRj50te5eNZ2T7LjhvCtGbqOuEuvPA4IMAVJMQsi4BscTBr3vq9jFiisP-HiK-Y8F4uktvm5e7XlWM7",
	"notification" : {"body" : "iket_madarchod","title" : "asd",},
	"delay_while_idle":True,
	"priority" : "high",

    }


	
 	result = requests.request('POST', url,headers=headers,json=json)
 	return HttpResponse(result)
def initial(request):
	return HttpResponse("under construction_iket")
