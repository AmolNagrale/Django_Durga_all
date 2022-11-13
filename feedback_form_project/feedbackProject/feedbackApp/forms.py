

# This is the explicite validatioon from programmer is successfully !!!!
from django import forms
from django.core import validators
from django.forms.fields import EmailField
from django.forms.widgets import Textarea


class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean(self):
        print('Bot validation.......')
        cleaned_data=super().clean()
        bot_handler_value=cleaned_data['bot_handler']
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        #if inputpwd != inputrpwd:
        if len (bot_handler_value) <0:
            raise forms.ValidationError(' Thanks Bot !!')




# from django import forms
# from django.core import validators

# def gmail_verification(value):
#     if value[len(value)-9:] !='gmail.com':
#         raise forms.ValidationError('must be gmail')

# class FeedBackForm(forms.Form):
#     name=forms.CharField()
#     rollno= forms.IntegerField()
#     email=forms.EmailField(validators=['gmail_verification'])
#     feedback=forms.CharField(widget=forms.Textarea)


# this code for the gmail verification at time of input field 







# from django import forms
# from django.core import validators

# def starts_with_d(value):
# #    if value[0].lower() !='d':
#     if value.isalpha() !=True:
#         raise forms.ValidationError('name should be start with d')


# class FeedBackForm(forms.Form):
#     name = forms.CharField(validators=['starts_with_d'])
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
#     # this is use for the validation on input field of the feedback field...







# from django import forms
# from django.core import validators
# class FeedBackForm(forms.Form):
#     name = forms.CharField(validators=['starts_with_d'])
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])



#     def clean_name(self):   
#         inputname=self.cleaned_data['name']
#         if len(inputname)<4:
#             raise forms.ValidationError('The lenght of name field should be <4')
#         return inputname

#     def clean_rollno(self):
#         inputrollno=self.cleaned_data['rollno']
#         print('validating rollno')
#         return inputrollno

#     def cleaned_mail(self):
#         inputmail=self.cleaned_mail['email']
#         print('Validating Email')
#         return inputmail

#     def cleaned_feedback(self):
#         inputfeedback=self.cleaned_data['feedback']
#         print('Validating feedback')
#         return inputfeedback 