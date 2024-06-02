from django.db import models

# Create your models here.

class Subscription(models.Model):
    plan_name = models.CharField( max_length=50,null=True,blank = True)
    amount = models.IntegerField(blank=True,null=True)
    vlalidity_months = models.IntegerField(blank=True,null=True)
    is_listed = models.BooleanField(default=True)
    no_users = models.BigIntegerField(blank=True,null=True)


