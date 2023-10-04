from rest_framework import serializers
from .models import User, ContactUs
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country','password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            country=validated_data['country'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            
        )
        return user
    
    def validate_email(self, value):
        if not value.endswith('.com') and "@" not in value: 
            raise ValidationError("Invalid email format. Only example.com emails are allowed.")
        return value
    
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'