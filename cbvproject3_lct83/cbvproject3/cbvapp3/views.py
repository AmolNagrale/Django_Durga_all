from django.shortcuts import render
from django.views.generic.base import View
from cbvapp3.models import Company
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model=Company


class CompanyDetailview(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')

    
class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')