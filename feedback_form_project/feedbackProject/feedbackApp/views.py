from django.shortcuts import render
from . import forms

# Create your views here.


def thankyou_view(request):
    return render(request,'feedbackApp/thankyou.html')


def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedBackForm()
        

    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
    
        if form.is_valid():
            print('form validation success and printing feedback info ')
            print('student Name :', form.cleaned_data['name'])
            print('student Roll No :', form.cleaned_data['rollno'])
            print('student Email ID :', form.cleaned_data['email'])
            print('student Feedback :', form.cleaned_data['feedback'])
            print('student password :', form.cleaned_data['password'])
            print('student rpassword :', form.cleaned_data['rpassword'])

    return render(request, 'feedbackApp/feedback.html',{'form':form})

    



        