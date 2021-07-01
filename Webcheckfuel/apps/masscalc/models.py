from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=50, verbose_name="Sector name")
    number = models.IntegerField(verbose_name="Sector number", db_index=True)
    calcskew = models.FloatField(verbose_name="Calculation skew")

    class Meta:
        verbose_name_plural = "Sectors"
        verbose_name = "Sector"
        ordering = ["-calcskew"]
