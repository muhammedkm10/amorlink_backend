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
from datetime import datetime
from django.db.models import Q

# Create your views here.


class UserProfileDetails(APIView):
    def get(self,request):
        details_header_value = request.META.get('HTTP_DETAILS', None)
        lookupUserid = request.META.get('HTTP_USERID', None)
        print(lookupUserid)
        if lookupUserid is not None:
                user = CustomUser.objects.get(id = lookupUserid)
        else:
                token = request.headers.get('Authorization')
                user_id ,email = convertjwt(token)
                user = CustomUser.objects.get(id = user_id)
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
                aboutdetails = get_object_or_404(CustomUser, id=user_id)
                for key,value in request.data.items():
                    if  key == "phone":
                        setattr(aboutdetails,key,value)
                        aboutdetails.save()
                    else:
                        if key == "dob":
                                current_date = datetime.now()
                                dobofuser_str = request.data['dob']
                                dobofuser = datetime.fromisoformat(dobofuser_str)  
                                age = current_date.year - dobofuser.year - ((current_date.month, current_date.day) < (dobofuser.month, dobofuser.day))
                                setattr(userdetails,"age",age)
                                setattr(userdetails,"dob",dobofuser)
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



# showing the preferences according to their preferences
class ShowPreferences(APIView):
      def get(self,request):
            details_header_value = request.META.get('HTTP_DETAILS', None)
            token = request.headers.get('Authorization')
            user_id ,email = convertjwt(token)
            user = CustomUser.objects.get(id = user_id)
            user_preferences = PatnerPreferences.objects.get(user_id_id = user.id)
            print("gender", user.male)

            
            if details_header_value == "religion":
                  other_users = ReligionInformation.objects.filter(Q(religion = user_preferences.religion) | Q(cast = user_preferences.cast) ).exclude( Q(user_id = user.id)|Q(user_id__male = user.male))
                  response_data = {"message":"success",'users':[]}
                  for user in other_users:
                        obj = CustomUser.objects.get(email = user.user_id )
                        main_detail_of_user = CustomUser.objects.get(email  = user.user_id)
                        basice_details = BasicDetails.objects.get(user_id = obj.id)
                        image = Gallary.objects.get(user_id = obj.id)
                        serializer1 = CustomUserSerializer(main_detail_of_user)
                        serializer2 = BasicDetailseializer(basice_details)
                        serializer3 = Gallaryseializer(image)
                        response_data['users'].append({"main_detail_of_user":serializer1.data,"basice_details":serializer2.data,"image":serializer3.data})
                  return Response(response_data) 
            

            elif details_header_value == "profession":
                  other_users = ProfessionalsDetails.objects.filter(Q(highest_education = user_preferences.highest_education)|Q(employed_in = user_preferences.employed_in)|Q(annual_income = user_preferences.annual_income)).exclude(Q(user_id = user.id)|Q(user_id__male = user.male))
                  response_data = {"message":"success",'users':[]}
                  for user in other_users:
                        obj = CustomUser.objects.get(email = user.user_id )
                        main_detail_of_user = CustomUser.objects.get(email  = user.user_id)
                        basice_details = BasicDetails.objects.get(user_id = obj.id)
                        image = Gallary.objects.get(user_id = obj.id)
                        serializer1 = CustomUserSerializer(main_detail_of_user)
                        serializer2 = BasicDetailseializer(basice_details)
                        serializer3 = Gallaryseializer(image)
                        response_data['users'].append({"main_detail_of_user":serializer1.data,"basice_details":serializer2.data,"image":serializer3.data})
                  return Response(response_data)
            
            elif details_header_value == "personal":
                  other_users = BasicDetails.objects.filter(Q(age = user_preferences.patner_age)|Q(height = user_preferences.height)|Q(marital_status = user_preferences.marital_status)|Q(mother_toungue = user_preferences.mother_toungue)|Q(physical_status = user_preferences.physical_status)).exclude(Q(user_id = user.id)|Q(user_id__male = user.male))
                  response_data = {"message":"success",'users':[]}
                  for user in other_users:
                        obj = CustomUser.objects.get(email = user.user_id )
                        main_detail_of_user = CustomUser.objects.get(email  = user.user_id)
                        basice_details = BasicDetails.objects.get(user_id = obj.id)
                        image = Gallary.objects.get(user_id = obj.id)
                        serializer1 = CustomUserSerializer(main_detail_of_user)
                        serializer2 = BasicDetailseializer(basice_details)
                        serializer3 = Gallaryseializer(image)
                        response_data['users'].append({"main_detail_of_user":serializer1.data,"basice_details":serializer2.data,"image":serializer3.data})
                  return Response(response_data)
            
            elif details_header_value == "lifestyle":
                  other_users = BasicDetails.objects.filter(Q(drinking_habits = user_preferences.drinking_habits)|Q(eating_habits = user_preferences.eating_habits)|Q(marital_status = user_preferences.marital_status)|Q(smalking_habits = user_preferences.smalking_habits)).exclude(Q(user_id = user.id)|Q(user_id__male = user.male))
                  response_data = {"message":"success",'users':[]}
                  for user in other_users:
                        obj = CustomUser.objects.get(email = user.user_id )
                        main_detail_of_user = CustomUser.objects.get(email  = user.user_id)
                        basice_details = BasicDetails.objects.get(user_id = obj.id)
                        image = Gallary.objects.get(user_id = obj.id)
                        serializer1 = CustomUserSerializer(main_detail_of_user)
                        serializer2 = BasicDetailseializer(basice_details)
                        serializer3 = Gallaryseializer(image)
                        response_data['users'].append({"main_detail_of_user":serializer1.data,"basice_details":serializer2.data,"image":serializer3.data})
                  return Response(response_data)
            





                
                




    