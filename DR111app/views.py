from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def alumlogin(request):
    return render(request,'alumlogin.html')
def clglogin(request):
    return render(request,'clglogin.html')
def dtlogin(request):
    return render(request,'dtlogin.html')
def alumregistration_1(request):
    return render(request,'alumniregistration_1.html')