from django.contrib import auth
from rest_framework import serializers
from .models import User
from services import auth_service

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('username'), email=validated_data.get('email'), password=validated_data.get('password'))
        user.save()
        return user
    