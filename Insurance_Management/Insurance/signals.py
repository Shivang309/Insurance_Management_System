from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomerDetail

@receiver(post_save, sender=User)
def create_customer_detail(sender, instance, created, **kwargs):
    if created:
        CustomerDetail.objects.create(user=instance)
