from django.shortcuts import render
import multiprocessing as mp
import time
import requests
from django.http import HttpResponseRedirect, HttpResponse
from SendOtp.models import user_data,user_token_data,fcm__not_registered
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from .models import questions,user_response,rules,current
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
import multiprocessing as mp
# Create your views here.
flag_timer=0

#current que 0 for wait for next ques
#current que -1 for quiz not started
#current que -2 the quiz has ended
@login_required
def logout_page(request):
    logout(request)
    return HttpResponse("you have succesfully logged out")
def question_get(request):

	current_question=current.objects.get(tag="current_question").value
	message=str(current.objects.get(tag="current_question").message)
	print "get question id"+str(current_question)
	current_quiz_id=current.objects.get(tag="current_quiz_id").value
	str_access_token=str(request.GET.get("access_token"))
	print "ACCESS TOKEN RECIVED:"+str_access_token
	try:
		user_list=user_token_data.objects.get(access_token=str_access_token)
		try:
			user_id=user_list.id
			print"\n\n\n\n\n\n\n\n\n\n\n"
			print"command reached here"
			user_response_list=user_response.objects.get(
				quiz_id=current_quiz_id,
				user_id=user_id,
				question_id=current_question,
				)
			response_json={
				"success":False,
				"message":"response already submitted",
				"message_image_url":request.scheme+'://'+request.get_host()+'/'+"media/general/timer_wait.jpg",
				}

			print"\n\n\n\n\n\n\n\n\n\n\n"
			print"command reached here too"
		except:
			if current_question==-1:
				response_json={
				"success":False,
				"message":message,
				"message_image_url":request.scheme+'://'+request.get_host()+'/'+"media/general/timer_wait.jpg",
				}
			elif current_question==0:
				response_json={
				"success":False,
				"message":"pls wait for next question",
				"message_image_url":request.scheme+'://'+request.get_host()+'/'+"media/general/timer.png",
				}
			else:
				#print "\n\n\n\debug:45\n\n\n"
				try:
					question_queries=questions.objects.get(question_id=current_question,quiz_id=current_quiz_id)
					rules_queries=rules.objects.filter(question_id=current_question)
					rules_str=""
					tmp=1
					for o in rules_queries:
						rules_str+=str(tmp)+") "+str(o.rules)
						rules_str+="\n"
						tmp+=1
					response_json={
					"success":True,
					"message":"question found and served",
					"message_image_url":"NULL",
					"data_type":int(question_queries.question_type),
					"question_data":{"question":str(question_queries.question),
					"question_id":int(question_queries.question_id),
					"option1":str(question_queries.option1),
					"option2":str(question_queries.option2),
					"option3":str(question_queries.option3),
					"option4":str(question_queries.option4),
					"points":str(question_queries.points),
					"image_url":request.scheme+'://'+request.get_host()+'/'+str(question_queries.image_url),
					"question_duration":str(question_queries.duration),},
					"rules":rules_str,
					}
					print "json ended"
					#"rules":[str(o.rules) for o in rules_queries]}
				except:
					response_json={
					"success":False,
					"message":"question with id"+str(current_question)+" not found or rules not found",
					"message_image_url":request.scheme+'://'+request.get_host()+'/'+"media/general/error.png",
					}
	except:
		response_json={
				"success":False,
				"message":"(Technical Error)\n\nPlease logout & register again\nSorry for the inconvenience caused",
				"message_image_url":request.scheme+'://'+request.get_host()+'/'+"media/general/error.png",
				}
	print str(response_json)
	return HttpResponse(str(response_json))
@login_required
@csrf_protect
def admin_panel(request):
	current_question=0
	current_quiz=0
	variables = RequestContext(request)
	if request.method=="GET":
		pass

	if request.method=="POST":
		if request.POST.get("send")=='SEND':
			#print"adddddddddddddddddddddddddddddddddddddddddddd"

			print str(request.POST.get("title"))+str(request.POST.get("data"))
			intent_id=request.POST.get("intent_id")
			if intent_id=="":
				intent_id=0
			print "////////////////////////////////////////////"+mp.current_process().name
			p1=mp.Process(name='MainProcess',target=send_notification,args=(request.POST.get("title"),request.POST.get("data"),intent_id))
			p1.start()

		if request.POST.get("question_set")=='QUESTION_SET':
			current_question_queries=current.objects.get(tag="current_question")
			print"debug 84"
			#global current_question
			if request.POST.get("question_id")=="":
				print"debug 87"
				current_question=0
			else:
				current_question=int(request.POST.get("question_id"))
				print "question activated:" +str(current_question)
			setattr(current_question_queries,'value',current_question)
			current_question_queries.save()
		if request.POST.get("quiz_set")=='QUIZ_SET':
			current_quiz_id_queries=current.objects.get(tag="current_quiz_id")
			print"debug 93"
			#global current_quiz_id
			if request.POST.get("quiz_id")=="":
				print"debug 96"
				current_quiz_id=0
			else:
				current_quiz_id=int(request.POST.get("quiz_id"))
				print "quiz activated:" +str(current_quiz_id)
			setattr(current_quiz_id_queries,'value',current_quiz_id)
			current_quiz_id_queries.save()
	return render_to_response('admin_panel.html',variables)
