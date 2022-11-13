from django.shortcuts import render
from sessionapp3.forms import AddItemForm

# Create your views here.
def Add_item_view(request):
    form=AddItemForm()
    if request.method=="POST":
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(20)
    return render(request,'sessionapp3/additem.html',{'form':form})

def display_item_view(request):
    return render (request,'sessionapp3/displayitem.html')

def session_info_view(request):
    session=request.sessions
    age=session.get_expiry_age()
    date=session.get_expiry_date()
    print('Expiry Age:',age)
    print('Expirt Date',date)

