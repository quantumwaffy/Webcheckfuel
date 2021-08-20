from django.urls import path

from .views import about, home

urlpatterns = [path("home/", home, name="home"), path("about/", about)]
