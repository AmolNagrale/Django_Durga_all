from django.shortcuts import render
from filterApp.models  import FilterModel

# Create your views here.
def upper_view(request):
    data_list = FilterModel.objects.all()
    return render (request,'filterApp/upper.html',{'data_list':data_list})

def lower_view(request):
    data_list = FilterModel.objects.all()
    return render (request,'filterApp/lower.html',{'data_list':data_list})