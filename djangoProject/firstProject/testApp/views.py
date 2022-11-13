from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s='<h1>Hello welcome to Django Classes...Django is nursary level concept</h1>'
    return HttpResponse(s)

