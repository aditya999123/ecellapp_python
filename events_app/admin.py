from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class events_dataAdmin(admin.ModelAdmin):
    list_display=["id","event_name"]
admin.site.register(events_data,events_dataAdmin)
