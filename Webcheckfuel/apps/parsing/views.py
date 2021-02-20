
from django.shortcuts import render
from Webcheckfuel.apps.parsing.models import Train

def index(request):
    messages = Train.objects.all()
    return render(request, 'parsing/index.html', {'messages':messages})