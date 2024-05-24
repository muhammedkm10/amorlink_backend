from django.db import models
from authapp.models import CustomUser

# Create your models here.
class BasicDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    marital_status = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    height = models.CharField(max_length=50,null=True,blank=True)
    mother_toungue = models.CharField(max_length=50,null=True,blank=True)


class ReligionInformation(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    religion = models.CharField(max_length=30,null=True,blank=True)
    cast = models.CharField(max_length=30,null=True,blank=True)




class FamilyDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    family_status = models.CharField(max_length=30,null=True,blank=True)


class ProfessionalsDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    employed_in = models.CharField(max_length=30,null=True,blank=True)
    annual_income = models.CharField(max_length=30,null=True,blank=True)
    


class LocationDetails(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    contry = models.CharField(max_length=30,null=True,blank=True)
    state = models.CharField(max_length=30,null=True,blank=True)
    district = models.CharField(max_length=30,null=True,blank=True)







