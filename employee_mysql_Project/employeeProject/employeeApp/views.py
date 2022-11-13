from django.shortcuts import render
from employeeApp.models import Employee

# Create your views here.


def index(response):
    return render(response, 'employeeApp/index.html')

def empview(request):
    emp_list=Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request, 'employeeApp/emp.html', context=my_dict)
