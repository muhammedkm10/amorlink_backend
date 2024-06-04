from django.urls import path
from . import views

urlpatterns = [
    path('add_edit_subscription',views.Add_List_subscription.as_view(),name="add_list_subscription"),
    path('add_edit_subscription/<int:pk>/',views.Add_List_subscription.as_view(),name='edit_subscription'),

    path('usermanagement',views.User_management.as_view())

    
]