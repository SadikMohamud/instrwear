from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, role="shopper", **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            role=role,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            email=email,
            password=password,
            role="merchant",
            **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        SHOPPER = "shopper", "Shopper"
        MERCHANT = "merchant", "Merchant"

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SHOPPER
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    

class ShopperProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shopper_profile"
    )

    phone = models.CharField(max_length=20, blank=True)

    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)

    city = models.CharField(max_length=120, blank=True)

    postcode = models.CharField(max_length=10, blank=True)

    delivery_notes = models.TextField(blank=True)

    def __str__(self):
        return f"ShopperProfile: {self.user.email}"


class MerchantProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="merchant_profile",
    )

    business_name = models.CharField(max_length=255, blank=True)

    phone = models.CharField(max_length=20, blank=True)

    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)

    city = models.CharField(max_length=120, blank=True)

    postcode = models.CharField(max_length=10, blank=True)

    bio = models.TextField(blank=True)

    def __str__(self):
        return self.business_name or f"MerchantProfile: {self.user.email}"