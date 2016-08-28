from django.contrib import admin
from .models import questions,user_response,rules,current
# Register your models here.
# class timerAdmin(admin.ModelAdmin):
#     list_display=["time"]
# admin.site.register(timer_table,timerAdmin)

class questionsAdmin(admin.ModelAdmin):
    list_display=["question","question_id","question_type"]
admin.site.register(questions,questionsAdmin)

class user_responseAdmin(admin.ModelAdmin):
    list_display=["user_id","quiz_id"]
admin.site.register(user_response,user_responseAdmin)

class rulesAdmin(admin.ModelAdmin):
    list_display=["question_id","rules"]
admin.site.register(rules,rulesAdmin)
class currentAdmin(admin.ModelAdmin):
    list_display=["tag","value"]
admin.site.register(current,currentAdmin)