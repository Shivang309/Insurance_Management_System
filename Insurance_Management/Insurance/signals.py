from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import CustomerDetail
<<<<<<< HEAD
from .models import Appointment
from .emails import send_appointment_email

@receiver(post_save, sender=Appointment)
def appointment_approved(sender, instance, **kwargs):
    if instance.status == 'A' and kwargs.get('created', False) == False:  # Ensure it's an update and status is 'Accepted'
        send_appointment_email(instance)
=======

@receiver(post_save, sender=User)
def create_customer_detail(sender, instance, created, **kwargs):
    if created:
        CustomerDetail.objects.create(user=instance)
>>>>>>> 2208dcd45d8341d791f527e33c160cc3ac585651
