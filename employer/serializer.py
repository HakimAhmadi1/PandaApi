
from backend.models import User
from rest_framework import serializers
from .models import Company_Info, Notification, Todo_List, Notes_List, Jobs, Job_Preferences, Job_PreScreen, Job_Reviews, Application

class Company_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Info
        fields = "__all__"    

class Todo_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_List
        fields = "__all__"
    
    
class Notes_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes_List
        fields = "__all__"

class JobsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Jobs
        fields = ["id","title", "hiring_number","hiring_country","hiring_city","phase","description","type","salary_rate","salary_start_range","salary_end_range","employer"]

class Job_PreferencesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Job_Preferences
        fields = "__all__" 

class Job_PreScreenSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Job_PreScreen
        fields = "__all__" 

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id","status","match"]

class Job_ReviewsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Job_Reviews
        fields = "__all__" 

class Applicant_CandidateViewSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Job_Reviews
        fields = "__all__" 

class Employer_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ["first_name", "last_name", "email", "phone"] 

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'message', 'create_at')