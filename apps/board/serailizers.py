from venv import create
from django.contrib import auth
from rest_framework import serializers
from .models import Board
from services import user_service

class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'