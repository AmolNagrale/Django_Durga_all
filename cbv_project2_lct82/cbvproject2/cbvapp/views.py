from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cbvapp.models import Book
# Create your views here.

#fuction based views
# def info_view(request):
#     book=Book.objects.all()
#     return render(request,'cbvapp/info.html')


class BookListView(ListView):
    model=Book
    template_name='cbvapp/book.html'
    context_object_name='list_of_book'

    #default template: book_list.html
    #default context object: book_list

class BookDetailView(DetailView):
    model=Book
    #default template name:book_details.html 
    #default context: book or object
