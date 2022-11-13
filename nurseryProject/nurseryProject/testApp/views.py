from django.shortcuts import render
import datetime

# Create your views here.
def base(request):
    date= datetime.datetime.now()
    guest='Amol'
    name='Amit'
    rollno=111
    mark=100
    msg=''
    h=int(date.strftime('%H'))
    if h<12:
        msg='Goog morning Have a great day'
    elif h<16:
        msg='Goog afternoon Have a great day'
    elif h<21:
        msg='Goog evening Have a great day'
    else:
        msg='Goog night!! sleep well sweet dearm !!!' 

    my_dict={'date':date, 'name':guest ,'msg':msg, mark:100, rollno:111, name:'Amit'}

    return render(request, 'testApp/base.html', context=my_dict)


def result(request):
    return render(request, 'testApp/result.html')