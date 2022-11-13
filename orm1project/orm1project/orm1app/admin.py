from django.contrib import admin
from orm1app.models import Employee1
# Register your models here.

class Employee1Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee1, Employee1Admin)