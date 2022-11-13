from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def empdata(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_data':emp_list}
    return render(request, 'testapp/emp.html',context=my_dict)
