from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class spons_dataAdmin(admin.ModelAdmin):
    list_display=["id"]
admin.site.register(spons_data,spons_dataAdmin)
