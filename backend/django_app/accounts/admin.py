from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django_app.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
