from django.shortcuts import render
import datetime
# Create your views here.
def tempviews(request):
    date=datetime.datetime.now()
    my_dict={'date_msg': date}
    return render(request,'testApp/wish.html', context=my_dict)
