from django.urls import path
from .views import MatchedUsersForChat


urlpatterns = [
    path("get_useer_chat/<int:userid>/<int:reciverid>",MatchedUsersForChat.as_view())
]

