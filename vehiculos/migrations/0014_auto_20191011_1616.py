# Generated by Django 2.2.5 on 2019-10-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0013_auto_20191011_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='vehiculos',
            field=models.ManyToManyField(blank=True, to='vehiculos.Vehiculo'),
        ),
    ]