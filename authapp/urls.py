from django.urls import path
from . import views

urlpatterns = [
    path('usersignup',views.UserRegistration().as_view()),
    path('otpverification',views.Otpverificaion().as_view()),

    
]