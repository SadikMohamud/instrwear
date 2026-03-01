from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import  settings

from .models import CustomUser, MerchantProfile 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_merchant_profile(sender, instance: CustomUser, created, **kwargs):
    if not created:
        return
    if instance.role == CustomUser.Role.MERCHANT:
        MerchantProfile.objects.create(user=instance)