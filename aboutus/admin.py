from django.contrib import admin
from .models import *

class aboutus_dataAdmin(admin.ModelAdmin):
    list_display=["id"]
admin.site.register(aboutus_data,aboutus_dataAdmin)

# Register your models here.
