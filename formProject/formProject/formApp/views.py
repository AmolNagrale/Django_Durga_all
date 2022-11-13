from django.shortcuts import render
from . import forms # we have already in form hence we have taken . only/ working on current working directory.
# Create your views here.

def studentregisterview(request):
    form=forms.StudentRegistration()
    return render (request, 'formApp/register.html',{'form':form}) # for the return the output in dict form.
