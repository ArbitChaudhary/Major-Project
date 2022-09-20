from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.user_registration, name="user_registration"),
    path("login", views.user_login, name="user_login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("", views.logOut, name="logout")
]