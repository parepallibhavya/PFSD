from django.shortcuts import render


def homePage(request):
    return render(request,"homepage.html")
def loginpage(request):
    return render(request,"login1.html")
def registrationpage(request):
    return render(request,"register.html")
def aboutpage(request):
    return render(request,"about.html")
def conatctuspage(request):
    return render(request,"contactus.html")





