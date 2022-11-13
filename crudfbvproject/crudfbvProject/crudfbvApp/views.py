from django.shortcuts import redirect, render
from crudfbvApp.models import Employee
from crudfbvApp.forms import EmployeeForm

# Create your views here.

def retrive_view(request):
    employees=Employee.objects.all()
    return render(request, 'crudfbvApp/index.html',{'employees':employees})


def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'crudfbvApp/create.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id) # this code for the deleting perticular id if we want to delete all table value we can use objects.all
    employee.delete()
    return redirect('/')


def update_view(request, id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST, instance=employee) # if we are not taken instance=employee then every record is updated as new entry in table.
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'crudfbvApp/update.html',{'employee':employee})

