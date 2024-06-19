from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Subscription,SubscriptionDetails
from .serializers import  Add_Update_subscription,Retrive_delete_subscription,Subscribed_user_serializer
from authapp.models import CustomUser
from authapp.serializers import CustomUserSerializer
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
import os
import stripe
from django.conf import settings
from authapp.utils import convertjwt
from django.shortcuts import redirect
from urllib.parse import urlencode




# Create your views here.

# view for adding and listing subcription
class Add_List_subscription(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = Subscription.objects.all()

    def get_serializer_class(self):            #  getting serializer classesss
        if self.request.method in ["POST",'PUT','PATCH']:
            return Add_Update_subscription
        return Retrive_delete_subscription
    
    def create(self, request, *args, **kwargs):    #creating the subscription plans
        serializer  = self.get_serializer(data = request.data)   # deserializing and validating the data
        serializer.is_valid(raise_exception = True) 
        self.perform_create(serializer)   #here creating new instance in the subscription table
        return Response({"message":"success"},status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)   #indicating the updation is partial
        instance = self.get_object()             #taking the object from the database that is to be updated
        serializer = self.get_serializer(instance,data = request.data,partial = partial)   #seializing the incoming data and the retrieved object
        serializer.is_valid(raise_exception = True)
        print(serializer.is_valid)
        self.update_function(serializer)   #calling the function with the data that is to be updated
        return Response({"message":"success"},status=status.HTTP_201_CREATED)
    def update_function(self,serializer):
        serializer.save()
 
 





# user management by admin view

class User_management(APIView):
    def get(self,request):
        users = CustomUser.objects.filter(is_superuser = False)
        serializer = CustomUserSerializer(users, many=True)
        return Response({'message':"success","users":serializer.data})
    def put(self,request):
        header = request.data["headers"]
        operation_type = header['type']
        user_id = header['user_id']
        user = CustomUser.objects.get(id = user_id)
        if operation_type == "block":
            user.is_blocked = True
        if operation_type == "unblock":
            user.is_blocked = False
        user.save()
        return Response({'message':"success"})
    
    
  


# paymentintent function for the payment


stripe.api_key = settings.STRIPE_SECRET_KEY

class Create_payment_intent(APIView):
    def post(self,request,validity_months):
        details_header_value = request.headers.get('details', None)
        print("HEADER VALUE",details_header_value)
        if details_header_value is  not None:
            payment_type = 'upgrade'
        else:
            payment_type = 'normal'


        token = request.headers.get('Authorization')
        user_id ,email = convertjwt(token)
        plan = Subscription.objects.get(vlalidity_months = validity_months)
  
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': plan.stripe_price_id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                

                success_url= f'http://127.0.0.1:8000/adminapp/payment-success/{user_id}/{plan.id}/?{urlencode({"session_id": "{{CHECKOUT_SESSION_ID}}", "payment_type": payment_type ,"validity_months":validity_months})}',
                cancel_url=f"{os.getenv('frontendUrl')}subscriptions"
            )
        except Exception as e:
            return str(e)
        return Response({'sessionId': checkout_session['id']},status=status.HTTP_200_OK)
        

# payment succesfull view

class PaymentSuccessfull(APIView):
    def get(self,request,user_id,plan_id):
        payment_type = request.GET.get('payment_type')
        print('payment type',payment_type)
        validity_months = request.GET.get('validity_months')
        session_id = request.GET.get("session_id")
        # upgrading plan
        if payment_type == "upgrade":
            current_plan = SubscriptionDetails.objects.get(user_id = user_id)
            print(current_plan)
            plan = Subscription.objects.get(vlalidity_months = validity_months)
            print(plan.amount)
            current_plan.expiry_date += timedelta(days = 30 *plan.vlalidity_months)
            current_plan.plan_id = plan_id
            current_plan.save()
            return redirect(f"{os.getenv('frontendUrl')}thanks?payment_success=true&session_id={session_id}") 
        # adding new plan
        current_date = timezone.now().date()
        plan_details = Subscription.objects.get(id  = plan_id)
        expiry_date  = current_date + timedelta(days=30 * plan_details.vlalidity_months )

        data = {
            "user_id" : user_id,
            "plan" : plan_id,
            "date_started" : current_date,
            'expiry_date' : expiry_date,
            "payment_session_id":session_id
        }
        user = CustomUser.objects.get(id = user_id)
        user.subscribed = True
        user.save()

        serializer = Subscribed_user_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print('some error occured')
        return redirect(f"{os.getenv('frontendUrl')}thanks?payment_success=true&session_id={session_id}") 
    
        
        

# getting the details of subscription for each users
class Subscription_details(APIView):
    def get(self,request):
        token = request.headers.get('Authorization')
        user_id ,email = convertjwt(token)
        current_user = CustomUser.objects.get(id = user_id)
        if not current_user.subscribed:
            queryset = Subscription.objects.all()
            serializer = Retrive_delete_subscription(queryset,many=True)
            return Response({"message":"not_subscribed",'subscription_details':serializer.data})
        else :
            subscription_details = SubscriptionDetails.objects.get(user_id = current_user)
            plan_details = Subscription.objects.get(id = subscription_details.plan_id)
            plan_details_serializer = Retrive_delete_subscription(plan_details)
            serializer = Subscribed_user_serializer(subscription_details)
            print(serializer.data)
            return Response({"message":"subscription_details",'subscription_details':serializer.data,"plan_details":plan_details_serializer.data})
    def patch(self,request):
        token = request.headers.get("Authorization")
        user_id ,email = convertjwt(token)
        current_user = CustomUser.objects.get(id = user_id)
        return Response({'message':"success"})



        
    

