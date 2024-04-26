# Generated by Django 5.0.1 on 2024-03-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0009_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('model', models.CharField(max_length=50)),
                ('pickup', models.CharField(max_length=122)),
                ('destination', models.CharField(max_length=122)),
                ('pickdate', models.DateField(null=True)),
                ('pickuptime', models.TimeField(null=True)),
                ('dropdate', models.DateField(null=True)),
                ('droptime', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CardriverBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('pickup', models.CharField(max_length=122)),
                ('destination', models.CharField(max_length=122)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('pickup', models.CharField(max_length=122)),
                ('destination', models.CharField(max_length=122)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
