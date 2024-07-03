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
from matchesmanagementapp.models import MatchRequests
from authapp.serializers import CustomUserSerializer
# Create your views here.
class MatchedUsersForChat(APIView):
    def get(self,request,userid,reciverid):
        if reciverid == "0":
             return Response({'message':"from navbar"})
        try:
            current_user = CustomUser.objects.get(id = userid)
            reciver =  CustomUser.objects.get(id = reciverid)
        except:
              return Response({'message':"no users"})
        
        if not current_user.subscribed :
             return Response({'message':"no_subscription"})
        try:
          ismatched = MatchRequests.objects.get(Q(user_id = current_user,match_id = reciver,request_accepted = True)|Q(user_id = reciver,match_id = current_user,request_accepted = True))
        except:
             return Response({'message':"no_matched_each_other"})
        
        messages =  ChatMessages.objects.filter(Q(sender = userid , receiver= reciverid)|Q(sender = reciverid , receiver= userid))
        photos = Gallary.objects.get(user_id = reciverid)
        photo_serializer = Gallaryseializer(photos,many=False)
        serializer = chatModelSerializer(messages,many = True)
        customuserserializer = CustomUserSerializer(reciver,many=False)
        messages = serializer.data
        return Response({'message':"success","messages":messages,"image":photo_serializer.data['image1'],"username":customuserserializer.data['username']})














































# notification view for chat
class Notification(APIView):
        def post(self,request,sender,reciverid):
            details_header_value = request.data.get('headers')
            message = details_header_value["details"]
            sender =  CustomUser.objects.get(id = sender)
            notification_message = f'📩 ({sender.username.upper()}): {message}'
            send_notification_to_user(reciverid, notification_message)
            return Response({'status': 'error', 'message': 'Only POST requests are allowed'})
        










