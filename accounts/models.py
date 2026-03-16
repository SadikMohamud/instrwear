"""
Author: Sadik Mohamud
Project: InstrWear
File: accounts/models.py
Purpose: Defines custom authentication system and profile models
Framework: Django

InstrWear supports three user roles:
1. Admin – platform administrator / superuser
2. Shopper – customers buying clothing
3. Merchant – businesses selling clothing

Each role has its own profile model storing additional data
such as address, phone number, profile image, and branding.
"""

# Django settings import (used to reference the AUTH_USER_MODEL safely)
from django.conf import settings

# Base classes used to build a custom authentication model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Core Django ORM model system
from django.db import models


# ============================================================
# Custom User Manager
# ============================================================

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.

    Handles:
    - Creating normal users
    - Creating superusers
    """

    def create_user(self, email, password=None, role="shopper", **extra_fields):
        """
        Creates and saves a standard user.

        Parameters
        ----------
        email : str
            Unique email used for login
        password : str
            User password
        role : str
            One of: 'admin', 'shopper', or 'merchant'
        """

        # Email is required for authentication
        if not email:
            raise ValueError("Email is required")

        # Normalize email format
        email = self.normalize_email(email)

        # Create user instance
        user = self.model(email=email, role=role, **extra_fields)

        # Hash password securely
        user.set_password(password)

        # Save user to database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates an admin (superuser).

        Superusers automatically receive:
        - admin panel access
        - full permissions
        - admin role inside the InstrWear application
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            email=email,
            password=password,
            role="admin",
            **extra_fields
        )


# ============================================================
# Custom User Model
# ============================================================

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom authentication model for InstrWear.

    Uses email instead of username for login.
    Supports multiple user roles.
    """

    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        SHOPPER = "shopper", "Shopper"
        MERCHANT = "merchant", "Merchant"

    # Unique login identifier
    email = models.EmailField(unique=True)

    # User's real name
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)

    # Determines whether user is admin, shopper or merchant
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SHOPPER
    )

    # Required authentication fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Attach custom manager
    objects = CustomUserManager()

    # Email replaces username for login
    USERNAME_FIELD = "email"

    # No additional required fields when creating superuser
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        """
        Ensure Django superusers always use the admin role.

        This keeps Django's built-in admin permissions aligned
        with the app-level role used inside InstrWear.
        """

        if self.is_superuser:
            self.role = self.Role.ADMIN
            self.is_staff = True

        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the user.
        Shows full name if available, otherwise email.
        """

        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or self.email


# ============================================================
# Shopper Profile Model
# ============================================================

class ShopperProfile(models.Model):
    """
    Stores additional information for shoppers.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="shopper_profile",
    )

    # Optional profile picture
    profile_image = models.ImageField(
        upload_to="shopper_profiles/",
        blank=True,
        null=True
    )

    # Contact information
    phone = models.CharField(max_length=20, blank=True)

    # Address fields
    house = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120, blank=True)
    county = models.CharField(max_length=120, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"ShopperProfile: {self.user.email}"


# ============================================================
# Merchant Profile Model
# ============================================================

class MerchantProfile(models.Model):
    """
    Stores business information for merchants.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="merchant_profile",
    )

    # Business details
    business_name = models.CharField(max_length=255, blank=True)

    # Optional brand logo
    logo = models.ImageField(
        upload_to="merchant_logos/",
        blank=True,
        null=True
    )

    # Contact number
    phone = models.CharField(max_length=20, blank=True)

    # Business address
    house = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120, blank=True)
    county = models.CharField(max_length=120, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    # Merchant bio / shop description
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.business_name or f"MerchantProfile: {self.user.email}"