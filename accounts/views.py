from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.timezone import now

User = get_user_model()


def send_welcome_email(to_email: str, request):
    subject = "Welcome to InstrWear"
    login_url = request.build_absolute_uri("/accounts/login/")
    html = render_to_string("emails/welcome.html", {
        "email": to_email,
        "login_url": login_url,
        "year": now().year,
    })
    msg = EmailMultiAlternatives(subject, "", settings.DEFAULT_FROM_EMAIL, [to_email])
    msg.attach_alternative(html, "text/html")
    msg.send()


def login_view(request):
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

        login(request, user)
        messages.success(request, "Logged in successfully.")
        if user.role == "merchant":
            return redirect("merchant_dashboard")
        return redirect("shopper_dashboard")

    return render(request, "accounts/login.html", {"role": role})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("landing")


def register_choice(request):
    return render(request, "accounts/register_choice.html")


def register_shopper(request):
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
        return redirect("shopper_dashboard")

    return render(request, "accounts/register_shopper.html")


def register_merchant(request):
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
        return redirect("merchant_dashboard")

    return render(request, "accounts/register_merchant.html")