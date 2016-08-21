from django.contrib import admin


# Register your models here.
from .models import version_control


class version_control_admin(admin.ModelAdmin):
    list_display=["app_version","compulsary_update"]

admin.site.register(version_control,version_control_admin)
# Register your models here.
