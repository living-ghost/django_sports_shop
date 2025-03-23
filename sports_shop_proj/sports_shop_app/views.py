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
