from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class developer_dataAdmin(admin.ModelAdmin):
    list_display=["id"]
admin.site.register(developer_data,developer_dataAdmin)
