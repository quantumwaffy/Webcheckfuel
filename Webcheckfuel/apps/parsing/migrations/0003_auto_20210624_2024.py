# Generated by Django 3.2.4 on 2021-06-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parsing", "0002_auto_20210621_2046"),
    ]

    operations = [
        migrations.AddField(
            model_name="locomotive",
            name="loc_num",
            field=models.CharField(
                blank=True, max_length=6, null=True, verbose_name="Locomotive number"
            ),
        ),
        migrations.AddField(
            model_name="locomotive",
            name="loc_ser",
            field=models.CharField(
                blank=True, max_length=6, null=True, verbose_name="Locomotive series"
            ),
        ),
        migrations.AlterField(
            model_name="locomotive",
            name="name",
            field=models.CharField(max_length=6, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="locomotive",
            name="type_loc_el",
            field=models.BooleanField(verbose_name="electric"),
        ),
        migrations.AlterField(
            model_name="train",
            name="loc_num",
            field=models.CharField(
                blank=True, max_length=6, null=True, verbose_name="Locomotive number"
            ),
        ),
        migrations.AlterField(
            model_name="train",
            name="loc_ser",
            field=models.CharField(
                blank=True, max_length=6, null=True, verbose_name="Locomotive series"
            ),
        ),
    ]
