from django.shortcuts import render

# Create your views here.
def index_info(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    return render(request,'newsApp/index.html')


def sportsinfo(request):
    return render(request,'newsApp/index.html')


def politicsinfo(request):
    return render(request,'newsApp/index.html')