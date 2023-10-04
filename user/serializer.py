
from rest_framework import serializers
from .models import SSL_Info, Seeker_Info, Projects, Employment_Status, Experience, Qualification, Seeker_Cv
from backend.models import User

class Seeker_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker_Info
        fields = "__all__" 

class SSL_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSL_Info
        fields = ["id","summary","skill","language"]

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__" 

class Employment_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment_Status
        fields = "__all__" 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__" 

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__" 

class Seeker_CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seeker_Cv
        fields = "__all__" 

class Seeker_ProfileSerializer(serializers.ModelSerializer):
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
