from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.response import Response
from testapp.serializers import EmployeeSerializers
from testapp.models import Employee
from rest_framework import viewsets

# Create your views here.
class EmployeeAPI(viewsets.ViewSet):
    def list(self,request,*args, **kwargs):
        emp = Employee.object.all()
        Serializer = EmployeeSerializers(emp)
        return Response(Serializer.data)

    def retrieve(self,request, *args,**kwargs):
        emp = Employee.object.all()
        serializer = EmployeeSerializers(emp)
        return Response(serializer.data)

    def create(self,request,*args,**kwargs):
        serializer = EmployeeSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            msg = {"msg" : "Data is created successfully"}
            return Response(msg)
        else:
            return Response(serializer.errors)

    def update(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            emp = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializers(emp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                msg = {"msg": "Driver Updated successfully"}
                return Response(msg)
            else:
                return Response(serializer.errors)
        else:
            msg = {"msg": "None id"}
            return Response(msg)
    
    def partial_update(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            emp = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializers(emp, data = request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                msg = {"msg": "Driver Updated successfully"}
                return Response(msg)
            else:
                return Response(serializer.errors)
        else:
            msg = {"msg": "None id"}
            return Response(msg)


    def destroy(self,request,pk,*args,**kwargs):
        stud = Employee.objects.get(pk=pk)
        if stud is not None:
            stud.delete()
            msg = {"msg": "Driver Deleted"}
            return Response(msg)
        else:
            msg = {"msg": "Driver not found"}
            return Response(msg)
    
