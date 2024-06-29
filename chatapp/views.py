from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.utils import convertjwt
from chatapp.models import ChatMessages
from django.db.models import Q
from .serializer import chatModelSerializer
from UserProfileapp.models import Gallary
from UserProfileapp.serializer import Gallaryseializer
from .consumers import send_notification_to_user
from authapp.models import CustomUser
# Create your views here.
class MatchedUsersForChat(APIView):
    def get(self,request,userid,reciverid):
        messages =  ChatMessages.objects.filter(Q(sender = userid , receiver= reciverid)|Q(sender = reciverid , receiver= userid))
        photos = Gallary.objects.get(user_id = reciverid)
        photo_serializer = Gallaryseializer(photos,many=False)
        serializer = chatModelSerializer(messages,many = True)
        messages = serializer.data
        return Response({'message':"success","messages":messages,"image":photo_serializer.data['image1']})



# notification view for chat
class Notification(APIView):
        def post(self,request,sender,reciverid):
            details_header_value = request.data.get('headers')
            message = details_header_value["details"]
            sender =  CustomUser.objects.get(id = sender)
            notification_message = f'📩 ({sender.username.upper()}): {message}'
            send_notification_to_user(reciverid, notification_message)
            return Response({'status': 'error', 'message': 'Only POST requests are allowed'})
        










