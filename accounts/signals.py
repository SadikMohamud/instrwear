"""
accounts/signals.py

Automatically create shopper or merchant profile
when a new user registers.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ShopperProfile, MerchantProfile
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profiles(sender, instance, created, **kwargs):

    if created:

        if instance.role == "shopper":
            ShopperProfile.objects.create(user=instance)

        elif instance.role == "merchant":
            MerchantProfile.objects.create(
                user=instance,
                business_name=f"{instance.first_name}'s Store"
            )