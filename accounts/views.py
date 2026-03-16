"""
Author: Sadik Mohamud
Project: InstrWear
File: accounts/views.py
Purpose: Authentication and registration controllers
Framework: Django

Handles:
- Login
- Logout
- Shopper registration
- Merchant registration
- Welcome emails
- Role-based routing
"""

# ============================================================
# Imports
# ============================================================

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.timezone import now

User = get_user_model()


# ============================================================
# Welcome Email
# ============================================================

def send_welcome_email(to_email: str, request):
    """
    Sends a welcome email after successful registration.
    """

    subject = "Welcome to InstrWear"

    login_url = request.build_absolute_uri("/accounts/login/")

    html = render_to_string(
        "emails/welcome.html",
        {
            "email": to_email,
            "login_url": login_url,
            "year": now().year,
        },
    )

    msg = EmailMultiAlternatives(
        subject,
        "",
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
    )

    msg.attach_alternative(html, "text/html")
    msg.send()


# ============================================================
# Login Controller
# ============================================================

def login_view(request):
    """
    Handles login for all users.

    Role redirect logic:
    Admin     → Django admin
    Merchant  → Merchant dashboard
    Shopper   → Shopper dashboard
    """

    role = (request.GET.get("role") or request.POST.get("role") or "shopper").lower()

    if role not in ["shopper", "merchant"]:
        role = "shopper"

    if request.method == "POST":

        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        user = authenticate(request, username=email, password=password)

        if user is None:
            messages.error(request, "Invalid credentials.")
            return render(request, "accounts/login.html", {"role": role})

        # Log the user in
        login(request, user)

        messages.success(request, "Logged in successfully.")

        # ============================================================
        # Role-based redirect
        # ============================================================

        # Platform admin / Django superuser
        if user.is_superuser or user.role == "admin":
            return redirect("/admin/")

        # Merchant dashboard
        if user.role == "merchant":
            return redirect("merchant_dashboard")

        # Shopper dashboard
        return redirect("shopper_dashboard")

    return render(request, "accounts/login.html", {"role": role})


# ============================================================
# Logout Controller
# ============================================================

def logout_view(request):
    """
    Logs user out and redirects to landing page.
    """

    logout(request)

    messages.info(request, "Logged out.")

    return redirect("landing")


# ============================================================
# Register Choice
# ============================================================

def register_choice(request):
    """
    Page allowing user to choose shopper or merchant account.
    """

    return render(request, "accounts/register_choice.html")


# ============================================================
# Shopper Registration
# ============================================================

def register_shopper(request):
    """
    Handles shopper account registration.
    """

    if request.method == "POST":

        email = (request.POST.get("email") or "").strip().lower()
        password = request.POST.get("password") or ""

        if User.objects.filter(email=email).exists():
            messages.error(request, "That email is already registered. Try logging in.")
            return render(request, "accounts/register_shopper.html")

        user = User.objects.create_user(
            email=email,
            password=password,
            role="shopper",
        )

        send_welcome_email(user.email, request)

        login(request, user)

        messages.success(request, "Welcome to InstrWear! Check your email.")

        return redirect("shopper_onboarding")

    return render(request, "accounts/register_shopper.html")


# ============================================================
# Merchant Registration
# ============================================================

def register_merchant(request):
    """
    Handles merchant account registration.
    """

    if request.method == "POST":

        email = (request.POST.get("email") or "").strip().lower()
        password = request.POST.get("password") or ""

        if User.objects.filter(email=email).exists():
            messages.error(request, "That email is already registered. Try logging in.")
            return render(request, "accounts/register_merchant.html")

        user = User.objects.create_user(
            email=email,
            password=password,
            role="merchant",
        )

        send_welcome_email(user.email, request)

        login(request, user)

        messages.success(request, "Welcome to InstrWear! Check your email.")

        return redirect("merchant_onboarding")

    return render(request, "accounts/register_merchant.html")


# ============================================================
# Access Choice (Login vs Register selection page)
# ============================================================

def access_choice(request, role):
    """
    Displays login/register options depending on selected role.
    """

    role = role.lower()

    if role not in ["shopper", "merchant"]:
        role = "shopper"

    return render(request, "accounts/access_choice.html", {"role": role})