from django.contrib import admin
from testapp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['id','ename','location','salary','qualification']


admin.site.register(Book,BookAdmin)