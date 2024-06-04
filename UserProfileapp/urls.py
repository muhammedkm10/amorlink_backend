from django.urls import path
from . import views

urlpatterns = [
    path('profiledetails',views.UserProfileDetails.as_view()),
    path('preferences',views.ShowPreferences.as_view())
    
    
]