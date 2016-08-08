from django.contrib import admin
from .models import questions
# Register your models here.
# class timerAdmin(admin.ModelAdmin):
#     list_display=["time"]
# admin.site.register(timer_table,timerAdmin)

class questionsAdmin(admin.ModelAdmin):
    list_display=["question","question_id","question_type"]
admin.site.register(questions,questionsAdmin)
