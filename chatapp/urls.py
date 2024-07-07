from django.urls import path
from .views import MatchedUsersForChat,Notification_view


urlpatterns = [
    path("get_useer_chat/<str:userid>/<str:reciverid>",MatchedUsersForChat.as_view()),
    path("notification/<int:sender>/<int:reciverid>",Notification_view.as_view(),name="notification_url"),
    path("notification",Notification_view.as_view())

]



