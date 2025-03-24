from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "sports_shop_app/index.html")

def about(request):
    return render(request, "sports_shop_app/about.html")

def contact(request):
    return render(request, "sports_shop_app/contact.html")

def shop(request):
    return render(request, "sports_shop_app/shop.html")

def skating(request):
    return render(request, "sports_shop_app/skating.html")

def login(request):
    return render(request, "sports_shop_app/login.html")

def register(request):
    return render(request, "sports_shop_app/register.html")

def profile(request):
    return render(request, "sports_shop_app/profile.html")

def settings(request):
    return render(request, "sports_shop_app/settings.html")

def logout(request):
    return render(request, "sports_shop_app/logout.html")
