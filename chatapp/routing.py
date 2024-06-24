from django.urls import re_path
from .consumers import PersonalChatConsumer

websocket_urlpatterns = [
    re_path('ws/chat/', PersonalChatConsumer.as_asgi()),

]