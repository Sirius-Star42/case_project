from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, BooleanField
from django import forms

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':'form-control', 
            'type':'password', 
            'style': 'max-width: 100%; margin-top: 0.5vh',
            'placeholder': '*****'
            }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class':'form-control', 
            'type':'password', 
            'style': 'max-width: 100%; margin-top: 0.5vh',
            'placeholder': '*****'
            }),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser', 'is_staff']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100%; margin-top: 0.5vh',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 100%; margin-top: 0.5vh',
                'placeholder': 'Email'
                }),
        }
