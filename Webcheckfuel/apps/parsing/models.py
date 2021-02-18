from django.db import models

class Trains (models.Model):
    ip = models.CharField(max_length=16)
    num = models.CharField(max_length=6)
    op_st = models.CharField(max_length=6)
    op_name = models.CharField(max_length=6)
    op_dt = models.DateTimeField(db_index=True)


