from django import forms
from django.forms.widgets import PasswordInput
from .models import UserModel
from django.db import models

class PasswordForm(UserModel):
    password2 = models.CharField(max_length=100)

class UserUpErro(forms.ModelForm):
    password2 = models.CharField()
    class Meta:
        model = PasswordForm
        fields=['username','email','password','password2']
        widgets = {"password": PasswordInput(), "password2": PasswordInput()}
