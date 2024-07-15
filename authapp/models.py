from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
import random



# Create your models here.
class CustomUser(AbstractUser):
    # USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, blank=True)
    # REQUIRED_FIELDS = []
    username = models.CharField(max_length=150, blank=True,unique=True)
    phone = models.CharField(max_length=20, blank=True , null=True)
    account_for = models.CharField(max_length=20, blank=True,null=True)
    about_groom  = models.TextField(null=True,blank=True)
    otp = models.IntegerField(blank=True,null= True)
    is_blocked = models.BooleanField(blank=True ,null=True)
    is_verified = models.BooleanField(blank=True ,null=True)
    male = models.BooleanField(null=True)
    subscribed = models.BooleanField(default=False)



@receiver(post_save, sender=CustomUser)
def _post_save_receiver(sender,instance,created, **kwargs):
    if created:
        subject = 'Your OTP for verification'
        otp = generate_otp()
        message = f'Your OTP is: {otp}. Please do not share this OTP.'
        from_email = 'muhammedmamu2906@gmail.com' 
        recipient_list = [instance.email]
        send_mail( subject,message,from_email,recipient_list, fail_silently=False)
        instance.otp = otp
        instance.save()


def generate_otp():
    return random.randint(100000, 999999)





    
    



