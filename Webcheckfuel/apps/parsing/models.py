from django.db import models

class Train (models.Model):
    ip = models.CharField(max_length=16)
    num = models.CharField(max_length=6)
    op_st = models.CharField(max_length=6)
    op_name = models.CharField(max_length=6)
    op_dt = models.DateTimeField(db_index=True)
    vag_all = models.IntegerField()
    vag_h = models.IntegerField()
    vag_l = models.IntegerField()
    loc_ser = models.CharField(max_length=6)
    loc_num = models.CharField(max_length=6)
    parse_dt = models.DateTimeField(auto_now_add=True, db_index=True, null=True)



class Locomotive (models.Model):
    f_crit = models.FloatField()
    weight = models.FloatField()
    calc_speed = models.FloatField()
    length = models.FloatField()
    type_loc_el = models.BooleanField()


