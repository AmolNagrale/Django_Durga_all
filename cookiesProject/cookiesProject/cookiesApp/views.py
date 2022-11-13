from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response=render(request,'cookiesApp/count.html', {'count':newcount})
    response.set_cookie('count',newcount, max_age=60) # instate of count we can use any name, as per our understating purpose
    return response