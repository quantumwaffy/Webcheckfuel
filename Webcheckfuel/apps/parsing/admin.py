from django.contrib import admin

# Register your models here.
from .models import Train
from .models import Locomotive

admin.site.register(Train)
admin.site.register(Locomotive)