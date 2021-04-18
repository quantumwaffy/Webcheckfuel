from .views import home, about
from django.urls import path


urlpatterns = [
    path('home/', home, name="home"),
    path('about/', about)
]