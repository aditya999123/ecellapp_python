from django.contrib import admin
from .models import timer_table,question
# Register your models here.
class timerAdmin(admin.ModelAdmin):
    list_display=["time"]
admin.site.register(timer_table,timerAdmin)

class questionAdmin(admin.ModelAdmin):
    list_display=["question"]
admin.site.register(question,questionAdmin)
