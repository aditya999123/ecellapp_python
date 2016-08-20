from django.contrib import admin
from .models import *
# Register your models here.
class contactus_dataAdmin(admin.ModelAdmin):
    list_display=["id","name"]
admin.site.register(contactus_data,contactus_dataAdmin)
