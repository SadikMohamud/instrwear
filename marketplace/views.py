from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
def landing(request):
    return render(request, "pages/landing.html")