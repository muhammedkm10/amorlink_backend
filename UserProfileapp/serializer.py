from rest_framework import serializers
from .models import BasicDetails,FamilyDetails,Gallary,LocationDetails,ProfessionalsDetails,ReligionInformation,PatnerPreferences



# basicdetails modal serializer
class BasicDetailseializer(serializers.ModelSerializer):
    class Meta:
        model  = BasicDetails
        fields = ['marital_status','dob','height','mother_toungue','gender','body_type',"physical_status","weight","drinking_habits","eating_habits","smalking_habits","hobbies","age"]


# ReligionInformation modal serializer
class ReligionInformationseializer(serializers.ModelSerializer):
    class Meta:
        model  = ReligionInformation
        fields = ['religion','cast','time_of_birth','place_of_birth']


# FamilyDetails modal serializer
class FamilyDetailsseializer(serializers.ModelSerializer):
    class Meta:
        model  = FamilyDetails
        fields = ['family_status','family_value','family_type','father_occupation','mother_occupation','no_of_brothers',"no_of_brothers_married","no_of_sisters","no_of_sisters_married","family_location","about_family"]


# Gallary modal serializer
class Gallaryseializer(serializers.ModelSerializer):
    class Meta:
        model  = Gallary
        fields = ['image1','image2','image3','image4','image5']


# locatom modal serializers
class LocationDetailsseializer(serializers.ModelSerializer):
    class Meta:
        model  = LocationDetails
        fields = ['contry','state','district','ancesters_origin','city','work_place']


#  professional details serializer
class ProfessionalsDetailsseializer(serializers.ModelSerializer):
    class Meta:
        model  = ProfessionalsDetails
        fields = ['employed_in','annual_income','highest_education','education_in_details','college','occupation',"organization"]


# PatnerPreferences modal serializer
class PatnerPreferencesDetailsseializer(serializers.ModelSerializer):
    class Meta:
        model  = PatnerPreferences
        fields = ['patner_age','height','marital_status','mother_toungue','physical_status','eating_habits',"drinking_habits","smalking_habits","religion","cast","highest_education","employed_in","annual_income","about_partner"]


