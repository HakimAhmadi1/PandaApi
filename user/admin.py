from django.contrib import admin
from .models import Seeker_Info, SSL_Info, Projects, Employment_Status, Experience, Qualification, Seeker_Cv


@admin.register(Seeker_Info)
class SeekerAdmin(admin.ModelAdmin):
    list_display = ('seeker','get_seeker_country', 'date_of_birth','place_of_birth','gender','passport','city')

    def get_seeker_country(self, obj):
        return obj.seeker.country

    get_seeker_country.short_description = 'Seeker Country'

@admin.register(SSL_Info)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('seeker','shortened_text','skill','language')

    def shortened_text(self, obj):
        
        max_length = 50
        if len(obj.summary) <= max_length:
            return obj.summary
        return f"{obj.summary[:max_length]}..."

    shortened_text.short_description = 'Short Summary'

# @admin.register(SSL_Info)
# class SkillsAdmin(admin.ModelAdmin):
#     list_display = ('seeker','skill','summary','language')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('seeker','role','short_text','url')

    def short_text(self, obj):
        
        max_length = 50
        if len(obj.description) <= max_length:
            return obj.description
        return f"{obj.description[:max_length]}..."

    short_text.short_description = 'Short Description'

# @admin.register(Languages)
# class LanguagesAdmin(admin.ModelAdmin):
#     list_display = ('seeker','language')

@admin.register(Employment_Status)
class Employment_StatusAdmin(admin.ModelAdmin):
    list_display = ('seeker','employment_status','employment_experience','employment_position','seeking_position')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('seeker','company','position','country','period_from','period_to')

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('seeker','education_level','degree','institute','start_period','complete_period')

admin.site.register(Seeker_Cv)
