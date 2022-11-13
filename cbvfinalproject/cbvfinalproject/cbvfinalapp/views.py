from django.shortcuts import render
from django.urls.base import reverse_lazy
from cbvfinalapp.models import Beer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class BeerListView(ListView):
    model=Beer


class BeerDetailView(DetailView):
    model=Beer

class BeerCreateView(CreateView):
    model=Beer
    #fields=('name','taste','color','price')
    fields='__all__'

class BeerUpdateView(UpdateView):
    model=Beer
    fields=('taste','color','price')

class BeerDeleteView(DeleteView):
    model=Beer
    success_url=reverse_lazy('home')