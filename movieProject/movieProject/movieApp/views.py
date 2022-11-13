from django.shortcuts import render
from movieApp.models import Movie
from movieApp.forms import MovieForm
# Create your views here.

def index_view(request):
    return render(request,'movieApp/index.html')

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'movieApp/addmovie.html',{'form':form})

def list_movie_view(request):
    movies_list =Movie.objects.all()
    return render(request,'movieApp/listmovie.html',{'movies_list':movies_list})

