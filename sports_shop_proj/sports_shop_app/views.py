from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Register


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

def user(request):
    return render(request, "sports_shop_app/user.html")

def profile(request):
    return render(request, "sports_shop_app/profile.html")

def settings(request):
    return render(request, "sports_shop_app/settings.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("loginEmail")
        password = request.POST.get("loginPassword")

        if not email or not password:
            return render(request, "sports_shop_app/index.html", {
                "error": "Both email and password are required"
            })

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('user')  # Update with your actual profile URL
        else:
            return render(request, "sports_shop_app/index.html", {
                "error": "Invalid email or password"
            })
    
    return render(request, "sports_shop_app/index.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("registerName")
        email = request.POST.get("registerEmail")
        password = request.POST.get("registerPassword")

        try:
            user = Register.objects.create_user(
                email=email,
                name=name,
                password=password
            )
            auth_login(request, user)
            return redirect('user')  # Update with your actual profile URL
        except Exception as e:
            return render(request, "sports_shop_app/index.html", {
                "error": str(e)
            })
    
    return render(request, "sports_shop_app/index.html")

def logout(request):
    auth_logout(request)
    return redirect('index')