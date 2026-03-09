from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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

def landing(request):
    return render(request, "core/landing_page.html")

def choose_role(request):
    return render(request, "pages/choose_role.html")