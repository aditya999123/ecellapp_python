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
		return HttpResponse('{"success":"1"}')
	except:
		return HttpResponse('{"success":"0"}')
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

			except:
				try:
					fcm_initial_list=fcm__not_registered.objects.get(fcm=fcm)
					fcm_initial_list.delete()
				except:
					pass
				number_user_no=user_data.objects.count()
				if number_user_no == None:
					number_user= 1
        		else:
        			number_user= number_user_no + 1
				user_token_data.create(
					id=number_user,
					fcm=fcm,
					access_token=access_token_str)
				user_data.objects.create(
					id=number_user,
					first_name=firstname,
					last_name=lastname,
					email=email,
					number=number,
					college=college,
					branch=branch,
					sem=sem,
					#access_token=access_token
					)
			response_json={
			"status":"verified",
			"access_token":access_token_str
			}
			return HttpResponse(str(response_json))
		else:
			return HttpResponse('{"status":"not_verified"}')
	except:
		return HttpResponse('{"status":"error"}')
@csrf_exempt
def send_fcm(request):
	if(request.method=='POST'):
		try:
			fcm=str(request.POST.get("fcm"))
			print "fcm======================"+fcm
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
