from django.contrib import admin
from mi2app.models import Child, Parent, Student1, Subchild, Teacher1

# Register your models here.

admin.site.register(Student1)
admin.site.register(Teacher1)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Subchild)
