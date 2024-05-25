from django.urls import path
from . import views
from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView,)
from.views import CustomTokenObtainPairView



urlpatterns = [
    # jwt urls
    path('api/token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),



    # other urls
    path('usersignup',views.UserRegistration().as_view()),
    path('otpverification',views.Otpverificaion().as_view()),
    path('userlogin',views.Login().as_view()),


    
]

