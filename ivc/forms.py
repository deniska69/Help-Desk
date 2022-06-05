from django.contrib.auth.models import User
from django import forms
from .models import App

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AppForm(forms.ModelForm):

    class Meta:
        model = App
        fields = ['tp', 'cr', 'note']