from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Subscription
from .serializers import  Add_Update_subscription,Retrive_delete_subscription
from authapp.models import CustomUser
from authapp.serializers import CustomUserSerializer
from rest_framework import status

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
    
    
  

    

  
    