from django.shortcuts import render
from modelformApp import forms
# Create your views here.
def student_view(request):
    form=forms.StudentForm()
    if request.method=="POST":
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('form data inserted into database successfully !!!')
    return render(request,'modelformApp/register.html',{'form':form})