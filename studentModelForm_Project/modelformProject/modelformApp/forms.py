from django import forms
from django.forms import fields
from modelformApp.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
