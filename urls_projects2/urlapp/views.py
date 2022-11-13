from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hydjobsinfo(request):
    s = '<h1> Welcome to Hydrabad jobs information </h1>'
    return HttpResponse(s)

def punejobsinfo(request):
    s = '<h1> Welcome to Pune jobs information </h1>'
    return HttpResponse(s)

def mumbaijobsinfo(request):
    s = '<h1> Welcome to Mumbai jobs information </h1>'
    return HttpResponse(s)

def noidajobsinfo(request):
    s = '<h1> Welcome to noida jobs information </h1>'
    return HttpResponse(s)