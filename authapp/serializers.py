from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CustomUser
        fields = ['id','username','email','phone','account_for','about_groom','date_joined',"is_blocked","subscribed"]

    