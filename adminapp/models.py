from django.db import models
import stripe
from django.conf import settings
from authapp.models import CustomUser
# Create your models here.
stripe.api_key = settings.STRIPE_SECRET_KEY

class Subscription(models.Model):
    plan_name = models.CharField( max_length=50,null=True,blank = True)
    amount = models.IntegerField(blank=True,null=True)
    vlalidity_months = models.IntegerField(blank=True,null=True)
    stripe_product_id = models.CharField(max_length=255,null=True,blank=True)
    stripe_price_id = models.CharField(max_length=255,null=True,blank=True)
    is_listed = models.BooleanField(default=True)
    no_users = models.BigIntegerField(blank=True,null=True)


    def save(self ,*args, **kwargs):
        if not self.stripe_price_id or not self.stripe_product_id:
            print("amount enteres in before the storage in the server",self.amount)
            self.create_stripe_product_and_price()
        super().save(*args,**kwargs)

    def  create_stripe_product_and_price(self):
       print("amount entered",self.amount)
       amount_paise = int(self.amount * 100)
       print(amount_paise)
       try:
            product = stripe.Product.create(name=self.plan_name)
            price = stripe.Price.create(
                product=product.id,
                unit_amount=amount_paise,
                currency='inr'  # Assuming you want to set the currency to INR
            )
            self.stripe_product_id = product.id
            self.stripe_price_id = price.id
       except stripe.error.StripeError as e:
            # Handle any Stripe API errors here
            print(f"Stripe API Error: {e}")
    

class SubscriptionDetails(models.Model):
    plan = models.ForeignKey(Subscription,on_delete=models.CASCADE,blank=True,null=True)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    payment_session_id = models.CharField(max_length=300 ,null=True,blank=True)
    date_started =  models.DateField(null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True)



