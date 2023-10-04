from django.contrib import admin
from .models import User, ContactUs

# admin.site.register([User])

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','country','phone', 'is_seeker','is_employer','is_manager')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('email','name','phone', 'subject','message')