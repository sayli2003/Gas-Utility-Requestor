from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import ServiceRequest

class CustomUserAdmin(UserAdmin):
    # Customize admin interface for CustomUser
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(ServiceRequest)