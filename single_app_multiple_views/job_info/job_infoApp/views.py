from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hydjobsinfo(request):
    return HttpResponse ('<h1> hydrabad jobs information </h1>')

def bngjobsinfo(request):
    return HttpResponse ('<h1> banglore jobs information </h1>')   

def punjobsinfo(request):
    return HttpResponse ('<h1> pune jobs information </h1>')

def chnjobsinfo(request):
    return HttpResponse ('<h1> Chennai jobs information </h1>')

def mumjobsinfo(request):
    return HttpResponse ('<h1> mumbai jobs information </h1>')
