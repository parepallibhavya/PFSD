from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Admin(AbstractBaseUser):
    email = models.CharField(max_length=50, blank=False, unique=True)
    phno = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    class Meta:
        db_table ="admin_table"

    def __str__(self):
        return self.username

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30,blank=False)
    email = models.CharField(max_length=50, blank=False, unique=True)
    phno = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)
    class Meta:
        db_table = "register_table"

class Service(models.Model):
    name = models.CharField(max_length=100)
    Services_choices=(("car booking","Car Booking"),("car driver booking","Car Driver Booking"),("car renting","Car Renting"),("car services","Car Services"),("feedback","Feedback"),("price calculator","Price Calculator"))
    Services=models.CharField(max_length=200,blank=False,choices=Services_choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class CarServices(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    pickup = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.name

    class CardriverBooking(models.Model):
        name = models.CharField(max_length=122)
        email = models.CharField(max_length=122)
        phone = models.CharField(max_length=12)
        pickup = models.CharField(max_length=122)
        destination = models.CharField(max_length=122)
        date = models.DateField(null=True)
        time = models.TimeField(null=True)
        def __str__(self):
            return self.name


class CarBooking(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    model = models.CharField(max_length=50)
    pickup = models.CharField(max_length=122)
    destination = models.CharField(max_length=122)
    pickdate = models.DateField(null=True)
    pickuptime = models.TimeField(null=True)
    dropdate = models.DateField(null=True)
    droptime = models.TimeField(null=True)

    def __str__(self):
        return self.name

