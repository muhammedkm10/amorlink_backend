from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.utils import convertjwt
from .models import BasicDetails,FamilyDetails,Gallary,LocationDetails,ProfessionalsDetails,ReligionInformation,PatnerPreferences
from authapp.models import CustomUser
from .serializer import BasicDetailseializer,FamilyDetailsseializer,ReligionInformationseializer,ProfessionalsDetailsseializer,LocationDetailsseializer,Gallaryseializer,PatnerPreferencesDetailsseializer
# Create your views here.


class UserProfileDetails(APIView):
    def get(self,request):
        details_header_value = request.META.get('HTTP_DETAILS', None)
        token = request.headers.get('Authorization')
        user_id ,email = convertjwt(token)
        print(user_id)
        try:
           user = CustomUser.objects.get(id = user_id)
        except:
            return Response({"message":"error"})
        if details_header_value == "basic_details":
            basic_details = BasicDetails.objects.get(user_id = user)
            serializer = BasicDetailseializer(basic_details)
            return Response({"message":"success","basic_details":serializer.data})
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
    