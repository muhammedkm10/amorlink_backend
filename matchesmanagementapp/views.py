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
from django.db.models import Q
# Create your views here.




# view for match management
class MatchView(APIView):
      # requesting for matches
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
      # fetching data from the data base to get the requested matches by current users and accepted matches by you
      def get(self,request):
            token = request.headers.get("Authorization")
            requested_for = request.META.get('HTTP_DETAILS',None)
            print(requested_for,"in the view")
            user_id ,email = convertjwt(token)
            user = CustomUser.objects.get(id = user_id)
            requested_users = MatchRequests.objects.none()
            user_details = []
            user_details1 = []
            user_details2 = []


            if not user.subscribed:
                  return Response({'message':'not subscribes'},status=status.HTTP_204_NO_CONTENT)
            if requested_for == "my_requests":
                  current_user_requestes = MatchRequests.objects.filter(user_id = user,match_id__is_blocked = False).exclude(request_accepted = True)
                  for i in current_user_requestes:
                       print(i.match_id.is_blocked,i.match_id.email)
                  print(current_user_requestes,"ddfdfdfd")
                  for i in  current_user_requestes:
                        basice_details = CustomUser.objects.get(id = i.match_id.id)
                        basic_details_serializer = CustomUserSerializer(instance = basice_details, many = False) 
                        image_details = Gallary.objects.get(user_id = basice_details)
                        image_serializer = Gallaryseializer(instance=image_details,many=False)
                        user_details2.append({"id":basic_details_serializer.data['id'],"name":basic_details_serializer.data['username'],"image_details":image_serializer.data['image1']})
                  return Response({'message':'success','users':user_details2},status=status.HTTP_200_OK)

            # requested matches by other to you
            if requested_for == "requested_users":
                 requested_users = MatchRequests.objects.filter(match_id = user.id,match_id__is_blocked = False).exclude(request_accepted = True)
                 for i in  requested_users:
                        basice_details = CustomUser.objects.get(id = i.user_id.id,is_blocked  = False)
                        basic_details_serializer = CustomUserSerializer(instance = basice_details, many = False) 
                        image_details = Gallary.objects.get(user_id = basice_details)
                        image_serializer = Gallaryseializer(instance=image_details,many=False)
                        user_details1.append({"id":basic_details_serializer.data['id'],"name":basic_details_serializer.data['username'],"image_details":image_serializer.data['image1']})
                 return Response({'message':'success','users':user_details1},status=status.HTTP_200_OK)
            
            

            # matched  by current user or other side user
            if requested_for == "matched":
            #      other users requested to match current user accepted
                 requested_users = MatchRequests.objects.filter(match_id = user.id,match_id__is_blocked = False).exclude(request_accepted = False)
            #      you requested and others accepted
                 requested_by_current_user = MatchRequests.objects.filter(user_id = user.id,match_id__is_blocked = False).exclude(request_accepted = False)
                 for i in  requested_users:
                        basice_details = CustomUser.objects.get(id = i.user_id.id,is_blocked  = False)
                        basic_details_serializer = CustomUserSerializer(instance = basice_details, many = False) 
                        image_details = Gallary.objects.get(user_id = basice_details)
                        image_serializer = Gallaryseializer(instance=image_details,many=False)
                        user_details.append({"id":basic_details_serializer.data['id'],"name":basic_details_serializer.data['username'],"image_details":image_serializer.data['image1']})
                 for i in  requested_by_current_user:
                        basice_details = CustomUser.objects.get(id = i.match_id.id,is_blocked  = False)
                        basic_details_serializer = CustomUserSerializer(instance = basice_details, many = False) 
                        image_details = Gallary.objects.get(user_id = basice_details)
                        image_serializer = Gallaryseializer(instance=image_details,many=False)
                        user_details.append({"id":basic_details_serializer.data['id'],"name":basic_details_serializer.data['username'],"image_details":image_serializer.data['image1']})
                 return Response({'message':'success','users':user_details},status=status.HTTP_200_OK)
            
            if not requested_users.exists():
                   return Response({'message':'nodata','users':[]},status=status.HTTP_200_OK)
            
      # to accept the request
      def patch(self,request,id):
            token = request.headers.get('Authorization')
            user_id ,email = convertjwt(token)
            obj = MatchRequests.objects.get(Q(match_id = user_id)&Q(user_id = id))
            obj.request_accepted = True
            obj.save()
            return Response({"message":"success"})
      # removing the requests from the requests
      def delete(self, request,id):
            token = request.headers.get('Authorization')
            user_id ,email = convertjwt(token)
            obj = MatchRequests.objects.get(Q(Q(match_id = user_id)&Q(user_id = id))|Q(Q(match_id = id)&Q(user_id = user_id)))
            obj.delete()

            return Response({"message":"success"})

            
            





            
