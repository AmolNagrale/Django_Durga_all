from django.contrib import admin
from filterApp.models import FilterModel

# Register your models here.
class FliterModelAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']


admin.site.register(FilterModel,FliterModelAdmin)