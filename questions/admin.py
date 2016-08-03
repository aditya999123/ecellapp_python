from django.contrib import admin
from .models import timer_table
# Register your models here.
class timerAdmin(admin.ModelAdmin):
    list_display=["time"]
admin.site.register(timer_table,timerAdmin)
