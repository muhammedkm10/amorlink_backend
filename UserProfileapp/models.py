from django.db import models
from authapp.models import CustomUser

# Create your models here.
class BasicDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    marital_status = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    height = models.CharField(max_length=50,null=True,blank=True)
    mother_toungue = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    body_type = models.CharField(max_length=30,null=True,blank=True)
    physical_status = models.CharField(max_length=30,null=True,blank=True)
    weight = models.CharField(max_length=30,null=True,blank=True)
    drinking_habits = models.CharField(max_length=30,null=True,blank=True)
    eating_habits = models.CharField(max_length=30,null=True,blank=True)
    smalking_habits = models.CharField(max_length=30,null=True,blank=True)
    hobbies = models.CharField(max_length=100,null=True,blank=True)
    age = models.CharField( max_length=50,null=True,blank=True)




class ReligionInformation(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    religion = models.CharField(max_length=30,null=True,blank=True)
    cast = models.CharField(max_length=30,null=True,blank=True)
    time_of_birth = models.CharField( max_length=50,null=True,blank=True)
    place_of_birth = models.CharField(max_length=50 ,null=True)
                                     




class FamilyDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    family_status = models.CharField(max_length=30,null=True,blank=True)
    family_value = models.CharField(max_length=50,null=True,blank=True)
    family_type = models.CharField(max_length=50,null=True,blank=True)
    father_occupation = models.CharField(max_length=50,null=True,blank=True)
    mother_occupation = models.CharField(max_length=50,null=True,blank=True)
    no_of_brothers = models.IntegerField(null=True,blank=True)
    no_of_brothers_married = models.IntegerField(null=True,blank=True)
    no_of_sisters = models.IntegerField(null=True,blank=True)
    no_of_sisters_married = models.IntegerField(null=True,blank=True)
    family_location = models.CharField(max_length=50 , null=True,blank=True)
    about_family = models.TextField(null=True,blank=True)










     


class ProfessionalsDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    employed_in = models.CharField(max_length=30,null=True,blank=True)
    annual_income = models.CharField(max_length=30,null=True,blank=True)
    highest_education = models.CharField(max_length=50,null=True,blank=True)
    education_in_details = models.TextField(null=True)
    college  =  models.CharField(max_length=50,null=True,blank=True)
    occupation  =  models.CharField(max_length=50,null=True,blank=True)
    organization  =  models.CharField(max_length=50,null=True,blank=True)



    


class LocationDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    contry = models.CharField(max_length=30,null=True,blank=True)
    state = models.CharField(max_length=30,null=True,blank=True)
    district = models.CharField(max_length=30,null=True,blank=True)
    ancesters_origin = models.CharField(max_length=30,null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    work_place = models.CharField(max_length=30,null=True,blank=True)

 


class Gallary(models.Model):
    user_id =  models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    image1 = models.ImageField(upload_to='user_gallary',null=True,blank=True)
    image2 = models.ImageField(upload_to='user_gallary',null=True,blank=True)
    image3 = models.ImageField(upload_to='user_gallary',null=True,blank=True)
    image4 = models.ImageField(upload_to='user_gallary',null=True,blank=True)
    image5 = models.ImageField(upload_to='user_gallary',null=True,blank=True)




class PatnerPreferences(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    patner_age = models.IntegerField(blank=True ,null=True)
    height = models.CharField(max_length=50,null=True,blank=True)
    marital_status = models.CharField(max_length=100,null=True,blank=True)
    mother_toungue = models.CharField(max_length=50,null=True,blank=True)
    physical_status = models.CharField(max_length=30,null=True,blank=True)
    eating_habits = models.CharField(max_length=30,null=True,blank=True)
    drinking_habits = models.CharField(max_length=30,null=True,blank=True)
    smalking_habits = models.CharField(max_length=30,null=True,blank=True)
    religion = models.CharField(max_length=30,null=True,blank=True)
    cast = models.CharField(max_length=30,null=True,blank=True)
    highest_education = models.CharField(max_length=50,null=True,blank=True)
    employed_in = models.CharField(max_length=30,null=True,blank=True)
    annual_income = models.CharField(max_length=30,null=True,blank=True)
    about_partner = models.TextField(blank=True,null=True)






