from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("user/", views.user, name="user"),
    path("settings/", views.settings, name="settings"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("skating/", views.skating, name="skating"),
]