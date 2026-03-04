from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

User = get_user_model()


# Create your views here.

def login_view(request):
    role = (request.GET.get("role") or request.POST.get("role") or "shopper").lower()
    if role not in ["shopper", "merchant"]:
        role = "shopper"

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

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
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            password=password,
            role="shopper"
        )

        login(request, user)
        return redirect("shopper_dashboard")

    return render(request, "accounts/register_shopper.html")


def register_merchant(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            password=password,
            role="merchant"
        )

        login(request, user)
        return redirect("merchant_dashboard")

    return render(request, "accounts/register_merchant.html")