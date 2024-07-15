import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chatapp.routing import websocket_urlpatterns
application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')


application = ProtocolTypeRouter({
    'http': application,
    'websocket': URLRouter(websocket_urlpatterns),
})
