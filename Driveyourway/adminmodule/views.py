from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def customermodule(request):
    return render(request,customermodule.html)
def sellermodule(request):
    return render(request,sellermodule.html)
