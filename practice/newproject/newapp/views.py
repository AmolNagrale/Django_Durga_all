from django.shortcuts import render
from newapp import views

# Create your views here.
def goodmorning(request):
    return render(request, 'newapp/base.html' )