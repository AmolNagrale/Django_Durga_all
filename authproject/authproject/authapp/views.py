
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request, 'authapp/home.html')

@login_required
def java_exam_view(request):
    return render(request, 'authapp/javaexam.html')

@login_required
def python_exam_view(request):
    return render(request, 'authapp/pythonexam.html')

@login_required
def aptitude_exam_view(request):
    return render(request, 'authapp/aptitudeexam.html') 

def logout_view(request):
    return render(request, 'authapp/logout.html')

def signup_view(request):
    form= SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)

        if form.is_valid(): 
            # user=form.save()             #this is the implicite validation   # internally encrypting the password 
            # form.save()
            # user.save()

            user=form.save()
            user.set_password(user.password)    # this is the explicite validation by programmer # our password in encrypted form
            user.save()
            form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form':form})