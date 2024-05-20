from django.urls import path
from . import views

urlpatterns = [
    path('firsturl',views.firstview().as_view())
    
]