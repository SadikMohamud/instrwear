from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def landing(request):
    return render(request, "pages/landing.html")


def choose_role(request):
    return render(request, "pages/choose_role.html")


@login_required
def shopper_onboarding(request):
    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    if request.method == "POST":
        return redirect("shopper_dashboard")

    return render(request, "shopper/onboarding.html")


@login_required
def merchant_onboarding(request):
    if request.user.role != "merchant":
        messages.error(request, "Access denied.")
        return redirect("landing")

    if request.method == "POST":
        return redirect("merchant_dashboard")

    return render(request, "merchant/onboarding.html")


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

    return render(request, "merchant/dashboard.html")


@login_required
def shopper_orders(request):
    if request.user.role != "shopper":
        messages.error(request, "Access denied.")
        return redirect("landing")

    return render(request, "shopper/orders.html")