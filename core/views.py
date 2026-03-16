"""
Author: Sadik Mohamud
Project: InstrWear
File: core/views.py
Purpose: Core views for public pages, onboarding, dashboards, and shopper orders
Framework: Django

Handles:
- landing page
- role selection
- shopper onboarding
- merchant onboarding
- shopper dashboard
- merchant dashboard
- shopper orders

The merchant dashboard also handles inline product creation
from the dashboard modal.
"""

# ============================================================
# Imports
# ============================================================

# Django messaging framework for user feedback
from django.contrib import messages

# Protect private pages from unauthenticated users
from django.contrib.auth.decorators import login_required

# Shortcut helpers for rendering templates and redirecting
from django.shortcuts import redirect, render

# Account profile models
from accounts.models import MerchantProfile, ShopperProfile

# Marketplace forms and models
from marketplace.forms import ProductForm
from marketplace.models import Product


# ============================================================
# Public Pages
# ============================================================

def landing(request):
    """
    Public landing page controller.

    Behaviour:
    - If user is not authenticated, show landing page
    - If user is admin, send them to Django admin
    - If user is merchant, send them to merchant dashboard
    - If user is shopper, send them to shopper dashboard
    """

    # Redirect authenticated users away from the public landing page
    if request.user.is_authenticated:

        # Django superusers / platform admins
        if request.user.is_superuser or request.user.role == "admin":
            return redirect("/admin/")

        # Merchant users
        if request.user.role == "merchant":
            return redirect("merchant_dashboard")

        # Shopper users
        if request.user.role == "shopper":
            return redirect("shopper_dashboard")

    # Public visitors see the landing page
    return render(request, "pages/landing.html")


def choose_role(request):
    """
    Role selection page.

    This view exists to support the route:
    /choose-role/

    For now, it sends users to the registration choice page.
    That keeps existing URLs working without breaking config/urls.py.
    """

    return redirect("register_choice")


# ============================================================
# Shopper Onboarding
# ============================================================

@login_required
def shopper_onboarding(request):
    """
    Shopper onboarding page.

    Saves:
    - shopper full name
    - phone number
    - UK address fields
    - optional profile image
    """

    # Prevent non-shoppers from accessing shopper onboarding
    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # Ensure shopper profile exists
    profile, _ = ShopperProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Split full name into first and last name
        full_name = (request.POST.get("full_name") or "").strip()
        if full_name:
            name_parts = full_name.split(maxsplit=1)
            request.user.first_name = name_parts[0]
            request.user.last_name = name_parts[1] if len(name_parts) > 1 else ""
            request.user.save()

        # Save shopper profile fields
        profile.phone = request.POST.get("phone", "").strip()
        profile.house = request.POST.get("house", "").strip()
        profile.street = request.POST.get("street", "").strip()
        profile.city = request.POST.get("city", "").strip()
        profile.county = request.POST.get("county", "").strip()
        profile.postcode = request.POST.get("postcode", "").strip()

        # Save optional image if uploaded
        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES.get("profile_image")

        profile.save()

        messages.success(request, f"Welcome {request.user.first_name} to InstrWear.")
        return redirect("shopper_dashboard")

    context = {
        "profile": profile,
    }

    return render(request, "shopper/onboarding.html", context)


# ============================================================
# Merchant Onboarding
# ============================================================

@login_required
def merchant_onboarding(request):
    """
    Merchant onboarding page.

    Saves:
    - merchant full name
    - business name
    - phone number
    - UK business address
    - bio
    - optional logo
    """

    # Prevent non-merchants from accessing merchant onboarding
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # Ensure merchant profile exists
    merchant, _ = MerchantProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Split full name into first and last name
        full_name = (request.POST.get("merchant_name") or "").strip()
        if full_name:
            name_parts = full_name.split(maxsplit=1)
            request.user.first_name = name_parts[0]
            request.user.last_name = name_parts[1] if len(name_parts) > 1 else ""
            request.user.save()

        # Save merchant profile fields
        merchant.business_name = request.POST.get("business_name", "").strip()
        merchant.phone = request.POST.get("phone", "").strip()
        merchant.house = request.POST.get("house", "").strip()
        merchant.street = request.POST.get("street", "").strip()
        merchant.city = request.POST.get("city", "").strip()
        merchant.county = request.POST.get("county", "").strip()
        merchant.postcode = request.POST.get("postcode", "").strip()
        merchant.bio = request.POST.get("bio", "").strip()

        # Save optional logo if uploaded
        if request.FILES.get("logo"):
            merchant.logo = request.FILES.get("logo")

        merchant.save()

        messages.success(request, f"Welcome {request.user.first_name} to InstrWear.")
        return redirect("merchant_dashboard")

    context = {
        "merchant": merchant,
    }

    return render(request, "merchant/onboarding.html", context)


# ============================================================
# Shopper Dashboard
# ============================================================

@login_required
def shopper_dashboard(request):
    """
    Shopper dashboard page.
    """

    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    return render(request, "shopper/dashboard.html")


# ============================================================
# Merchant Dashboard
# ============================================================

@login_required
def merchant_dashboard(request):
    """
    Merchant dashboard page.

    Handles:
    - displaying merchant inventory statistics
    - displaying merchant products
    - adding a new product through the dashboard modal
    """

    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    # Ensure merchant profile exists
    merchant_profile, _ = MerchantProfile.objects.get_or_create(user=request.user)

    # Handle Add Product modal submission
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)

            # Attach product to current merchant
            product.merchant = request.user
            product.save()

            messages.success(request, f"{product.name} was added successfully.")
            return redirect("merchant_dashboard")
    else:
        form = ProductForm()

    # Get this merchant's products
    products = Product.objects.filter(merchant=request.user).order_by("-created_at")

    # Calculate dashboard stats
    total_products = products.count()
    active_products = products.filter(is_active=True).count()
    low_stock_products = products.filter(stock__lt=10).count()
    inventory_value = sum(product.price * product.stock for product in products)

    context = {
        "merchant_profile": merchant_profile,
        "form": form,
        "products": products,
        "total_products": total_products,
        "active_products": active_products,
        "low_stock_products": low_stock_products,
        "inventory_value": inventory_value,
    }

    return render(request, "merchant/dashboard.html", context)


# ============================================================
# Shopper Orders
# ============================================================

@login_required
def shopper_orders(request):
    """
    Shopper order history page.
    """

    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    return render(request, "shopper/orders.html")