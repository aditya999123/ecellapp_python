from django.contrib import admin

# Register your models here.
from .models import home_data
class home_dataAdmin(admin.ModelAdmin):
    list_display=["id","title"]
admin.site.register(home_data,home_dataAdmin)