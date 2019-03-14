from django.contrib.auth.models import User
from django import forms

# inherit from base User class and override it and make our own 
class UserForm(forms.ModelForm):
    # we want the password characters to be hidden
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # specify the db we will be using
        model = User
        # what fields do we want to appear in the form?
        fields = ['username', 'email', 'password']