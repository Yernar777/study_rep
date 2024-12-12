from .models import *
from django import forms
from django.contrib.auth.models import User

from django.forms.widgets import TextInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm




class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())




class ReviewForms(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['name', 'email', 'review_text']

class ReviewForms1(forms.ModelForm):
    class Meta:
        model = Review1
        fields = ['email',]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'otziv', 'placeholder': 'Email'})
        }
        labels = {
            'email': ''
        }