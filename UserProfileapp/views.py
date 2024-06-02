import base64
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.utils import convertjwt
from .models import BasicDetails,FamilyDetails,Gallary,LocationDetails,ProfessionalsDetails,ReligionInformation,PatnerPreferences
from authapp.models import CustomUser
from .serializer import BasicDetailseializer,FamilyDetailsseializer,ReligionInformationseializer,ProfessionalsDetailsseializer,LocationDetailsseializer,Gallaryseializer,PatnerPreferencesDetailsseializer
from django.shortcuts import get_object_or_404
from authapp.serializers import CustomUserSerializer
# Create your views here.


class UserProfileDetails(APIView):
    def get(self,request):
        details_header_value = request.META.get('HTTP_DETAILS', None)
        token = request.headers.get('Authorization')
        user_id ,email = convertjwt(token)
        try:
           user = CustomUser.objects.get(id = user_id)
        except:
            return Response({"message":"error"})
        if details_header_value == "basic_details":
            basic_details = BasicDetails.objects.get(user_id = user)
            serializer1 = CustomUserSerializer(user)
            serializer = BasicDetailseializer(basic_details)
            return Response({"message":"success","basic_details":serializer.data,"userdetails":serializer1.data})
        elif details_header_value == "family_details":
            family_details = FamilyDetails.objects.get(user_id = user)
            serializer = FamilyDetailsseializer(family_details)
            return Response({"message":"success","family_details":serializer.data})
        elif details_header_value == "location_details":
            location_details  = LocationDetails.objects.get(user_id = user)
            serializer = LocationDetailsseializer(location_details)
            return Response({"message":"success","location_details":serializer.data})
        elif details_header_value == "partner_preferences":
            partner_preferences  = PatnerPreferences.objects.get(user_id = user)
            serializer = PatnerPreferencesDetailsseializer(partner_preferences)
            return Response({"message":"success","partner_preferences":serializer.data})
        elif details_header_value == "photos_gallary":
            photos_gallary  = Gallary.objects.get(user_id = user)
            serializer = Gallaryseializer(photos_gallary)
            return Response({"message":"success","photos_gallary":serializer.data})
        elif details_header_value == "profesional_details":
            profesional_details  = ProfessionalsDetails.objects.get(user_id = user)
            serializer = ProfessionalsDetailsseializer(profesional_details)
            return Response({"message":"success","profesional_details":serializer.data})
        elif details_header_value == "religional_information":
            religional_information  = ReligionInformation.objects.get(user_id = user)
            serializer = ReligionInformationseializer(religional_information)
            return Response({"message":"success","religional_information":serializer.data})
        return Response({"message":"error"})
    def put(self,request):
        details_header_value = request.META.get('HTTP_DETAILS', None)
        token = request.headers.get('Authorization')
        user_id ,email = convertjwt(token)
        user = CustomUser.objects.get(id = user_id)
        if details_header_value == "basic_details":
                userdetails = get_object_or_404(BasicDetails, user_id=user)
                aboutdetais = get_object_or_404(CustomUser, id=user_id)
                for key,value in request.data.items():
                    print(key,value)
                    if  key == "phone":
                        setattr(aboutdetais,key,value)
                        aboutdetais.save()
                    else:
                        setattr(userdetails,key,value)
                userdetails.save()
                return Response({"message":"success"})
        elif details_header_value == "religional_information":
                userdetails = get_object_or_404(ReligionInformation, user_id=user)
                for key,value in request.data.items():
                        setattr(userdetails,key,value)
                userdetails.save()
                return Response({"message":"success"})
        elif details_header_value == "profesional_details":
                userdetails = get_object_or_404(ProfessionalsDetails, user_id=user)
                for key,value in request.data.items():
                        setattr(userdetails,key,value)
                userdetails.save()
                return Response({"message":"success"})
        elif details_header_value == "partner_preferences":
                userdetails = get_object_or_404(PatnerPreferences, user_id=user)
                for key,value in request.data.items():
                        setattr(userdetails,key,value)
                userdetails.save()
                return Response({"message":"success"})
        elif details_header_value == "location_details":
                userdetails = get_object_or_404(LocationDetails, user_id=user)
                for key,value in request.data.items():
                        setattr(userdetails,key,value)
                userdetails.save()
                return Response({"message":"success"})
        elif details_header_value == "family_details":
                userdetails = get_object_or_404(FamilyDetails, user_id=user)
                for key,value in request.data.items():
                        setattr(userdetails,key,value)
                userdetails.save()
                return Response({"message":"success"})
        elif details_header_value == "photos_gallary":
                userdetails = get_object_or_404(Gallary, user_id=user)
                for i in range(2,6):
                      image_field_name = f'image{i}'
                      if f'image{i}' in request.data:
                                image1_file = request.data.get(f'image{i}')
                                format, imgstr = image1_file.split(';base64,')
                                ext = format.split('/')[-1]
                                image_file = ContentFile(base64.b64decode(imgstr), name=f'image{i}.{ext}')
                                setattr(userdetails, image_field_name, image_file)
                userdetails.save()
                return Response({"message":"success"})
        
    def delete(self,request) :
          img = request.data['name']
          token = request.headers.get("Authorization")
          user_id ,email = convertjwt(token)
          user = CustomUser.objects.get(id = user_id)
          imagerow = Gallary.objects.get(user_id = user)
          setattr(imagerow, img, None)
          imagerow.save()

          return Response({"message":"success"})

                      
                
                




    