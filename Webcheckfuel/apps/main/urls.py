from .views import *
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', index, name="index"),
    path('', include('django.contrib.auth.urls'), name="auth"),
    path('home/', home, name="home"),
    path('about/', about)
]