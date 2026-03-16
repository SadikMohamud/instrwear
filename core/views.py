"""
Author: Sadik Mohamud
Project: InstrWear
File: core/views.py
Purpose: Core views for public pages, onboarding, dashboards, and shopper orders
Framework: Django
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import MerchantProfile, ShopperProfile
from marketplace.forms import ProductForm
from marketplace.models import Order, Product


def landing(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.role == "admin":
            return redirect("/admin/")

        if request.user.role == "merchant":
            return redirect("merchant_dashboard")

        if request.user.role == "shopper":
            return redirect("shopper_dashboard")

    return render(request, "pages/landing.html")


def choose_role(request):
    return redirect("register_choice")


@login_required
def shopper_onboarding(request):
    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    profile, _ = ShopperProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        request.user.first_name = (request.POST.get("first_name") or "").strip()
        request.user.last_name = (request.POST.get("last_name") or "").strip()
        request.user.save()

        profile.phone = (request.POST.get("phone") or "").strip()
        profile.house = (request.POST.get("house") or "").strip()
        profile.street = (request.POST.get("street") or "").strip()
        profile.city = (request.POST.get("city") or "").strip()
        profile.county = (request.POST.get("county") or "").strip()
        profile.postcode = (request.POST.get("postcode") or "").strip()

        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES.get("profile_image")

        profile.save()

        messages.success(request, f"Welcome {request.user.first_name} to InstrWear.")
        return redirect("shopper_dashboard")

    return render(request, "shopper/onboarding.html", {"profile": profile})


@login_required
def merchant_onboarding(request):
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    merchant, _ = MerchantProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        request.user.first_name = (request.POST.get("first_name") or "").strip()
        request.user.last_name = (request.POST.get("last_name") or "").strip()
        request.user.save()

        merchant.business_name = (request.POST.get("business_name") or "").strip()
        merchant.phone = (request.POST.get("phone") or "").strip()
        merchant.house = (request.POST.get("house") or "").strip()
        merchant.street = (request.POST.get("street") or "").strip()
        merchant.city = (request.POST.get("city") or "").strip()
        merchant.county = (request.POST.get("county") or "").strip()
        merchant.postcode = (request.POST.get("postcode") or "").strip()
        merchant.bio = (request.POST.get("bio") or "").strip()

        if request.FILES.get("logo"):
            merchant.logo = request.FILES.get("logo")

        merchant.save()

        messages.success(request, f"Welcome {request.user.first_name} to InstrWear.")
        return redirect("merchant_dashboard")

    return render(request, "merchant/onboarding.html", {"merchant": merchant})


@login_required
def shopper_dashboard(request):
    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    return render(request, "shopper/dashboard.html")


@login_required
def merchant_dashboard(request):
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    merchant_profile, _ = MerchantProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.merchant = request.user
            product.save()

            messages.success(request, f"{product.name} was added successfully.")
            return redirect("merchant_dashboard")
    else:
        form = ProductForm()

    products = Product.objects.filter(merchant=request.user).order_by("-created_at")

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


@login_required
def shopper_orders(request):
    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    orders = Order.objects.filter(user=request.user).prefetch_related("items").order_by("-created_at")

    return render(request, "shopper/orders.html", {"orders": orders})