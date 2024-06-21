from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from.models import SubscriptionDetails
from django.core.mail import send_mail


@shared_task(bind=True)
def subscription_expiring_email(self):
    current_date = timezone.now()
    after_one_week = current_date + timedelta(days=7)
    plan_expiring_users = SubscriptionDetails.objects.filter(expiry_date__lte = after_one_week ,expiry_date__gte = current_date)
    expired_users = SubscriptionDetails.objects.filter(expiry_date = current_date)
    for i in expired_users:
        i.user_id.subscribed = False
        i.user_id.save()
    for i in plan_expiring_users:
        user_email = i.user_id.email
        send_mail(
            "Subscription expiring mail from AMORLINK matrimony",
            "Your plan will expire within few days .At AmorLink, we understand that finding a meaningful and lasting relationship requires the right tools and opportunities. While our free membership gives you access to basic features, upgrading to our Premium Subscription allows you to unlock the full potential of our platform, including the ability to request matches with your ideal partners.",
            'muhammedmamu2906@gmail.com',
            [user_email],
            fail_silently=False
            
        )
    return "Task Successfull"





