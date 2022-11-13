from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'durganewsapp/index.html')


def moviesinfo(request):
    head_msg = 'Latest movie information'
    msg1='sonali slowly getting cured'
    msg2='Salman gonig to marrigae soon'
    msg3='Modi is going to act in some movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request, 'durganewsapp/news.html',context=my_dict)


def sportsinfo(request):
    head_msg = 'Latest Sports information'
    msg1='yesterday IPL match own by MI '
    msg2='Kohli will take sansyas from T-20 & one day matchs'
    msg3='Mr. Dhoni assign as a mentor to indian team'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request, 'durganewsapp/news.html',context=my_dict)


def politicsinfo(request):
    head_msg = 'Latest movie information'
    msg1='sonali slowly getting cured'
    msg2='Salman gonig to marrigae soon'
    msg3='Modi is going to act in some movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request, 'durganewsapp/news.html',context=my_dict)