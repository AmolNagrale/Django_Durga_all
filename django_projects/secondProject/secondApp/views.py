from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def time_info_view(request):
    time=datetime.datetime.now()
    s='<h1> hello friends Good Morning !!!! </h1>''<hr>'
    s=s+'<h1> Hello current Date and time is:' +str(time)+'</h1>'
    return HttpResponse(s)