from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework import status
from UserProfileapp.models import BasicDetails,FamilyDetails,LocationDetails,ProfessionalsDetails,ReligionInformation
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from .models import generate_otp
from .utils import convertjwt
from .serializers import CustomUserSerializer
# Create your views here.

# customization for the token 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        return token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer





# registration of the user 
class UserRegistration(APIView):
            def post(self, request):
                        if CustomUser.objects.filter(email = request.data['email']).exists():
                                    return Response({"error": "emailused"},status=status.HTTP_400_BAD_REQUEST)
                        if len(request.data['phone']) != 10:
                                    return Response({"error": "phonenumber"},status=status.HTTP_400_BAD_REQUEST)
                        user = CustomUser(username = request.data['name'],email = request.data['email'],password = make_password(request.data['password']),phone = request.data['phone'],about_groom = request.data['about'],is_blocked = False,is_verified = False,account_for =  request.data['accountFor'])
                        user.save()
                        current_user = CustomUser.objects.get(id = user.id)
                        BasicDetails.objects.create(user_id = current_user,marital_status =request.data['maritalStatus'],dob=request.data['dob'],height=request.data['height'],mother_toungue= request.data['language'])
                        ReligionInformation.objects.create(user_id = current_user,religion=request.data['religion'],cast=request.data['cast'])
                        FamilyDetails.objects.create(user_id = current_user,family_status=request.data['familystatus'])
                        ProfessionalsDetails.objects.create(user_id = current_user,employed_in=request.data['employed_in'],annual_income=request.data['annual_income'])
                        LocationDetails.objects.create(user_id = current_user,contry=request.data['country'],state=request.data['state'],district=request.data['district'])
                        return Response({"message": "Signup successful"},status=status.HTTP_201_CREATED)
            def get(self ,request):
                  token = request.headers.get('Authorization')
                  user_id ,email = convertjwt(token)
                  print(user_id,email)
                  user = CustomUser.objects.get(id = user_id)
                  serializer = CustomUserSerializer(user)
                  print(serializer.data)
  
                  return Response({"message": "Success","user":serializer.data})

    
    



# after the registration otp verification
class Otpverificaion(APIView):
        def post(self,request):
            try:
              user = CustomUser.objects.get(email = request.data["email"])
            except:
                return Response({"error": "notpresent"},status=status.HTTP_400_BAD_REQUEST)
            if user.otp == int(request.data['otpValue']):
                  print("halo")
                  user.is_verified = True
                  user.save()
                  return Response({"message": "verified succesfully"},status=status.HTTP_201_CREATED)
            return Response({"error": "faild"},status=status.HTTP_400_BAD_REQUEST)



# login of the user
class Login(APIView):
      def post(self , request):
            print(request.data)
            email = request.data['email']
            password = request.data['password']
            print(request.content_type)
            try:
                  user = CustomUser.objects.get(email = email)
            except:
                  return Response({"error":"notpresent"},status=status.HTTP_400_BAD_REQUEST)
            if user and user.check_password(password) :
                  if user.is_superuser:
                         return Response({"message":"adminfound","role":"admin"},status=status.HTTP_200_OK)
                  else:
                       if user.is_verified:
                             return Response({"message":"userfound","role":"user"},status=status.HTTP_200_OK) 
                       else: 
                             subject  = "Your otp for verification "
                             otp = generate_otp()
                             message = f'Your OTP is: {otp}. Please do not share this OTP.'
                             from_email = 'muhammedmamu2906@gmail.com' 
                             recipient_list = [email]
                             send_mail( subject,message,from_email,recipient_list, fail_silently=False)
                             user.otp = otp
                             user.save()
                             return Response({"error":"notverified"},status=status.HTTP_400_BAD_REQUEST)
            return Response({"error":"notpresent"},status=status.HTTP_400_BAD_REQUEST)





