from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistration(UserCreationForm):
    """
    Based on code from the two tutorials in views.py
    """
    email=forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']