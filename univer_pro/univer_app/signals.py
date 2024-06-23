import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

@receiver(post_save, sender=Student)
def generate_verification_code(sender, instance, created, **kwargs):
    if created:
        instance.verification_code = ''.join(random.choices('0123456789', k=6))
        instance.save()
