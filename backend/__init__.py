from .celery import app as celery_app

__all__ = ('celery_app',)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()