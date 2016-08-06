from django.contrib import admin

from .models import otp_data,user_data,user_token_data,fcm__not_registered
class otp_dataAdmin(admin.ModelAdmin):
    list_display=["number","otp"]
admin.site.register(otp_data,otp_dataAdmin)

class user_dataAdmin(admin.ModelAdmin):
    list_display=["first_name","number"]
admin.site.register(user_data,user_dataAdmin)

class user_token_data_dataAdmin(admin.ModelAdmin):
    list_display=["id","fcm"]
admin.site.register(user_token_data,user_token_data_dataAdmin)
class fcm__not_registeredAdmin(admin.ModelAdmin):
    list_display=["fcm"]
admin.site.register(fcm__not_registered,fcm__not_registeredAdmin)
# Register your models here.
