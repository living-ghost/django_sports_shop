from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Register, Subscriber

# Imports Supporting OTP Verification

import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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

def send_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            messages.error(request, "Email is required!")
            return redirect('index')
        
        otp = str(random.randint(100000, 999999))

        request.session['otp'] = otp
        request.session['email'] = email
        request.session.set_expiry(300)
        
        try:
            send_mail(
                subject="Your OTP for Subscription",
                message=f"Your OTP is: {otp}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False
            )

            messages.success(request, "OTP sent to your email")

            return render(request, "sports_shop_app/verify_otp.html")
        
        except Exception as e:
            # Clear session if email fails
            if 'otp' in request.session:
                del request.session['otp']
            if 'email' in request.session:
                del request.session['email']

            messages.error(request, f"Failed to send OTP: {str(e)}")
            return redirect('index')

    return redirect('index')

def verify_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp", "").strip()
        stored_otp = request.session.get("otp")
        email = request.session.get("email")

        if not (user_otp and stored_otp and email):
            messages.error(request, "Invalid OTP or session expired!")
            return redirect('index')
        
        if user_otp == stored_otp:
            try:
                Subscriber.objects.create(subscriber_email=email, is_verified=True)
                messages.success(request, "Email verified and subscribed!")
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Invalid OTP!")

        del request.session['otp']
        del request.session['email']
        return redirect('index')
    
    return redirect('index')