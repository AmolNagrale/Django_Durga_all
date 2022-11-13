
from django.shortcuts import render
from sessionapp.forms import NameForm, AgeForm, GFForm

# Create your views here.

def name_views(request):
    form=NameForm()
    return render(request, 'sessionapp/name.html',{'form':form})


def age_views(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request, 'sessionapp/age.html',{'form':form})



def gf_views(request):
    age=request.GET['age']
    request.session['age']=age
    form=GFForm()
    return render(request, 'sessionapp/gf.html',{'form':form})

def result_views(request):
    gf=request.GET['gf']
    request.session['gf']=gf

    return render(request, 'sessionapp/result.html')