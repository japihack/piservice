# Generated by Django 2.2.5 on 2019-09-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_auto_20190923_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(default='0', max_length=9),
        ),
    ]