from django.db import models

class Train (models.Model):
    ip = models.CharField(max_length=16, verbose_name= 'Train ID')
    num = models.CharField(max_length=6, verbose_name= 'Train Number')
    op_st = models.CharField(max_length=6, verbose_name= 'Station of Operation')
    op_name = models.CharField(max_length=6, verbose_name= 'Name of Operation')
    op_dt = models.DateTimeField(db_index=True, verbose_name= 'Time and Date of Operation')
    vag_all = models.IntegerField(verbose_name= 'Count of all vagons')
    vag_h = models.IntegerField(verbose_name= 'Count of heavy vagons')
    vag_l = models.IntegerField(verbose_name= 'Count of light vagons')
    loc_ser = models.CharField(max_length=6, verbose_name= 'Locomotive series')
    loc_num = models.CharField(max_length=6, verbose_name= 'Locomotive number')
    parse_dt = models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name= 'Parsing datetime')

    class Meta:
        verbose_name_plural = 'Trains'
        verbose_name = 'Train'
        ordering = ['-parse_dt']


class Locomotive (models.Model):
    name = models.CharField(max_length=10, verbose_name= 'Name')
    f_crit = models.FloatField(verbose_name= 'Critical power, N')
    weight = models.FloatField(verbose_name= 'Weight, t')
    calc_speed = models.FloatField(verbose_name= 'Calculation speed, km / h')
    length = models.FloatField(verbose_name= 'Length, m')
    type_loc_el = models.BooleanField(verbose_name= 'is the electric traction')

    class Meta:
        verbose_name_plural = 'Locomotives'
        verbose_name = 'Locomotive'

