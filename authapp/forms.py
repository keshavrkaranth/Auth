from django.contrib.auth.models import User
from django import forms
from .models import *
class RegistrationForm(forms.ModelForm):
    phone_no  = forms.CharField(max_length=12)
    class Meta():
        model = User
        fields = ['first_name','last_name','phone_no','email','username','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control',}),
        }
        help_texts = {
            'username': None
        }



class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())
