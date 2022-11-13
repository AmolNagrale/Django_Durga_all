from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    user=request.user
    print(user)
    return HttpResponse('<h1>Welcome to django first project</h1>' '<hr>')


