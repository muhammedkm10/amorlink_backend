from django.urls import path
from . import views

urlpatterns = [
    path('add_edit_subscription',views.Add_List_subscription.as_view()),
    path('usermanagement',views.User_management.as_view())

    
]