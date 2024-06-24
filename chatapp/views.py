from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.utils import convertjwt
from chatapp.models import ChatMessages
from django.db.models import Q
from .serializer import chatModelSerializer
from UserProfileapp.models import Gallary
from UserProfileapp.serializer import Gallaryseializer
# Create your views here.
class MatchedUsersForChat(APIView):
    def get(self,request,userid,reciverid):
        messages =  ChatMessages.objects.filter(Q(sender = userid , receiver= reciverid)|Q(sender = reciverid , receiver= userid))
        photos = Gallary.objects.get(user_id = reciverid)
        photo_serializer = Gallaryseializer(photos,many=False)

        
        serializer = chatModelSerializer(messages,many = True)
        return Response({'message':"success","messages":serializer.data,"image":photo_serializer.data['image1']})
