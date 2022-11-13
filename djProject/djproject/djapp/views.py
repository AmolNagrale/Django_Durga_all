from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'djapp/home.html')

def banjobs(request):
    return render(request, 'djapp/banglore.html')

def chnjobs(request):
    return render(request, 'djapp/chennai.html')

def hydjobs(request):
    return render(request, 'djapp/hydjob.html')

def punejobs(request):
    return render(request, 'djapp/punejob.html')

