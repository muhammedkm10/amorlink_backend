from django.urls import path
from . import views

urlpatterns = [
    path('add_edit_subscription',views.Add_List_subscription.as_view(),name="add_list_subscription"),
    path('add_edit_subscription/<int:pk>/',views.Add_List_subscription.as_view(),name='edit_subscription'),
    path('usermanagement',views.User_management.as_view()),


    # payment gateway urls

    path("create_checkout_session/<int:validity_months>",views.Create_payment_intent.as_view()),

    # payment succesfull
    path('payment-success/<int:user_id>/<int:plan_id>/',views.PaymentSuccessfull.as_view()),

    # subscription details user side
    path('subscription_details',views.Subscription_details.as_view()),
    

    
]
