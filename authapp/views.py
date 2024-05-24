from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework import status
from UserProfileapp.models import BasicDetails,FamilyDetails,LocationDetails,ProfessionalsDetails,ReligionInformation
from django.contrib.auth.hashers import make_password

# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        if CustomUser.objects.filter(email = request.data['email']).exists():
                    return Response({"error": "emailused"},status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['phone']) != 10:
                    return Response({"error": "phonenumber"},status=status.HTTP_400_BAD_REQUEST)
        user = CustomUser(username = request.data['name'],email = request.data['email'],password = make_password(request.data['password']),phone = request.data['phone'],about_groom = request.data['about'],is_blocked = False,is_verified = False,account_for =  request.data['accountFor'])
        user.save()
        current_user = CustomUser.objects.get(id = user.id)
        
        # BasicDetails.objects.create(user_id = current_user,marital_status =request.data['maritalStatus'],dob=request.data['dob'],height=request.data['height'],mother_toungue= request.data['language'])
        # ReligionInformation.objects.create(user_id = current_user,religion=request.data['religion'],cast=request.data['cast'])
        # FamilyDetails.objects.create(user_id = current_user,family_status=request.data['familystatus'])
        # ProfessionalsDetails.objects.create(user_id = current_user,employed_in=request.data['employed_in'],annual_income=request.data['annual_income'])
        # LocationDetails.objects.create(user_id = current_user,contry=request.data['country'],state=request.data['state'],district=request.data['district'])
        return Response({"message": "Signup successful"},status=status.HTTP_201_CREATED)
    

class Otpverificaion(APIView):
        def post(self,request):
            print(request.data['otpValue'],request.data['email'])
            try:
              user = CustomUser.objects.get(email = request.data["email"])
            except:
                return Response({"error": "notpresent"},status=status.HTTP_400_BAD_REQUEST)
            print(user)
            if user.otp == int(request.data['otpValue']):
                  print("halo")
                  user.is_verified = True
                  user.save()
                  return Response({"message": "verified succesfully"},status=status.HTTP_201_CREATED)
            return Response({"error": "faild"},status=status.HTTP_400_BAD_REQUEST)
            

                
