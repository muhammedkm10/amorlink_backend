from  rest_framework import serializers
from .models import  MatchRequests


class MatchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchRequests
        fields = '__all__'
    