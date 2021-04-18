from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')
