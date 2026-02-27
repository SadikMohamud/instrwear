from django.shortcuts import render

# Create your views here.

def login_view(request):
    role = (request.GET.get("role") or "shopper").lower()
    if role not in ["shopper", "merchant"]:
        role = "shopper"
    return render(request, "accounts/login.html", {"role": role})