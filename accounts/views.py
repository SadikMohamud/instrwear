from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

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
        # Temporary: go to landing for now
        if user.role == "merchant":
            return redirect("merchant_dashboard")
        return redirect("shopper_dashboard")

    return render(request, "accounts/login.html", {"role": role})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("landing")