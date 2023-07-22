from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django import forms
from .models import *

class SignupForm(UserCreationForm):
    email: forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'text', 'name':'name', 'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'email', 'name':'email', 'placeholder': 'Enter your email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'password', 'name':'password', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'password', 'name':'password', 'placeholder': 'Confirm your password'})

