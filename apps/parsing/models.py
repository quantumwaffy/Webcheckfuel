from django.db import models


class Train(models.Model):
    locomotive = models.ForeignKey(
        "Locomotive",
        related_name="trains",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    ip = models.CharField(max_length=16, verbose_name="Train ID")
    num = models.CharField(max_length=6, verbose_name="Train Number")
    op_st = models.CharField(max_length=6, verbose_name="Station of Operation")
    op_name = models.CharField(max_length=6, verbose_name="Name of Operation")
    op_dt = models.DateTimeField(db_index=True, verbose_name="Time and Date of Operation")
    vag_all = models.IntegerField(verbose_name="Count of all vagons")
    vag_h = models.IntegerField(verbose_name="Count of heavy vagons")
    vag_l = models.IntegerField(verbose_name="Count of light vagons")
    loc_ser = models.CharField(max_length=6, verbose_name="Locomotive series", null=True, blank=True)
    loc_num = models.CharField(max_length=6, verbose_name="Locomotive number", null=True, blank=True)
    parse_dt = models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name="Parsing datetime")

    def __str__(self):
        return self.num

    class Meta:
        verbose_name_plural = "Trains"
        verbose_name = "Train"
        ordering = ["-parse_dt"]


class Locomotive(models.Model):
    name = models.CharField(max_length=6, verbose_name="Name")
    f_crit = models.FloatField(verbose_name="Critical power, N")
    weight = models.FloatField(verbose_name="Weight, t")
    calc_speed = models.FloatField(verbose_name="Calculation speed, km / h")
    length = models.FloatField(verbose_name="Length, m")
    type_loc_el = models.BooleanField(verbose_name="electric")
    loc_ser = models.CharField(max_length=6, verbose_name="Locomotive series", null=True, blank=True)
    loc_num = models.CharField(max_length=6, verbose_name="Locomotive number", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Locomotives"
        verbose_name = "Locomotive"


class Sector(models.Model):
    train = models.ForeignKey(Train, related_name="sectors", on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Sector name")
    number = models.IntegerField(verbose_name="Sector number", db_index=True)
    calcskew = models.FloatField(verbose_name="Calculation skew")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sectors"
        verbose_name = "Sector"
        ordering = ["-calcskew"]


class UploadedFile(models.Model):
    file = models.FileField(upload_to="media/uploaded_files", verbose_name="Files")
    name = models.CharField(max_length=255, verbose_name="File name")
    uploaded_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Uploaded datetime")
