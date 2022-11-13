from django.contrib import admin
from djapp.models import hydjobs,banjobs,punejobs,chnjobs


# Register your models here.
class hydjobAdmin(admin.ModelAdmin):
    list_display = ['date', 'company','title','eligibility','address','email','phonenumber']


class punejobAdmin(admin.ModelAdmin):
    list_display = ['date', 'company','title','eligibility','address','email','phonenumber']


class chnjobAdmin(admin.ModelAdmin):
    list_display = ['date', 'company','title','eligibility','address','email','phonenumber']

class banjobAdmin(admin.ModelAdmin):
    list_display = ['date', 'company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hydjobAdmin)
admin.site.register(banjobs,banjobAdmin)
admin.site.register(chnjobs,chnjobAdmin)
admin.site.register(punejobs,punejobAdmin)