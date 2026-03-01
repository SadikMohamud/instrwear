from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SHOPPER = "shopper", "Shopper"
        MERCHANT = "merchant", "Merchant"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SHOPPER,
    )

    def __str__(self):
        return self.username



class MerchantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "merchant_profile",)
    business_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.business_name or f"MerchantProfile:{self.user.username}" 