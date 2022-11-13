from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'advTempApp/home.html')

def movies_view(request):
    return render(request,'advTempApp/movies.html')

def sports_view(request):
    return render(request,'advTempApp/sports.html')

def politics_view(request):
    return render(request,'advTempApp/politics.html')