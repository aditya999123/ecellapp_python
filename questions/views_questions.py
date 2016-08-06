from django.shortcuts import render
import multiprocessing as mp
import time
import requests
from django.http import HttpResponseRedirect, HttpResponse
from .models import timer_table
from SendOtp.models import user_data,user_token_data
# Create your views here.
def question(request):
	timer_query=timer_table.objects.all()
	timer=timer_query[0]

	if(timer.time!=0):
		json={"time":timer.time,
		"question":" ",
		"question_no":0,
		"option1":" ",
		"option2":" ",
		"option3":" ",
		"option4":" ",
		"message":"the 1st round of bquiz",
		}
	if(timer.time==0):
		json={"time":timer.time,
		"question":"question1",
		"question_no":1,
		"option1":"a",
		"option2":"b",
		"option3":"c",
		"option4":"d",
		"message":"the",
		}
	return HttpResponse(str(json))


def send_notification(request,data):
	user_list=user_data.objects.all()
	url="https://fcm.googleapis.com/fcm/send"
	headers={
	'Content-Type':'application/json',
	"Authorization":"key=AIzaSyCmRDiB2zoKvbeiMTgVQXVs-o86tJ3AH04"
	}
	for o in user_list:
		print o.fcm
		json=  {"to" : o.fcm,
		"notification" : {
		"body" : data,
		"title" : "ECell-BQuiz",}}
		print json
		result=requests.request('POST', url,headers=headers,json=json)
      	print result

      	
 	return HttpResponse('{"success":"1"}')
