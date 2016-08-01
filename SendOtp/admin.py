from django.contrib import admin

from .models import otp_data,user_data,fcm_data
class otp_dataAdmin(admin.ModelAdmin):
    list_display=["number","otp"]
admin.site.register(otp_data,otp_dataAdmin)

class user_dataAdmin(admin.ModelAdmin):
    list_display=["first_name","number"]
admin.site.register(user_data,user_dataAdmin)

class fcm_dataAdmin(admin.ModelAdmin):
    list_display=["fcm"]
admin.site.register(fcm_data,fcm_dataAdmin)
# Register your models here.
