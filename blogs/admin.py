from django.contrib import admin
from .models import *

class blogs_dataAdmin(admin.ModelAdmin):
    list_display=["id","title"]
admin.site.register(blogs_data,blogs_dataAdmin)

# Register your models here.
