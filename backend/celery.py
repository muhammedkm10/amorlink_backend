from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery("backend")

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule={
'send-mail-everyday-at-12':{
        'task':'adminapp.tasks.subscription_expiring_email',
        'schedule': crontab(hour=0,minute=1),
        
    }

}