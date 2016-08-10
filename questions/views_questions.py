from django.shortcuts import render
import multiprocessing as mp
import time
import requests
from django.http import HttpResponseRedirect, HttpResponse
from SendOtp.models import user_data,user_token_data,fcm__not_registered
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from .models import questions,user_response

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
flag_timer=0
current_question=-1
current_quiz_id=0
#current que 0 for wait for next ques
#current que -1 for quiz not started
#current que -2 the quiz has ended
def fun():
	pass
def question_get(request):
	str_access_token=request.GET.get("access_token")
	try:
		access_token_queries=user_token_data.objects.get(access_token=str_access_token)
		if current_question==-1:
			response_json={
			"success":False,
			"message":"quiz not started",
			"message_image_url":"NULL",
			"data_type":-1,
			"question_data":{"question":"NULL",
			"option1":"NULL",
			"option2":"NULL",
			"option3":"NULL",
			"option4":"NULL",
			"image_url":"NULL",
			"question_duration":0,}
			}
		
		elif current_question==0:
			response_json={
			"success":False,
			"message":"pls wait for next question",
			"message_image_url":"NULL",
			"data_type":-1,
			"question_data":{"question":"NULL",
			"option1":"NULL",
			"option2":"NULL",
			"option3":"NULL",
			"option4":"NULL",
			"image_url":"NULL",
			"question_duration":0,}
			}
		else:
			try:
				question_queries=questions.objects.get(question_id=current_question)
				response_json={
				"success":True,
				"message":"question found and served",
				"message_image_url":"NULL",
				"data_type":int(question_queries.question_type),
				"question_data":{"question":str(question_queries.question),
				"option1":str(question_queries.option1),
				"option2":str(question_queries.option2),
				"option3":str(question_queries.option3),
				"option4":str(question_queries.option4),
				"image_url":str(question_queries.image_url),
				"question_duration":str(question_queries.duration),}
				}
			except:
				response_json={
				"success":False,
				"message":"question with id"+str(current_question)+" not found",
				"message_image_url":"NULL",
				"data_type":0,
				"question_data":{"question":"NULL",
				"option1":"NULL",
				"option2":"NULL",
				"option3":"NULL",
				"option4":"NULL",
				"image_url":"NULL",
				"question_duration":0,}
				}
	except:
		response_json={
				"success":False,
				"message":"access token did not match",
				"message_image_url":"NULL",
				"data_type":0,
				"question_data":{"question":"NULL",
				"option1":"NULL",
				"option2":"NULL",
				"option3":"NULL",
				"option4":"NULL",
				"image_url":"NULL",
				"question_duration":0,}
				}
	return HttpResponse(str(response_json))
@csrf_protect
def admin_panel(request):
	variables = RequestContext(request)
	if request.method=="GET":
		pass
		
	if request.method=="POST":
		if request.POST.get("send")=='SEND':
			#print"adddddddddddddddddddddddddddddddddddddddddddd"

			print str(request.POST.get("title"))+str(request.POST.get("data"))
			send_notification(request.POST.get("title"),request.POST.get("data"))

		if request.POST.get("question_set")=='QUESTION_SET':
			print"debug 109"
			global current_question
			if request.POST.get("question_id")=="":
				print"debug 112"
				current_question=0
			else:
				current_question=int(request.POST.get("question_id"))
				print "question activated:" +str(current_question)
		
	return render_to_response('admin_panel.html',variables)
#@csrf_protect
def send_notification(title,data):
	user_list=user_token_data.objects.all()
	try:
		user_list.append(fcm__not_registered.objects.all())
	except:
		pass
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	'Content-Type':'application/json',
	"Authorization":"key=AIzaSyCmRDiB2zoKvbeiMTgVQXVs-o86tJ3AH04"
	}
	for o in user_list:
		print o.fcm
		json=  {"to" : o.fcm,
		"notification" : {
		"body" : str(data),
		"title" : str(title),}}
		print json
		print requests.request('POST', url,headers=headers,json=json)

@csrf_exempt
def send_ans(request):
	if (request.method=='GET'):
		pass
	if(request.method)=='POST':
		if(current_question==-1):
			response_json={
			"success":False,
			"message":"quiz has not started",
			}
		if(current_question>=0):
			question_id_user=int(str(request.POST.get("question_id")))
			user_access_token=str(request.POST.get("access_token"))
			global current_quiz_id
			try:
				user_id=user_token_data.objects.get(access_token=user_access_token)[0].id
				try:
					user_response_list=user_response.objects.get(
						quiz_id=current_quiz_id,
						user_id=user_id,
						question_id=question_id_user,
						)
					response_json={
					"success":False,
					"message":"response already registered",
					"message_image":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Fluorite-270246.jpg",
					"message_display":"your response for this question has already been submitted",
					}
				except:
					user_response.objects.create(
						quiz_id=current_quiz_id,
						user_id=user_id,
						question_id=question_id_user,
						response=str(request.POST.get("response"))
						)
					response_json={
					"success":True,
					"message_image":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Fluorite-270246.jpg",
					"message_display":"your response has been successfuly submitted",
					"message":"response successfuly registered",
					}
			except:
				response_json={
					"success":False,
					"message":"access token not found",
					"message_image":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Fluorite-270246.jpg",
					"message_display":"pls register again",
					}
	return HttpResponse(str(response_json))