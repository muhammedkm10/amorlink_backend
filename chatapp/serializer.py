from rest_framework.serializers import ModelSerializer
from .models import ChatMessages

class chatModelSerializer(ModelSerializer):
    class Meta:
        model = ChatMessages
        fields = '__all__'