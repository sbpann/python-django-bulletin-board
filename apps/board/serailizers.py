from django.contrib import auth
from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'
    
    def create(self, validated_data):
        # TODO: set created_by user from req.user
        # TODO: set moderator to be empty on create
        return super().create(validated_data)