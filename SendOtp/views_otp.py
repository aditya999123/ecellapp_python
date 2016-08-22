from django.shortcuts import render
import random
import requests
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def get_otp(request):
	try:
		url='http://api.msg91.com/api/sendhttp.php?authkey=120246AC7mrK6PUjd5794d29c&mobiles='
		name=str(request.POST.get("name"))
		number=str(request.POST.get("mobile"))
		#phno_data = np.loadtxt('phno.csv', delimiter=' ',dtype='str')
		#n = random.random()
		#for o in phno_data:
		#	url+= str(o)+',
		n=random.randint(1000,9999)
		url+=str(number)
		otp=str(n)

		#url+='&message='+'E-Cell team welcomes you. \nVerification code for the app is '+otp
		url+='&message='+'Dear '+name+' \nE-Cell team welcomes you. \nVerification code for the app is '+otp
		url+='&sender=mECell&route=4'
	
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
		response_json={"success":True,"message":"party"}
	except:
		response_json={"success":False,"message":"otp not sent"}
	print str(response_json)
	return HttpResponse(str(response_json))
#@csrf_exempt
@csrf_exempt
def ver_otp(request):
	try:
		firstname=str(request.POST.get("first_name"))
		lastname=str(request.POST.get("last_name"))
		email=str(request.POST.get("email"))
		college=str(request.POST.get("college"))
		branch=str(request.POST.get("branch"))
		sem=str(request.POST.get("semester"))
		number=str(request.POST.get("mobile"))
		otp=str(request.POST.get("otp"))
		fcm=str(request.POST.get("fcm"))
		print"\n"
		print fcm

		print "get method successful"
		print"\n"
		access_token_str=str(random.randint(1000,9999))+number+str(random.randint(1000,9999))
		
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

				user_token_data_list=user_token_data.objects.get(id=user_list.id)
				setattr(user_token_data_list,'fcm',fcm)
				#setattr(user_token_data_list,'access_token',access_token_str)
				user_token_data_list.save()
				access_token_str=str(user_token_data_list.access_token)
				response_json={
				"success":True,
				"message":"successful",
				"access_token":access_token_str,}

			except:
				try:
					fcm__not_registered.objects.get(fcm=fcm).delete()
				except:
					pass
				try:
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
					print "debug=99"
					user_list=user_data.objects.get(number=number)
					print "debug=101"

					#print"\nerror in getting id\n"
					user_token_data.objects.create(
						id=user_list.id,
						fcm=fcm,
						access_token=access_token_str)
					print"debug=108"
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
	print str(response_json)
	return HttpResponse(str(response_json))
from Splash_Screen.models import version_control
@csrf_exempt
def send_fcm(request):
	version=version_control.objects.all()[0].app_version
	if(request.method=='POST'):
		try:
			fcm=str(request.POST.get("fcm"))
			if fcm!=None:

				print "fcm recived:"+fcm
				try:
					fcm_list=user_data.objects.get(fcm=fcm)
					response_json={"success":True,
					"version":int(version),
					"message":"already added"}
				except:
					try:
						fcm_list=fcm__not_registered.objects.get(fcm=fcm)
						response_json={"success":True,
						"version":int(version),
						"message":"already added"}
					except:
						fcm__not_registered.objects.create(fcm=fcm)
						response_json={"success":True,
						"version":int(version),
						"message":"successfully added"}
			else:
				response_json={"success":False,
				"version":int(version),
				"message":"fcm none recieved"}

		except:
			response_json={"success":False,
			"version":int(version),
			"message":"send fcm : invalid parameters"}

	else:
		response_json={"success":False,
				"message":"not post method"}
	print str(response_json)
	return HttpResponse(str(response_json))

def initial(request):
	return HttpResponse("<a href=./login>admin_login</a>")
