# Generated by Django 5.0.1 on 2024-02-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0003_alter_car_carprice_alter_car_carseating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='carprice',
        ),
        migrations.RemoveField(
            model_name='car',
            name='carseating',
        ),
    ]