from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def shopper_dashboard(request):
    if request.user.role != "shopper":
        messages.error(request, "Access denied (shopper only).")
        return redirect("landing")
    return render(request, "shopper/dashboard.html")

@login_required
def merchant_dashboard(request):
    if request.user.role != "merchant":
        messages.error(request, "Access denied (merchant only).")
        return redirect("landing")
    return render(request, "merchant/dashboard.html")