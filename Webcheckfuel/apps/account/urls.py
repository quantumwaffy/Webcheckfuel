from .views import *
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', user_login, name="auth"),
    ]
