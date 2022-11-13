from django.contrib import admin
from employeeApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','addr']

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)

