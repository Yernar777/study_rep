from .models import *
from django import forms


class ReviewForms(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['name', 'email', 'review_text']