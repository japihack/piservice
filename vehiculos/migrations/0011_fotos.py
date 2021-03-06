# Generated by Django 2.2.5 on 2019-10-04 10:25

from django.db import migrations, models
import django.db.models.deletion
import vehiculos.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0010_vehiculo_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to=vehiculos.models.custom_upload_to)),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.Vehiculo')),
            ],
        ),
    ]