#@csrf_protect
def send_notification_request(intent_id,data_body,title,fcm_list):
	print "called"
	#fvR0TS--jv0:APA91bHEHaU7gXqO8_SFqC2ybF0Mkirna0RfiYKNfouB0hN0rnlOLztvDGFRnUHWC7X1sgKcadrEuLTammB1KGHzfYMnxGqrjwqzMPcXmJMt-3LE6iQgzXLm306JYewZjXE8zSEyFDBK
	for o in fcm_list:
		json= {
		"to" :str(o),
		"data":{
		"intent_id":int(intent_id),
		"body" :'"'+str(data_body)+'"',
		"title" :'"'+str(title)+'"',
		},
		}
		print json
		url="https://fcm.googleapis.com/fcm/send"
		headers={
		'Content-Type':'application/json',
		"Authorization":"key=AIzaSyCmRDiB2zoKvbeiMTgVQXVs-o86tJ3AH04"
		}
		#print json
		print requests.request('POST', url,headers=headers,json=json)
import time
def send_notification(title,data_body,intent_id=0):
	print"//////////////////////////////////////////\n\n\n\n\n"

	user_fcm_list=[]
	for o in user_token_data.objects.all():
		if str(o.fcm) not in user_fcm_list:
			user_fcm_list.append(str(o.fcm))
	for o in fcm__not_registered.objects.all():
		if str(o.fcm) not in user_fcm_list:
			user_fcm_list.append(str(o.fcm))
	list_number=len(user_fcm_list)
	for iterator in range(30,list_number,31):
		print iterator-30,iterator
		p1=mp.Process(name='notification_mp',target=send_notification_request,args=(intent_id,data_body,title,user_fcm_list[iterator-30:iterator]))
		p1.start()
		time.sleep(1)

@csrf_exempt
def send_ans(request):
	current_question=current.objects.get(tag="current_question").value
	current_quiz_id=current.objects.get(tag="current_quiz_id").value
	if (request.method=='GET'):
		response_json={
					"success":False,
					"message":"not post method",
					"message_image":request.scheme+'://'+request.get_host()+'/'+"media/general/error.png",
					"message_display":"Please Start the quiz again",

					}
	if(request.method)=='POST':
		if(current_question==-1):
			response_json={
			"success":False,
			"message":"quiz has not started",
			"message_image":request.scheme+'://'+request.get_host()+'/'+"media/general/timer_wait.jpg",
			"message_display":"Please Wait quiz hasnt started",
			}
		if(current_question>=0):
			question_id_user=int(str(request.POST.get("question_id")))
			user_access_token=str(request.POST.get("access_token"))
			print "access_token recived:"+user_access_token
			global current_quiz_id
			try:
				user_list=user_token_data.objects.get(access_token=user_access_token)
				print "access_token recived:"+user_access_token

				user_id=user_list.id
				try:
					user_response_list=user_response.objects.get(
						quiz_id=current_quiz_id,
						user_id=user_id,
						question_id=question_id_user,
						)
					response_json={
					"success":False,
					"message":"response already registered",
					"message_image":request.scheme+'://'+request.get_host()+'/'+"media/general/error.png",
					"message_display":"Your response for this question has already been submitted",
					}
				except:
					user_response.objects.create(
						quiz_id=current_quiz_id,
						user_id=user_id,
						question_id=question_id_user,
						response=str(request.POST.get("answer"))
						)
					response_json={
					"success":True,
					"message_image":request.scheme+'://'+request.get_host()+'/'+"media/general/thumbsup.png",
					"message":"Response Successfuly Registered",
					"message_display":"Response Successfuly Registered",


					}
			except:
				response_json={
					"success":False,
					"message_image":request.scheme+'://'+request.get_host()+'/'+"media/general/error.png",
					"message":"access_token did not match",
					"message_display":"Pls clear Data of the app and register again",
					}
	print str(response_json)
	return HttpResponse(str(response_json))
def test(request):
	rules_queries=rules.objects.filter(question_id=current_question)
	#response_json={"rules":[str(o.rules) for o in rules_queries]}
	rules_str=""
	for o in rules_queries:
		rules_str+=str(o.rules)
		rules_str+="\n"
	response_json={"rules":rules_str}
	return HttpResponse(str(response_json))