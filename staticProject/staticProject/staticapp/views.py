from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'staticapp/index.html')


def sportsinfo(request):
    head_msg='Latest Sports Information'
    msg1 ='Kohli gave left and right to brodman Record'
    msg2 = 'India performance not upto the mark in asian Games'
    msg3 = 'First Gold accuired by china'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3 }
    return render(request, 'staticapp/index.html', context=my_dict)



def moviesinfo(request):
    head_msg='Latest movies Information'
    msg1 ='Sonali slowly getting cured'
    msg2 = 'Salman going to marriage soon'
    msg3 = 'Narendra Modi is going to act in some movie'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3 }
    return render(request, 'staticapp/index.html', context=my_dict)


def politicsinfo(request):
    head_msg = 'Latest Politics Information'
    msg1 = 'Intelagana election will come in two months'
    msg2 = 'Achhedin Aagayaa !!!'
    msg3 = 'Kerala money gaya..... Center wont accept and wont give  !!!'
    my_dict={'head_msg':head_msg, 'msg1':msg1,'msg2':msg2,'msg3':msg3 }
    return render(request, 'staticapp/index.html', context=my_dict)