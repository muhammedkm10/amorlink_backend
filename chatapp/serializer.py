from rest_framework.serializers import ModelSerializer
from .models import ChatMessages,Notifications
from authapp.serializers import CustomUserSerializer
from authapp.models import CustomUser

class chatModelSerializer(ModelSerializer):
    class Meta:
        model = ChatMessages
        fields = '__all__'

class Cusomuseserializer_for_notifications(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username'] 

class NotificationSerializer(ModelSerializer):
    sender = Cusomuseserializer_for_notifications()
    class Meta:
        model = Notifications
        fields = ['sender','match_send_request']










