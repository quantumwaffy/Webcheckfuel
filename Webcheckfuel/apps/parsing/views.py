
from django.shortcuts import render
from Webcheckfuel.apps.parsing.models import Train
from .main import main as go

def index(request):
    if request.user.is_authenticated:
        messages = Train.objects.all()
        return render(request, 'parsing/index.html', {'messages':messages})


