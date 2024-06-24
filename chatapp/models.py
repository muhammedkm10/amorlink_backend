from django.db import models
from authapp.models import CustomUser
# Create your models here.

class ChatMessages(models.Model):
    sender = models.IntegerField(null=True,blank= True)
    receiver = models.IntegerField(null=True,blank= True)
    content = models.TextField()
    thread_name = models.CharField(max_length=30,null= True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
