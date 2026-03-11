"""
marketplace/models.py

Core marketplace data models for InstrWear.

These models handle:
- product categories
- merchant product listings
- shopper carts
- orders and order items

The goal is to support the full flow:
Merchant adds product -> Shopper browses -> Adds to cart -> Places order
"""

# Django model utilities
from django.conf import settings
from django.db import models
from django.utils.text import slugify


# ============================================================
# Category Model
# ============================================================

class Category(models.Model):
    """
    Stores product categories such as:
    - Streetwear
    - Footwear
    - Accessories
    - Womenswear
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Automatically create a slug from the category name
        if one has not been provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ============================================================
# Product Model
# ============================================================

class Product(models.Model):
    """
    Stores merchant product listings.

    Each product belongs to:
    - one merchant user
    - one category

    Products are what shoppers will browse and buy.
    """

    merchant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="products"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products"
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to="products/", blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Automatically generate a unique-looking slug from the product name
        if one does not already exist.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ============================================================
# Cart Model
# ============================================================

class Cart(models.Model):
    """
    One cart per shopper.

    This gives each logged-in shopper a basket
    they can add products to before checkout.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        """
        Calculate the full cart total by summing all cart items.
        """
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f"Cart: {self.user.email}"


# ============================================================
# Cart Item Model
# ============================================================

class CartItem(models.Model):
    """
    Individual product line inside a cart.
    """

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "product")

    def subtotal(self):
        """
        Return quantity multiplied by product price.
        """
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


# ============================================================
# Order Model
# ============================================================

class Order(models.Model):
    """
    Stores a completed shopper order.

    This is created during checkout.
    """

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        SHIPPED = "shipped", "Shipped"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)

    house = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120, blank=True)
    county = models.CharField(max_length=120, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"


# ============================================================
# Order Item Model
# ============================================================

class OrderItem(models.Model):
    """
    Stores each product that belongs to an order.

    This keeps a snapshot of the product name and price at time of purchase.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_items"
    )

    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        """
        Return line total for this order item.
        """
        return self.product_price * self.quantity

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"


# ============================================================
# File Metadata
# ============================================================

"""
Author: Sadik Mohamud
Project: InstrWear
File: marketplace/models.py
Purpose: Marketplace, cart, and order data models
Framework: Django
"""