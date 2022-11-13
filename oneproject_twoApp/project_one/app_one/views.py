from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def first_app(request):
    return HttpResponse('<h1> This is fiest app </h1>')