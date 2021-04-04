from django.contrib import admin

# Register your models here.
from .models import Train
from .models import Locomotive



class LocomotiveAdmin(admin.ModelAdmin):
    list_display = ('name','f_crit', 'weight', 'calc_speed', 'length', 'type_loc_el')
    list_display_links = ('f_crit', 'weight', 'calc_speed', 'length', 'type_loc_el')
    search_fields = ('name',)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('ip','num','op_st','op_name','op_dt','vag_all','loc_ser','loc_num')
    list_display_links = ('num','op_st' )
    search_fields = ('num','op_st','loc_num')

admin.site.register(Train,TrainAdmin)
admin.site.register(Locomotive,LocomotiveAdmin)
