# Generated by Django 3.0 on 2019-12-31 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0016_auto_20191117_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
