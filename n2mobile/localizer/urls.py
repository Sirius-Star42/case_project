from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
from .views import Home, loginPage, registerPage, logoutUser

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('login/', loginPage, name="login"),
    path('register/', registerPage, name="register"),
    path('logout/', logoutUser, name="logout"),
]