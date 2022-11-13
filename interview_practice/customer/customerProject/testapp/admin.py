from django.contrib import admin
from testapp.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','ename','eno','mailid','phonenumber','age']


admin.site.register(Customer,CustomerAdmin)