from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Company_Info, Todo_List, Notes_List, Jobs, Job_Preferences, Job_PreScreen, Job_Reviews, Application

@admin.register(Company_Info)
class Company_InfoAdmin(admin.ModelAdmin):
    list_display = ("employer","company_name","industry","city","website","operating_since")

@admin.register(Todo_List)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('employer', 'shortened_todo', 'is_complete')

    def shortened_todo(self, obj):
        
        max_length = 50
        if len(obj.todo) <= max_length:
            return obj.todo
        return f"{obj.todo[:max_length]}..."

    shortened_todo.short_description = 'Shortened Todo'

@admin.register(Notes_List)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('employer', 'shortened_todo', 'is_complete')

    def shortened_todo(self, obj):
        
        max_length = 50
        if len(obj.notes) <= max_length:
            return obj.notes
        return f"{obj.notes[:max_length]}..."

    shortened_todo.short_description = 'Shortened Todo'

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('employer', 'title', 'hiring_country', 'status','phase','salary_start_range','salary_end_range','created_at')

@admin.register(Job_Preferences)
class Job_PreferencesAdmin(admin.ModelAdmin):
    list_display = ('job', 'resume', 'send_update_to','application_deadline','hiring_timeline')

@admin.register(Job_PreScreen)
class Job_PreScreenAdmin(admin.ModelAdmin):
    list_display = ('job', 'question', 'required')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'seeker', 'status','match','applied_date')

@admin.register(Job_Reviews)
class Job_ReviewAdmin(admin.ModelAdmin):
    list_display = ('job', 'email', 'review','shortlisted_candidate','interview_candidate','rate')

