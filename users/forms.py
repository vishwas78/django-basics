from django.contrib.auth.models import User
from django import forms


class UserAuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
