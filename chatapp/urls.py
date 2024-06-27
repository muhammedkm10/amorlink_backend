from django.urls import path
from .views import MatchedUsersForChat,Notification


urlpatterns = [
    path("get_useer_chat/<int:userid>/<int:reciverid>",MatchedUsersForChat.as_view()),
    path("notification/<int:sender>/<int:reciverid>",Notification.as_view(),name="notification_url")
]



