from django.contrib import admin
from modelformApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','mark']

    # Register your models here.
admin.site.register(Student,StudentAdmin)
