from django.contrib import admin
from cbvapp3.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','location','ceo']

admin.site.register(Company, CompanyAdmin)


 