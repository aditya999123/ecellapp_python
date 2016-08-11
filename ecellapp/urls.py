"""ecellapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Splash_Screen import views_splash_screen
from SendOtp import views_otp
from questions import views_questions
urlpatterns = [
	#url(r'^',views_otp.initial,name='intial'),
    url(r'^$',views_otp.initial,name='start'),
    url(r'^check_version',views_splash_screen.get_version),
    url(r'^admin/', admin.site.urls),
    url(r'^get_otp/$',views_otp.get_otp, name = 'otp'),
    url(r'^send_fcm/$',views_otp.send_fcm, name = 'fcm'),
    url(r'^ver_otp/$',views_otp.ver_otp, name = 'otp_ver'), 
    url(r'^get_ques/$',views_questions.question_get, name = 'get_ques'),
    url(r'^admin_panel/$',views_questions.admin_panel, name = 'admin_panel'),
    url(r'^send_ans/$',views_questions.send_ans, name = 'send_ans'),
    #url(r'^ques_trigger/$',views_questions.question, name = 'ques_trigger'),

#    url(r'^timer_trigger/(?P<time_set>.+)/$',views_questions.trigger, name = 'trigger'),


]
