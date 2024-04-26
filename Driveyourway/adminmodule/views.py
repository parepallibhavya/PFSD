from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Admin, Register
from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def home(request):
    return render(request, "adminhome.html")
def viewallcustomers(request):
    return render(request,"view_all_customers.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username taken...")
                return render(request, "register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")


class CarBooking:
    pass


def carbooking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        model = request.POST.get('model')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        pickdate = request.POST.get('pickdate')
        pickuptime = request.POST.get('pickuptime')
        dropdate = request.POST.get('dropdate')
        droptime = request.POST.get('droptime')
        carbooking = CarBooking(name=name, email=email, phone=phone, destination=destination, pickdate=pickdate,
                                pickuptime=pickuptime, dropdate=dropdate, droptime=droptime, pickup=pickup, model=model)
        carbooking.save()

        return render(request, 'payment.html')

    return render(request, 'carbooking.html')
def payment(request):
    return render(request,'payment.html')
def carDriverBooking(name, email, phone, destination, date, time, pickup):
    pass
def cardriverbooking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        cardriverbooking = carDriverBooking(name=name, email=email, phone=phone, destination=destination, date=date, time=time, pickup=pickup)
        cardriverbooking.save()
        return render(request, 'payment.html')

    return render(request, 'cardriverbooking.html')


class CarServices:
    pass


def carservices(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        carservices = CarServices(name=name, email=email, phone=phone, destination=destination,date = date,time = time,pickup=pickup)
        carservices.save()
        return render(request,'payment.html')

    return render(request,'carservices.html')
def calculator(request):
    return render(request, 'calculator.html')
def confirm(request):
    return render(request,'confirm.html')




