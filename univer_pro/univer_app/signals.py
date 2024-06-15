# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Student

@receiver(post_save, sender=Student)
def notify_admin_new_student(sender, instance, created, **kwargs):
    if created:
        # Уведомление администратору
        send_mail(
            'New Student Registration',
            f'A new student {instance.user.username} has registered. Please review and approve.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
