from django.db import models
from authapp.models import CustomUser
# Create your models here.

class ChatMessages(models.Model):
    sender = models.IntegerField(null=True,blank= True)
    receiver = models.IntegerField(null=True,blank= True)
    content = models.TextField()
    thread_name = models.CharField(max_length=30,null= True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Notifications(models.Model):
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name="notification_sender")
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name='notification_reciever')
    match_send_request = models.BooleanField(null=True,blank=True)
    seen = models.BooleanField(default=False)





