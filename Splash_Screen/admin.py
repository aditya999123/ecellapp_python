from django.contrib import admin


# Register your models here.
from .models import splash_screen_model


class splash_screen_model_admin(admin.ModelAdmin):
    list_display=["app_version","compulsary_update"]

admin.site.register(splash_screen_model,splash_screen_model_admin)
# Register your models here.
