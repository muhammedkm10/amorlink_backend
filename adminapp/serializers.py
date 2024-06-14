from rest_framework.serializers import ModelSerializer
from .models import Subscription,SubscriptionDetails



# adding and  updating excluding the two colums
class Add_Update_subscription(ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ['no_users']
 


# retriving and deleting the data from the data base
class Retrive_delete_subscription(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

# subscribed user details serializer

class Subscribed_user_serializer(ModelSerializer):
    class Meta:
        model = SubscriptionDetails
        fields = '__all__'