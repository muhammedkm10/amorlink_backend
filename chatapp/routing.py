from django.urls import re_path
from .consumers import PersonalChatConsumer, NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/?$', PersonalChatConsumer.as_asgi()),
    re_path(r'ws/notification/?$', NotificationConsumer.as_asgi())
]