# Generated by Django 3.2.4 on 2021-08-21 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0005_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='locomotive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trains', to='parsing.locomotive'),
        ),
    ]