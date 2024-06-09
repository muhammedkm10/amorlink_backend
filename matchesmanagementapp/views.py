from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authapp.utils import convertjwt
from .serializer import MatchModelSerializer
from .models import MatchRequests
from authapp.models import CustomUser
from authapp.serializers import CustomUserSerializer
from UserProfileapp.serializer import Gallaryseializer,Gallary

# Create your views here.

class MatchView(APIView):
      def post(self,request,id):
            token = request.headers.get("Authorization")
            user_id , email = convertjwt(token)
            data = {
                  'user_id':user_id,
                  'match_id':id,
                  "request_accepted":False
            }
            serializer = MatchModelSerializer(data = data)
            if serializer.is_valid():
                  serializer.save()
                  return Response({'message':"success"},status=status.HTTP_201_CREATED)
            return Response({'message':"error"},status=status.HTTP_400_BAD_REQUEST)
      def get(self,request):
            token = request.headers.get("Authorization")
            user_id ,email = convertjwt(token)
            user = CustomUser.objects.get(id = user_id)
            requested_users = MatchRequests.objects.filter(user_id = user).exclude(request_accepted = True)
            user_details = []
            for i in  requested_users:
                 basice_details = CustomUser.objects.get(id = i.match_id.id)
                 basice_details_serializer = CustomUserSerializer(instance = basice_details, many = False) 
                 image_details = Gallary.objects.get(user_id = basice_details)
                 image_serializer = Gallaryseializer(instance=image_details,many=False)
                 user_details.append({"id":basice_details_serializer.data['id'],"name":basice_details_serializer.data['username'],"image_details":image_serializer.data['image1']})
            return Response({'message':'success','requested_users':user_details},status=status.HTTP_200_OK)
            





            
