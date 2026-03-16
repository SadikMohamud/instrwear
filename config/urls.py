"""
Author: Sadik Mohamud
Project: InstrWear
File: config/urls.py
Purpose: Main URL routing for public pages, authentication, dashboards, marketplace, cart, checkout, and media files
Framework: Django
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import (
    landing,
    choose_role,
    shopper_onboarding,
    merchant_onboarding,
    shopper_dashboard,
    merchant_dashboard,
    shopper_orders,
)

from accounts.views import (
    login_view,
    logout_view,
    register_choice,
    register_shopper,
    register_merchant,
)

from marketplace.views import (
    merchant_product_list,
    merchant_add_product,
    shopper_product_list,
    shopper_product_detail,
    cart_view,
    add_to_cart,
    update_cart_item,
    remove_cart_item,
    checkout_view,
    checkout_success,
    checkout_cancel,
    stripe_webhook,
)

urlpatterns = [
    # ============================================================
    # Django Admin
    # ============================================================
    path("admin/", admin.site.urls),

    # ============================================================
    # Public Routes
    # ============================================================
    path("", landing, name="landing"),
    path("choose-role/", choose_role, name="choose_role"),

    # ============================================================
    # Authentication Routes
    # ============================================================
    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register/", register_choice, name="register_choice"),
    path("accounts/register/shopper/", register_shopper, name="register_shopper"),
    path("accounts/register/merchant/", register_merchant, name="register_merchant"),

    # ============================================================
    # Shopper Routes
    # ============================================================
    path("shopper/dashboard/", shopper_dashboard, name="shopper_dashboard"),
    path("shopper/orders/", shopper_orders, name="shopper_orders"),
    path("shopper/onboarding/", shopper_onboarding, name="shopper_onboarding"),
    path("shopper/products/", shopper_product_list, name="shopper_product_list"),
    path("shopper/products/<slug:slug>/", shopper_product_detail, name="shopper_product_detail"),

    # ============================================================
    # Merchant Routes
    # ============================================================
    path("merchant/dashboard/", merchant_dashboard, name="merchant_dashboard"),
    path("merchant/onboarding/", merchant_onboarding, name="merchant_onboarding"),
    path("merchant/products/", merchant_product_list, name="merchant_products"),
    path("merchant/products/add/", merchant_add_product, name="merchant_add_product"),

    # ============================================================
    # Cart Routes
    # ============================================================
    path("shopper/cart/", cart_view, name="cart_view"),
    path("shopper/cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("shopper/cart/item/<int:item_id>/update/", update_cart_item, name="update_cart_item"),
    path("shopper/cart/item/<int:item_id>/remove/", remove_cart_item, name="remove_cart_item"),

    # ============================================================
    # Checkout / Payment Routes
    # ============================================================
    path("shopper/checkout/", checkout_view, name="checkout_view"),
    path("shopper/checkout/success/", checkout_success, name="checkout_success"),
    path("shopper/checkout/cancel/", checkout_cancel, name="checkout_cancel"),

    # ============================================================
    # Stripe Webhook
    # ============================================================
    path("stripe/webhook/", stripe_webhook, name="stripe_webhook"),
]

# ============================================================
# Media files (development only)
# ============================================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)