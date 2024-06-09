from django.db import models
from authapp.models import CustomUser

# Create your models here.
class MatchRequests(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True,related_name='current_user')
    match_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True,related_name="matched_user")
    request_accepted = models.BooleanField(default=False)