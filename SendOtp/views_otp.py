from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
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
		response_json={"success":True}
	except:
		response_json={"success":False}
	
	return HttpResponse(str(response_json))
def ver_otp(request,firstname,lastname,email,college,branch,sem,number,otp,fcm):
	access_token_str=str(random.randint(1000,9999))+number+str(random.randint(1000,9999))
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
				#setattr(user_list,'access_token',access_token)
				user_list.save()

				user_token_data_list=user_token_data.get(id=user_list.id)
				setattr(user_token_data_list,'fcm',fcm)
				setattr(user_token_data_list,'access_token',access_token_str)

			except:
				try:
					fcm_initial_list=fcm__not_registered.objects.get(fcm=fcm)
					fcm_initial_list.delete()
					user_data.objects.create(
						first_name=firstname,
						last_name=lastname,
						email=email,
						number=number,
						college=college,
						branch=branch,
						sem=sem,
						#access_token=access_token
						)

					user_token_data.create(
						id=user_data.objects.all().reverse()[0].id,
						fcm=fcm,
						access_token=access_token_str)
					response_json={
					"success":True,
					"message":"successful",
					"access_token":access_token_str,
					}
				except:
					response_json={
					"success":False,
					"message":"fcm not found in table",
					"access_token":access_token_str,
					}

			#return HttpResponse(str(response_json))
		else:
			#return HttpResponse('{"status":"not_verified"}')
			response_json={
			"success":False,
			"message":"not verified otp did not match",
			"access_token":"NULL",
			}

	except:
		response_json={
			"success":False,
			"message":"number does not exsist",
			"access_token":"NULL",
			}
	return HttpResponse(str(response_json))
@csrf_exempt
def send_fcm(request):
	if(request.method=='POST'):
		try:
			fcm=str(request.POST.get("fcm"))
			print "fcm recived:"+fcm
			try:
				fcm_list=fcm__not_registered.objects.get(fcm=fcm)
				response_json={"success":True,
				"message":"already added"}
			except:
				fcm__not_registered.objects.create(fcm=fcm)
				response_json={"success":True,
				"message":"successfully added"}
		except:
			response_json={"success":False,
				"message":"send fcm : invalid parameters"}

	else:
		response_json={"success":False,
				"message":"not post method"}		
	return HttpResponse(str(response_json))

def initial(request):
	return HttpResponse("under construction_iket")
