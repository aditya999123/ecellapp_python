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
from aboutus import views_aboutus
from blogs import views_blogs
from contactus import views_contactus
from esummit import views_esummit
from events_app import views_events
from home import views_home
from spons import views_spons
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	#url(r'^',views_otp.initial,name='intial'),
    url(r'^$',views_otp.initial,name='start'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve'),
    url(r'^admin/', admin.site.urls),
    url(r'^get_otp/$',views_otp.get_otp, name = 'otp'),
    url(r'^send_fcm/$',views_otp.send_fcm, name = 'fcm'),
    url(r'^ver_otp/$',views_otp.ver_otp, name = 'otp_ver'), 
    url(r'^get_ques/$',views_questions.question_get, name = 'get_ques'),
    url(r'^admin_panel/$',views_questions.admin_panel, name = 'admin_panel'),
    url(r'^send_ans/$',views_questions.send_ans, name = 'send_ans'),
    #url(r'^test/$',views_questions.test, name = 'test'),
    url(r'^aboutus/$',views_aboutus.feed, name = 'about_us_feed'),
    url(r'^blogs/$',views_blogs.feed, name = 'views_blogs_feed'),
    url(r'^contactus/$',views_contactus.feed, name = 'views_contactus_feed'),
    url(r'^esummit/$',views_esummit.feed, name = 'views_esummit_feed'),
    url(r'^events/$',views_events.feed, name = 'views_events_feed'),
    #events registration to be included afterwards
    url(r'^home/$',views_home.feed, name = 'views_home_feed'),
    url(r'^spons/',views_spons.feed, name = 'views_spons_feed'),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)