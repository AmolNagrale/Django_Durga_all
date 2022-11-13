from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    request.session.set_test_cookies()
    return HttpResponse('<h1>index Page</h1>')

def check_view(request):
    if request.session.test_worked_cookies():
        print("Cookies are working properly")
        request.session.delete_test_cookies()
        return HttpResponse('<h1>Checking Page</h1>')
    