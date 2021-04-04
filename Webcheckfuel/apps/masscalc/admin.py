from django.contrib import admin
from .models import Sector

class SectorAdmin(admin.ModelAdmin):
    list_display = ('name','number', 'calcskew')
    list_display_links = ('name', 'number', 'calcskew')
    search_fields = ('name',)
admin.site.register(Sector,SectorAdmin)