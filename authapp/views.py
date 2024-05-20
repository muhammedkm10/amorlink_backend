from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.


class firstview(APIView):
    def get(self,request):
       return Response({"name":"muhammed"})

