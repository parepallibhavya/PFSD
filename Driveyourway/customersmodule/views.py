from django.shortcuts import render

# Create your views here.
def Customerhome(request):
    return render(request, 'Customerhome.html')
def Viewallbookings(request):
    return render(request,'viewallbookings.html')
def feedback(request):
    return render(request,'feedback.html')
def logout(request):
    return render(request, 'logout.html')
