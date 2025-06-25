from rest_framework import serializers
from .models import CustomUser

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email','password','user_type']
        
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        fields=['email','password','user_type']
        
